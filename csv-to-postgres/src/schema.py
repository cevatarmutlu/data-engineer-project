from pyspark.sql.types import StructType,StructField, StringType, IntegerType, DateType, BooleanType

netflix_title_schema = StructType([
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

users_schema = StructType([
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

schemas = {
    "netflix_title": netflix_title_schema,
    "users": users_schema
}