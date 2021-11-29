from pyspark.sql import SparkSession

spark = SparkSession \
            .builder \
            .getOrCreate()

from pyspark.sql.types import StructType,StructField, StringType, IntegerType, DateType, BooleanType
schema = StructType([
    StructField("id",IntegerType(),False),
    StructField("username",StringType(),False),
    StructField("password",StringType(),False),
    StructField("mail", StringType(), False),
    StructField("name", StringType(), True),
    StructField("surname", StringType(), True),
    StructField("start", DateType(), False),
    StructField("is_active", BooleanType(), False),
    StructField("end", DateType(), False),
])

csv_path = "users.csv"
df = spark.read.csv(
    path=csv_path,
    schema=schema,
    header="true",
    dateFormat="yyyy-MM-d"
)
df.show()
# # csv function options: https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option

df.write.format("jdbc").option("url", "jdbc:postgresql://localhost:5432/postgres") \
        .option("dbtable", "users") \
        .option("user", "postgres") \
        .option("password", "123") \
        .option("driver", "org.postgresql.Driver") \
        .mode('append') \
        .save()
