
import sys

from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.mllib.tree import RandomForestModel
from pyspark.mllib.evaluation import MulticlassMetrics
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import Vectors

conf = (SparkConf().setAppName("TWineApp"))
sc = SparkContext("local", conf=conf)
sc.setLogLevel("ERROR")
SContext = SQLContext(sc)

if len(sys.argv) == 2:
    testFile = sys.argv[1]
print("Read Dataset")

model = RandomForestModel.load(sc, "s3://winemodelbucket/Trainmodel/")
print(model)


Dframe = SContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', sep=';').load('s3://winemodelbucket/ValidationDataset.csv')

outputRdd = Dframe.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[:11])))

predictions = model.predict(outputRdd.map(lambda x: x.features))
LBandPred = outputRdd.map(lambda lp: lp.label).zip(predictions)

metrics = MulticlassMetrics(LBandPred)

F1score = metrics.fMeasure()
print("\n\n==== Summary Statatistics ====")
print(" F(1) Score = %s" % metrics.weightedFMeasure())
print("Precision = %s" % metrics.weightedPrecision)