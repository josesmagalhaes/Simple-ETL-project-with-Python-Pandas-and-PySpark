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