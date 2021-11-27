## update
sudo apt update -y
sudo apt install openjdk-8-jdk -y

SCALA_VERSION=2.13
KAFKA_VERSION=3.0.0

## Download tgz
wget https://downloads.apache.org/kafka/$KAFKA_VERSION/kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz

## Extract tgz
tar -xzvf kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz

## Remove tgz
rm kafka_2.12-$KAFKA_VERSION.tgz
