from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("prac6").getOrCreate()

data = spark.read.csv("../../prac6/customer-orders.csv")

data.show(10)

data = data.toDF("cust_no","prod_id","price")
data = data.withColumns({"cust_no":data.cust_no.cast("int"), "prod_id": data.prod_id.cast("int"), "price": data.price.cast("float")})
total_spent_by_cust = data.groupBy("cust_no").sum("price")

total_spent_by_cust.show()
