# Application Code

In the following documentation going to describe the [code](aiven_excercise.py) line by line .

## From lines (1-7)

Import all python packages which is going to help in making our Application

|    Library    |                     Description                      |
| :-----------: | :--------------------------------------------------: |
| KafkaProducer |            It will help to data to topic             |
| KafkaConsumer |      this library is use for cosuming the data       |
|    pandas     | using pandas to storing consuimng data in postgresql |
|  sqlalchemy   |         used to connect python with database         |
|     faker     |              for generating random data              |

## from lines(9-10)

Create a `json_serializer` funtion to converts the Python objects into appropriate json objects. We create this because Serialization is the process of converting an object into a stream of bytes that are used for transmission and Kafka stores and transmit these bytes of arrays in its queue.

## Line 12

Here we are creating producer to send data by using `kafkaProducer`

|       key        |      value       |               description                |
| :--------------: | :--------------: | :--------------------------------------: |
| bootstrap_server | "localhost:9092" |                  client                  |
| value_serializer | json_serializer  | using funtion which we intialized before |

## from lines (14-23)

create funtion `producer_func(p)` which will generate the random data to send to topic `demo`

## from lines (26-56)

In this fucntion consumer will cosume the data by using `kafkaConsumer`.

|        key        |       value        |                                                               description                                                                |
| :---------------: | :----------------: | :--------------------------------------------------------------------------------------------------------------------------------------: |
|       topic       |       "demo"       |                                                                  client                                                                  |
| bootstrap_server  |  "localhost:9092"  |                                                                  client                                                                  |
| auto_offset_reset |     "earliest"     | it is a property to specify whether you want to consume the records from the beginning (earliest) or the last committed offset (latest). |
|     group_id      | "consumer_group_b" |                                                                                                                                          |

In this function it will print out the all the topics,partition and the offset.

Most importantly all of the consumed data will be store in list(`Data`) which will then push to postgresql by `pandas`. Further Pandas Daframe can be used for analyzing and visualizing the data .
