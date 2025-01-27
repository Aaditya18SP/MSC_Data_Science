from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, FloatType

spark = SparkSession.builder.master("local").appName("prac6").getOrCreate()

df= spark.read.csv("/home/aadityapal/Study/MSC_Data_Science/Sem1/Data_visualization/Power_BI/Car_Market_Analysis/car_prices.csv", header=True)

#print(df.columns)
#print(df.dtypes)

#typecast the types of the colums since they are strings
df=df.withColumns({'odometer':df.odometer.cast(IntegerType()), 'sellingprice':df.sellingprice.cast(FloatType())})
print(df.dtypes)

df.groupby(df.make).sum("odometer","sellingprice").show()
df.groupby(df.make).avg("odometer").show()




