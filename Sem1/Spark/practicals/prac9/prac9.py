from pyspark.sql import SparkSession,Column,Row
from pyspark.sql.functions import explode, split,lit,window
import datetime
spark = SparkSession.builder.master("local").appName("prac9").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

lines = spark.readStream.format("socket").option("host","localhost").option("port","9999").option("includeTimestamp","true").load()

words = lines.select(explode(split(lines.value," ")).alias("word"),lines.timestamp)
word_counts = words.groupby(words.word,window(words.timestamp, "1 minute", "5 seconds")).count()
query = word_counts.writeStream.outputMode("complete").format("console").start()

query.awaitTermination()
