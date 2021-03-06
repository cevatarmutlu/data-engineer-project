from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window, to_timestamp
from pyspark.sql.types import StringType, StructType, StructField, IntegerType, ArrayType

schema = StructType([
    StructField("user_id",IntegerType(),False),
    StructField("status",StringType(),False),
    StructField("film_watch",StringType(),False),
    StructField("movie", ArrayType(StructType([
      StructField("show_id",IntegerType(),True),
      StructField("title", StringType(), True),
      StructField("listed_in", StringType(), True)
    ])), True)
])

spark = SparkSession \
        .builder \
        .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "user_activities") \
    .load()

# df = df.selectExpr("CAST(value AS STRING)")
df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")


# # %Y-%m-%d %H-%M-%S
ta = df.withColumn("start_time", to_timestamp(col("start_time") ,"yyyy-L-d H-m-s")).withColumn("end_date", to_timestamp(col("end_date"), "yyyy-MM-d k-m-s"))
ta.printSchema()
# za = ta.groupBy("movie_id", "start-time").count()
# # df = data.groupBy(window(col("start_time"), "30 seconds", "5 seconds") ,col("movie_id")).count()
df = ta.withWatermark("start_time", "10 seconds").groupBy(window(col("start_time"), "10 seconds", "5 seconds"), "movie_id").count().orderBy("movie_id")
# # bir üst satırın kaynak: https://databricks.com/blog/2021/10/12/native-support-of-session-window-in-spark-structured-streaming.html

horse = movie.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .start()

horse.awaitTermination()
# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0
