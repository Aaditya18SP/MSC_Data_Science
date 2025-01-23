from pyspark import SparkConf, SparkContext
import re
conf = SparkConf().setMaster("local").setAppName("prac4")
sc = SparkContext(conf=conf)

data = sc.textFile("./book.txt")


result = data.flatMap(lambda x: re.split(r'[\s]',x)).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y).sortBy(lambda x : x[1], False).take(20)
#for r in result:
print(result)
