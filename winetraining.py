


from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.mllib.tree import RandomForest
from pyspark.mllib.regression import LabeledPoint
from pyspark.ml.feature import VectorAssembler
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.evaluation import MulticlassMetrics
from pyspark.sql.functions import col


conf = (SparkConf().setAppName("TWineApp"))
sc = SparkContext("local", conf=conf)
sc.setLogLevel("ERROR")
SContext = SQLContext(sc)

dataFrame = SContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', sep=';').load('s3://winemodelbucket/TrainingDataset.csv')
validatedataFrame = SContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', sep=';').load('s3://winemodelbucket/ValidationDataset.csv')


Dframe = dataFrame.select(dataFrame.columns[:11])

outputRdd = dataFrame.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[:11])))

model = RandomForest.trainClassifier(outputRdd,numClasses=10,categoricalFeaturesInfo={}, numTrees=60, maxBins=32, maxDepth=4, seed=42)


validOutRdd = validatedataFrame.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[:11])))

predictions = model.predict(validOutRdd.map(lambda x: x.features))
LBandPred = validOutRdd.map(lambda lp: lp.label).zip(predictions)

metrics = MulticlassMetrics(LBandPred)


F1score = metrics.fMeasure()
print("==== Summary Statistics ====")
print("Weighted F(1) Score = %3s" % metrics.weightedFMeasure())

print("Saving model")

model.save(sc, "s3://winemodelbucket/Trainmodel/")

print("Model Saved")