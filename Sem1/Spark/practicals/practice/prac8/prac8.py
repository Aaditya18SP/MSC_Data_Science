from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS

spark = SparkSession.builder.master("local").appName("prac8").getOrCreate()

movies_data = spark.read.csv("../../ml-100k/u.item",sep="|")
movies_data=movies_data.select("_c0","_c1").toDF("id","name")
movies_data = movies_data.withColumn("id", movies_data.id.cast("int"))
movies_data.show(10)

data = spark.read.csv("../../ml-100k/u.data",sep="\t")

data = data.toDF("user","item","rating","timestamp")
data =data.withColumns({"user":data.user.cast("int"), "item":data.item.cast("int"), "rating":data.rating.cast("float")})

data.show(10)

model = ALS(userCol="user", itemCol="item", ratingCol="rating").fit(data)

user_df = spark.createDataFrame([{"user":1}])

# 5 recommendations
pred = model.recommendForUserSubset(user_df, 5)

pred.show()

result = pred.collect()[0].asDict()
recommendations = result["recommendations"]

result_df = spark.createDataFrame(recommendations)

result_df=result_df.join(movies_data, result_df.item==movies_data.id).select(result_df.item, movies_data.name, result_df.rating)

result_df.show(5)



