#from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession,Row

#conf = SparkConf().setMaster("local").setAppName("prac5")
#sc = SparkContext(conf=conf)


spark = SparkSession.builder.appName("prac5").master("local").getOrCreate()

df = spark.createDataFrame([
    Row(name="ABC",age=18, bg="AB+"),
    Row(name="DEF",age=19, bg="A+"),
    Row(name="GHI",age=20, bg="B+"),
    Row(name="JKL",age=21, bg="O+"),
    Row(name="MNO",age=22, bg="A+")
    ])

df.show()

query = spark.sql("SELECT * FROM {df} where age>20", df=df)
query.show()


print()
print("Using df.select method which works like the one in sql")


df.select("name").filter(df.age >20).show()
df.select(df.name).filter(df.age >20).show()

print()
print("===group by===")
df.groupby("bg").count().show()


print()
print("===sorting==")
df.groupby("bg").count().sort("count", ascending=False).show()
