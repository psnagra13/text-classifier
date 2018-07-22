import pickle
from utils.models.NB import nb
from utils.models.svm import svm
from utils.models.gridsearch import gs
from utils.models.gridsearchsvm import gssvm
from utils.models.RF import rf
from utils.models.DT import dt
from utils.models.KNN import knn
from utils.models.svc import svc

import csv
with open('output/train/processedData/processedAdvancedList.pickle', 'rb') as handle:
     trainData =  pickle.load(handle)
with open('output/test/processedData/processedAdvancedList.pickle', 'rb') as handle:
     testData =  pickle.load(handle)

outputPath='output/models/3/'



'''Uncomment the Line when you want to execute the model'''

# gssvm(trainData,testData,outputPath)
# gs(trainData,testData,outputPath)
nb(trainData,testData,outputPath)
# svm(trainData,testData,outputPath)
# rf(trainData,testData,outputPath)
# dt(trainData,testData,outputPath)
# knn(trainData,testData,outputPath)
# svc(trainData,testData,outputPath)
