from pyspark.sql import SparkSession

spark = SparkSession \
            .builder \
            .getOrCreate()

from pyspark.sql.types import StructType,StructField, StringType, IntegerType, DateType
from pyspark.sql.functions import monotonically_increasing_id, to_date

schema = StructType([
    StructField("show_id",StringType(),True),
    StructField("type",StringType(),True),
    StructField("title",StringType(),True),
    StructField("director", StringType(), True),
    StructField("cast", StringType(), True),
    StructField("country", StringType(), True),
    StructField("date_added", DateType(), True),
    StructField("release_year", IntegerType(), True),
    StructField("rating", StringType(), True),
    StructField("duration", StringType(), True),
    StructField("listed_in", StringType(), True),
    StructField("description", StringType(), True),
])

csv_path = "/home/cevat/workspace/data-engineer-project/netflix_titles.csv"
df = spark.read.csv(
    path=csv_path,
    schema=schema,
    header="true",
    dateFormat="MMMM d, yyyy"
)
# csv function options: https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option

df.printSchema()

from pyspark.sql.functions import col, lit, split, when
df.printSchema()
## Notnull olmayacak kolona gerçekten notnull değer gelmediğinden emin ol
df = df.filter(col("type") == "Movie").withColumn("show_id", monotonically_increasing_id())

df.write.format("jdbc").option("url", "jdbc:postgresql://localhost:5432/postgres") \
        .option("dbtable", "deneme") \
        .option("user", "postgres") \
        .option("password", "123") \
        .option("driver", "org.postgresql.Driver") \
        .mode('append') \
        .save()
