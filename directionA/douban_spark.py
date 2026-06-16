from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
import time
import pandas as pd

# ======================
# 1. Spark Session
# ======================
spark = SparkSession.builder.appName("A3_PerformanceCompare").getOrCreate()

# ======================
# 2. 读取数据
# ======================
df = spark.read.option("header", True).option("inferSchema", True)\
    .csv("/opt/spark/work-dir/douban_movies.csv")

# ======================
# 3. 打印 A-1 Schema
# ======================
print("\n===== A-1 Schema =====")
df.printSchema()

# ======================
# 4. Pandas 对比
# ======================
start = time.time()
pdf = pd.read_csv("/opt/spark/work-dir/douban_movies.csv")

pandas_result = (
    pdf.groupby("genres")["rating_score"]
       .mean()
       .sort_values(ascending=False)
)

pandas_time = time.time() - start

print("\n===== Pandas 耗时 =====")
print(pandas_time, "秒")

# ======================
# 5. PySpark 对比
# ======================
start = time.time()

spark_result = (
    df.groupBy("genres")
      .agg(avg("rating_score").alias("avg_rating"))
      .orderBy("avg_rating", ascending=False)
)

# 强制触发执行
spark_result.count()

spark_time = time.time() - start

print("\n===== Spark 耗时 =====")
print(spark_time, "秒")

# ======================
# 6. 输出对比结果
# ======================
print("\n===== A-3 RESULT =====")
print("Pandas:", pandas_time, "秒")
print("Spark :", spark_time, "秒")

print("\n===== Pandas Top10 =====")
print(pandas_result.head(10))

print("\n===== Spark Top10 =====")
spark_result.show(10, truncate=False)

spark.stop()