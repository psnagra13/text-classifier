import pickle
from utils.models.NB import nb
from utils.models.svm import svm
from utils.models.gridsearch import gs
from utils.models.gridsearchsvm import gssvm
from utils.models.RF import rf
from utils.models.DT import dt
import csv
from utils.models.ensemble import ensemble

with open('output/train/processedData/processedAdvancedList.pickle', 'rb') as handle:
     trainData =  pickle.load(handle)
with open('output/test/processedData/processedAdvancedList.pickle', 'rb') as handle:
     testData =  pickle.load(handle)

outputPath='output/models/3/'


# Comment the model you want to skip
# By default all the models will be exceuted
nb(trainData,testData,outputPath)
svm(trainData,testData,outputPath)
rf(trainData,testData,outputPath)
dt(trainData,testData,outputPath)
gssvm(trainData,testData,outputPath)
gs(trainData,testData,outputPath)


csvProbPath = 'output/final.csv'

en = ensemble(outputPath)
en.getFinalProbabilities(csvProbPath)
