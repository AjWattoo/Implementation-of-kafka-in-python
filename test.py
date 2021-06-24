import pandas as pd
from sqlalchemy import create_engine
import pytest
import json
from kafka import KafkaConsumer, TopicPartition
from kafka import KafkaProducer


@pytest.fixture
def produce():
    producer= KafkaProducer(bootstrap_servers=["localhost:9092"])
    register_user = {"name" : "ahmad","address" : "lynasstr 5","created_at" : "2021"}
    producer.send("demo",json.dumps(register_user).encode("utf-8"))
    producer.close()

def test_database():
    engine=create_engine('postgres+psycopg2://avnadmin:e2g6lh35onw1lze8@testpostgres-wattoorocx-963f.aivencloud.com:16577/defaultdb')
    df_test=pd.read_sql_query("SELECT * FROM table_name ",engine)
    assert len(df_test.columns) == 4
    assert df_test.columns[0] == 'index'
    assert df_test.columns[1] == 'name'
    assert df_test.columns[2] == 'address'
    assert df_test.columns[3] == 'created_at'

def test_cosumer_getting_data(produce):
    consumer = KafkaConsumer("demo",bootstrap_servers= "localhost:9092",auto_offset_reset="earliest",group_id="consumer_group_b") 
    for msg in consumer:
        consumer_data = json.loads(msg.value)
        break
    assert consumer_data is not None

    assert list(consumer_data.keys())[0]  == "name"
    assert list(consumer_data.keys())[1] == "address"
    assert list(consumer_data.keys())[2]  == "created_at"

def test_partition(produce):
    consumer = KafkaConsumer("demo",bootstrap_servers= "localhost:9092",auto_offset_reset="earliest",group_id="consumer_group_b") 
    PARTITIONS = []
    for partition in consumer.partitions_for_topic("demo"):
        PARTITIONS.append(TopicPartition("demo", partition))

    assert len(PARTITIONS) == 3
