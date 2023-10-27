from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()



parDF1=spark.read.parquet("inventory.parquet")


print(parDF1)
