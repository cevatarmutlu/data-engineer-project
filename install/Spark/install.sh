## install Java
sudo apt update -y
sudo apt install openjdk-8-jdk -y

## which java
## readlink -f path
## write to .bashrc export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/

# verison: Spark 3.2.0
wget https://dlcdn.apache.org/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz

tar -xzvf spark-3.2.0-bin-hadoop3.2.tgz

rm spark-3.2.0-bin-hadoop3.2.tgz

## cd spark-3.2.0-bin-hadoop3.2/bin
## ./spark-shell

## SPARK HOME -> .bashrc
# export SPARK_HOME=spark_path
