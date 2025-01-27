from pyspark import SparkContext,SparkConf

conf = SparkConf().setMaster("local").setAppName("prac3")
sc = SparkContext(conf=conf)

sc.setLogLevel("ERROR")
data = sc.textFile("../../prac3/data.csv")

min_temp = data.filter(lambda x : "TMIN" in x).map(lambda x: (x.split(",")[0], float(x.split(",")[3]))).reduceByKey(lambda x,y: min(x,y)).collect()
print(min_temp)

max_temp = data.filter(lambda x : "TMAX" in x).map(lambda x: (x.split(",")[0],float(x.split(",")[3]))).reduceByKey(lambda x,y: max(x,y)).collect()

print(max_temp)
