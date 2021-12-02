import argparse
from pyspark.sql import SparkSession
from src.schema import schemas
import src.config as config
from src.transform import transfroms

def getVariables():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--csv', help="Csv path", required=True, type=str)
    parser.add_argument('-s', '--schema', help="Schema name in schema.py", required=True, type=str)
    parser.add_argument('-he', '--header', help="If csv file not contains a header row header should be false. Default: true", type=str, default="true")
    parser.add_argument('-tb', '--table', help="table name", type=str, required=True)
    parser.add_argument('-tr', '--transform', help="transform name in transform.py", type=str)

    args = parser.parse_args()

    csv = args.csv
    schema = args.schema
    header = args.header
    table = args.table
    transform = args.transform

    return csv, schema, header, table, transform

if __name__ == "__main__":
## Notnull olmayacak kolona gerçekten notnull değer gelmediğinden emin ol

    csv, schema, header, table, transform = getVariables()
    conf = config.get("database-configs")

    spark = SparkSession \
            .builder \
            .config("spark.jars", "src/jars/postgresql-42.2.5.jar") \
            .getOrCreate()

    df = spark.read.csv(
        path=csv,
        schema=schemas.get(schema),
        header=header,
    )

    if transform != None:
        df = transfroms.get(transform)(df)

    df.write.format("jdbc").option("url", f"jdbc:{conf.get('rdbms')}://{conf.get('host')}:{conf.get('port')}/{conf.get('db-name')}") \
        .option("dbtable", table) \
        .option("user", conf.get('user')) \
        .option("password", conf.get('password')) \
        .option("driver", conf.get('driver')) \
        .mode('append') \
        .save()

# users: spark-submit --driver-class-path src/jars/postgresql-42.2.5.jar main.py -c src/resource/users.csv -s users -tb users -tr users
# netflix_title: spark-submit --driver-class-path src/jars/postgresql-42.2.5.jar main.py -c src/resource/netflix_titles.csv -s netflix_title -tb deneme -tr netflix_title
