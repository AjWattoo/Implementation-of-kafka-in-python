# Quick Guide

## Introduction

This demo application describing how user can send data to a kafka topic and then read by kafka consumer. Then application will store the consumed data in `Postgreql`. To run this demo user have to go thorugh following steps:

1. Download kafka
2. Install Kafka
3. Run zookeeper
4. Run kafka server
5. Install and run CMAK(_optional_ kafka manager for better vizualitzation to create topic and partition)
6. Run python script
7. Test application

## Download kafka

To download the kafka,run this on termial

```
wget https://apache.mirror.digionline.de/kafka/2.8.0/kafka_2.13-2.8.0.tgz
```

## Install kafka

Extract a tar.gz archive. The following command shell helps to extract tar files out a tar.gz archive.

```
tar -xvzf kafka_2.13-2.8.0.tgz
```

| Key |                             Value                              |
| :-: | :------------------------------------------------------------: |
|  x  |                         extract files                          |
|  v  | Verbose, print the file names as they are extracted one by one |
|  z  |                  The file is a “gzipped” file                  |
|  f  |        Use the following tar archive for the operation         |

## Run zookeeper

Start the ZooKeeper service

```
bin/zookeeper-server-start.sh config/zookeeper.properties
```

## Run kafka-server

open another terminal session and start the Kafka broker service

```
$ bin/kafka-server-start.sh config/server.properties
```

## Creating topic

So before you can write your events, you must create a topic.There are two ways to do that

- From terminal

```
bin/kafka-topics.sh --create --topic demo --bootstrap-server localhost:9092
```

- From [CMAK](https://github.com/yahoo/CMAK)

Thia will give you better idea of cluster,partitions,topic,replication factor and consumer groups. To install and run this used following commands on the teminal

```
wget https://github.com/yahoo/CMAK.git
```

Go into the folder CMAK and run this to activate the manger

```
bin/cmak -Dconfig.file=/path/to/application.conf -Dhttp.port=8080
```

Run on browser

```
localhost:8080
```

In brower we have a beautiful GUI of kafka manager where we can easily manage and see our data.

## Run python script

```Python
python kafka_code.py
```

## Run application test

```Python
pytest test.py
```
