from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("prac5").getOrCreate()

data = spark.read.csv("../../prac5/fakefriends.csv")

data=data.toDF("no","name","age","no_of_friends")

data =data.withColumns({"age":data.age.cast("int"), "no_of_friends": data.no_of_friends.cast("int")})
total_by_age = data.groupBy("age").count()
total_by_age.show()

data.createOrReplaceTempView("user")
users_sql = spark.sql("SELECT * FROM user Where age >13 AND age <65")
users_sql.show(10)

print(data.dtypes)
sql2 = data.select("name","age").where((data.age > 12) & (data.age < 20))
sql2.show()
