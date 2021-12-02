from pyspark.sql.functions import col, monotonically_increasing_id, split, to_timestamp

def netflix_transform(df):
    return df \
        .filter(col("type") == "Movie") \
        .withColumn("show_id", monotonically_increasing_id()) \
        .withColumn("date_added", to_timestamp(col("date_added"), "MMMM d, yyyy")) \
        .withColumn("duration", split(col("duration"), " ").getItem(0).cast("integer"))


def users_tranform(df):
    return df.withColumn("start", to_timestamp(col("start"), "yyyy-MM-d"))

transfroms = {
    'netflix_title': netflix_transform,
    'users': users_tranform
}