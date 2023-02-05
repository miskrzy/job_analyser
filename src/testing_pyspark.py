from pyspark.sql import SparkSession


spark = SparkSession.builder.getOrCreate()

data = [('123', 123), ('1234', 1234), ('12345', 12345), ('123456', 123456), ('1234567', 1234567)]

rdd = spark.sparkContext.parallelize(data)
print(type(rdd))
