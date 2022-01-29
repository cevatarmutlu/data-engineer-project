from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

schema = StructType([
    StructField("user_id",IntegerType(),False),
    StructField("film_watch",BooleanType(),False),
    StructField("movie", MapType(StringType(), StringType(), True)),
    StructField("timestamp",StringType(),False),
])

# pyspark --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0,org.elasticsearch:elasticsearch-spark-30_2.12:7.16.0

# spark.sparkContext.setLogLevel("ERROR")

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "user_activities") \
    .load()

# .withColumn(col('movie.listed_in'), split(col('movie.listed_in'), ','))

data = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*").withColumn('timestamp', to_timestamp(col('timestamp'), 'yyyy-L-d H:m:s')).withColumn('movie_categories', split(col('movie.listed_in'), ',')).drop(col('movie.listed_in'))


query = data.writeStream \
.outputMode("append") \
.format("es") \
.option("es.nodes", "localhost") \
.option("es.port", 9200) \
.option("checkpointLocation", "/tmp/") \
.start("/movie_logs")
query.awaitTermination()

horse = data.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .start()

horse.awaitTermination()
