from pyspark.sql import SparkSession,Row

spark = SparkSession.builder.master("local").appName("prac7").getOrCreate()

movies_df = spark.read.csv("../ml-100k/u.item",sep="|")

#movies_df.show(10)

movies_dict = {}
for rec in movies_df.collect():
    dict = rec.asDict()
    movie_id = dict['_c0']
    movie_name = dict['_c1']
    movies_dict[movie_id] = movie_name

#print(movies_dict)
broadcast_var =spark.sparkContext.broadcast(movies_dict)

ratings_df = spark.read.csv("../ml-100k/u.data", sep="\t")
#ratings_df.show(10)

'''
createDfList = []
for rec in ratings_df.collect():
    rec_dict = rec.asDict()
    user_id = rec_dict["_c0"]
    item_id =  rec_dict["_c1"]
    rating =  rec_dict["_c2"]
    timestamp =  rec_dict["_c3"]

    movie_name = broadcast_var.value[item_id]
    row = Row(user_id = user_id, movie_name = movie_name , rating = rating, timestamp = timestamp)
    createDfList.append(row)

updated_df  = spark.createDataFrame(createDfList)

updated_df.show(10)
'''

def newRowMaker(row):
    rec_dict = row.asDict()

    user_id = rec_dict["_c0"]
    item_id =  rec_dict["_c1"]
    rating =  rec_dict["_c2"]
    timestamp =  rec_dict["_c3"]

    movie_name = broadcast_var.value[item_id]
    return Row(user_id = user_id, movie_name = movie_name , rating = rating, timestamp = timestamp)

df_list = ratings_df.rdd.map(newRowMaker)
print(df_list.take(5))

updated_df = spark.createDataFrame(df_list)

updated_df.show(10)
#ratings_df.foreach(lambda row:row._c1 =(broadcast_var.value)[row._c1])


