from faker import Faker
from kafka import KafkaProducer
from kafka import KafkaConsumer, TopicPartition
import pandas as pd
import time
from sqlalchemy import create_engine
import json

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer= KafkaProducer(bootstrap_servers=["localhost:9092"],value_serializer=json_serializer)

def producer_func(p):

    fake = Faker()
    i=0
    while i<=10:
        register_user = {"name" : fake.name(),"address" : fake.address(),"created_at" : fake.year()}
        producer.send("demo",register_user)
        time.sleep(1)
        i+=1
    producer.close()


def consumer_func():
    consumer = KafkaConsumer("demo",bootstrap_servers= "localhost:9092",auto_offset_reset="earliest",group_id="consumer_group_b") 
    data=[]


    #get all the partiton
    PARTITIONS = []
    for partition in consumer.partitions_for_topic("demo"):
        PARTITIONS.append(TopicPartition("demo", partition))


    # get all offsets
    end_offsets = consumer.end_offsets(PARTITIONS)
    print("Topic Patitions = ",end_offsets)



    for msg in consumer:
        data.append(json.loads(msg.value))
        if len(data) == 10:
            break



    #creating pandas dataframe which will import directly into postgrsql database

    df= pd.DataFrame.from_dict(data, orient='columns')
    print("total data")
    print(df)
    engine=create_engine('postgres+psycopg2://avnadmin:e2g6lh35onw1lze8@testpostgres-wattoorocx-963f.aivencloud.com:16577/defaultdb')
    con = engine.connect()
    df.to_sql('table2', engine)


if __name__ =="__main__":
    producer_func(producer)
    consumer_func()


