from pyspark.sql import SparkSession, Row

spark = SparkSession.builder.master("local").appName("prac7").getOrCreate()

data = spark.read.csv("../../ml-100k/u.item", sep="|")

data = data.select("_c0","_c1")

movie_dict ={}
for rec in data.collect():
    dic = rec.asDict()
    id = int(dic["_c0"])
    name = dic["_c1"]
    movie_dict[id] = name

broadcast_var = spark.sparkContext.broadcast(movie_dict)


def newRowMaker(row):
    dic = row.asDict()
    #print(dic)
    return Row(user=int(dic["_c0"]), item=int(dic["_c1"]), movie_name=(broadcast_var.value)[int(dic["_c1"])], rating=float(dic["_c2"]), timestamp = dic["_c3"])

data2= spark.read.csv("../../ml-100k/u.data", sep="\t")

data2.show(5)
data2= data2.rdd.map(newRowMaker)

updated_df = spark.createDataFrame(data2)
updated_df.show(10)
