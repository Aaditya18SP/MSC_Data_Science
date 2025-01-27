#from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
#conf = SparkConf().setMaster("local").setAppName("prac8_movie_recommendations")
#sc = SparkContext(conf=conf)

spark = SparkSession.builder.master("local").appName("prac8_movie_recommendations").getOrCreate()

#create a dict of movie id and movie name
#movies_file = sc.textFile("../ml-100k/u.items")
movies_file = spark.read.csv("../ml-100k/u.item", sep="|")

movies_dict = {}
def mapper(row):
    r_dict = row.asDict()
    movie_id = r_dict["_c0"].strip()
    movie_name = r_dict["_c1"].strip()

    movies_dict[movie_id] = movie_name


rec =movies_file.collect()
for r in rec:
    mapper(r)

#print(movies_dict)
print()
train_data = spark.read.csv("../ml-100k/u1.base",sep="\t")
train_data.show(10)

train_data = train_data.toDF("user","item","rating","timestamp")

train_data_df = train_data.withColumns({"user":train_data.user.cast("int"), "item":train_data.item.cast("int"), "rating":train_data.rating.cast("float")})

model = ALS().fit(train_data_df)
user_id = spark.createDataFrame([{"user":1}])

#top 10 recommendations
pred = model.recommendForUserSubset(user_id, 10)
 
pred.show()

for rec in pred.collect():
    r = rec.asDict()
    recommendations = r["recommendations"]
    for recommend in recommendations:
        #print(recommend)
        row = recommend.asDict()
        item_id = row["item"]
        rating = row["rating"]
        print(str(item_id) + "\t"+ movies_dict[str(item_id)]+ "\t"+ str(rating))
        #print(str(recommend)+ " : "+movies_dict[str(recommend)])
