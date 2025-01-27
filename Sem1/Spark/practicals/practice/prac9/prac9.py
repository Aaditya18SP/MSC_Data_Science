from pyspark.sql import SparkSession
from pyspark.sql.functions import explode,split,window

spark = SparkSession.builder.master("local").appName("window_streaming").getOrCreate()

lines = spark.readStream.format("socket").option("host","localhost").option("port","8999").option("includeTimestamp","true").load()

words = lines.select(explode(split(lines.value," ")).alias("word"), lines.timestamp)

wordCount = words.groupBy(window(words.timestamp,"1 minute","10 seconds"),words.word).count()

query = wordCount.writeStream.format("console").outputMode("complete").start()

query.awaitTermination()
