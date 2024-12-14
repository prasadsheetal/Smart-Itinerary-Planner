from pyspark.sql import SparkSession
from pyspark.ml.feature import Word2Vec, Tokenizer

# Initialize Spark
spark = SparkSession.builder.appName("EventRecommendation").getOrCreate()

# Load Event Data
events_df = spark.read.csv("hdfs://localhost:9000/events.csv", header=True)

# Preprocess the Text Data
tokenizer = Tokenizer(inputCol="description", outputCol="words")
words_df = tokenizer.transform(events_df)

# Build Word2Vec Model
word2vec = Word2Vec(vectorSize=100, inputCol="words", outputCol="features")
model = word2vec.fit(words_df)

# Transform Data
recommendations = model.transform(words_df)
recommendations.show(truncate=False)
