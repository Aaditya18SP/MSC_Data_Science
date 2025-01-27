# Spark context
spark context is the low-level way of accessing low-level RDDs. The RDDs should not be directly used as suggested but rather be used through DataFrames.

# Reading data from a file

## 1. using spark context to load data into RDD
```python
sparkcontext.textFile("path")
```

## 2. load data into a dataframe
```python
#general
sparksession.read.load("path",format="csv")
#from csv
sparksession.read.csv("path")
```

# Writing data to a file
## 1. using the spark context
```python
#TODO
```
## 2. using the spark session
```python
#dataframe.write returns a DataFrameWriter
dataframe.write.csv()
```

# Creating Spark Context
```python
from pyspark import SparkContext, SparkConf
conf = SparkConf().setMaster("local").setAppName("name")
sc = SparkContext(conf=conf)
```

# Creating Spark Session
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local").appName("name").getOrCreate()
```
