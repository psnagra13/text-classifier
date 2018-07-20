import pickle
from utils.models.NB import nb
from utils.models.svm import svm
from utils.models.gridsearch import gs
from utils.models.gridsearchsvm import gssvm
with open('output/train/processedData/processedAdvancedList.pickle', 'rb') as handle:
     trainData =  pickle.load(handle)
with open('output/test/processedData/processedAdvancedList.pickle', 'rb') as handle:
     testData =  pickle.load(handle)

outputPath='output/models/1/'

gssvm(trainData,testData,outputPath)

gs(trainData,testData,outputPath)

nb(trainData,testData,outputPath)

svm(trainData,testData,outputPath)


