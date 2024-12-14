from pyspark.sql import SparkSession
from pyspark.ml.feature import Word2Vec, Tokenizer

spark = SparkSession.builder.appName("EventRecommendation").getOrCreate()
events_df = spark.read.csv("hdfs://path_to_events.csv", header=True)

# Tokenize event descriptions
tokenizer = Tokenizer(inputCol="description", outputCol="words")
words_df = tokenizer.transform(events_df)

# Train Word2Vec model
word2vec = Word2Vec(vectorSize=100, inputCol="words", outputCol="features")
model = word2vec.fit(words_df)
recommendations = model.transform(words_df)
recommendations.show()
