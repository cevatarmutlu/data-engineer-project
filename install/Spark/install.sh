## install Java
sudo apt update -y
sudo apt install openjdk-8-jdk -y

# verison: Spark 3.2.0
wget https://dlcdn.apache.org/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz

tar -xzvf spark-3.2.0-bin-hadoop3.2.tgz

rm spark-3.2.0-bin-hadoop3.2.tgz
