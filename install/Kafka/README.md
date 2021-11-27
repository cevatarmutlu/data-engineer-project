## Kafka Kurulumu

Bu döküman sıfır bir `linux` bilgisayara `Kafka` kurulumunun nasıl yapıldığını anlatacaktır.


## Java kurulumu

Kafka kurulum için Java' ya ihtiyaç duymaktadır. Bu dokümanda Java olarak Java8 kurulmuştur. 

> Kafka, Java8 ve sonraki Java sürümlerini desteklemektedir.

Java kurulumu:

    sudo apt install openjdk-8-jdk -y

## Kafka Kurulumu

Kafka' nın 3.0.0 sürümü indirilmiştir. Scala verision olarak 2.13 olanı tercih edilmiştir.

### İndirme

    wget https://dlcdn.apache.org/kafka/3.0.0/kafka_2.13-3.0.0.tgz

### Zip' ten çıkarma

    tar -xzvf kafka_2.13-3.0.0.tgz

### Kafka ve Zookeeper' ı başlatma

Bu işlem için iki farklı terminal açın ve iki terminal ile kafka dizinine gidin ve aşağıdaki komutları girin

Birinci terminal. Zookeeper' ı başlatma komutu

    bin/zookeeper-server-start.sh config/zookeeper.properties

İkinci terminal. Kafka' yı başlatma komutu

    bin/kafka-server-start.sh config/server.properties

### Topic oluşturma

Yeni bir terminal başlatarak kafka dizinine gidin ve aşağıdaki komutu çalıştırın. Aşağıdaki komut TOPIC_NAME adında bir topic oluşturur.

    bin/kafka-topics.sh --create --topic TOPIC_NAME --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

> Yukarıdaki topic oluşturma komutu farklı sürümlere göre değişiklik gösterebilir.