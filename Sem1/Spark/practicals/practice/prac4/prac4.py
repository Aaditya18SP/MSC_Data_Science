from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("prac4")
sc = SparkContext(conf=conf)

data = sc.textFile("../../prac4/book.txt")

wordCount = data.flatMap(lambda x: x.split(" ")).map(lambda x:x.strip()).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y).sortBy(lambda x:x[1], ascending=False).take(20)

print(wordCount)

