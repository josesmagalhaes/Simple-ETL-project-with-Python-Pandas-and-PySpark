from pyspark.sql.session import SparkSession

from pyspark.sql.types import (BooleanType, IntegerType, StringType, 
                               TimestampType, StructType,
                               StructField, ArrayType,
                               TimestampType,FloatType)

import pyspark.sql.functions as F

spark = SparkSession.builder.appName('firstSeesion')\
   .config('spark.master', 'local')\
   .config("spark.executor.memory", "2gb") \
   .config('spark.shuffle.sql.partitions', 2)\
   .getOrCreate() 

schema = StructType([StructField("target", StringType()),
                   StructField("_id", IntegerType()),
                   StructField("date", StringType()),
                   StructField("flag", StringType()),
                   StructField("user", StringType()),
                   StructField("text", StringType()),
                  ])
path = "E:/scripts/training.1600000.processed.noemoticon.csv"

df   = spark.read.format("csv")\
                  .schema(schema)\
                  .load(path)