from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("practical3")
sc = SparkContext(conf= conf)

data = sc.textFile("./data.csv")

#print(data.take(5))

#group_by = data.groupBy(lambda x : x.split(",")[0]).filter(lambda x:x[1].split(",")[2]=="TMIN").collect()
min_temps= data.filter(lambda x : "TMIN" in x).map(lambda x : (x.split(",")[0], (float(x.split(",")[3])-32)*(5.0/9.0))).reduceByKey(lambda x,y: min(x,y)).collect()

#first = group_by[0]
#for i in first[1]:
    #print(i)
#print(group_by.take(5))
print("==========================\n MIN TEMP BY STATION ID\n ==========================")
for temp in min_temps:
    print(temp[0] + "\t{:.2f}C".format(temp[1]) )

print()
print("==========================\n MAX TEMP BY STATION ID\n ==========================")
max_temps = data.filter(lambda x : "TMAX" in x).map(lambda x : (x.split(",")[0], (float(x.split(",")[3])-32)*(5.0/9.0))).reduceByKey(lambda x,y : max(x,y)).collect()

for temp in max_temps:
    print(temp[0]+"\t{:.2f}C".format(temp[1]))


