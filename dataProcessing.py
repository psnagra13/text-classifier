from utils.dataRead.datareading import load_data
from utils.dataProcess.dataprocessing import data_process
from utils.dataProcess.dataprocessingadvanced import data_process_advanced
import pickle
#################################################################################
#                            PARAMETERS
#################################################################################

train_data_path ='dataset-full/train'
test_data_path ='dataset-full/test'

parameters = {
                'toLower':True,
                'removePunctuations':True,
                'extractEmails': True,
                'extractNamedEntities':True,
                'outputPath':'output/'
}

parameters_advanced = {
                'removeCommonWords':True,
                'removeLowOccurrenceWords': True,
                'minimumNumberOfOccurrenceOfWords':5  # it is the threshold for the word to appear
                                                        # in dataset to be included in feature vector
}



#################################################################################
#                               CODE
#################################################################################

# Read data from files
print ("Reading Files...")
ld_train = load_data(train_data_path)
ld_test = load_data(test_data_path)

# Data PreProcessing
print ("Processing Train Data...")
dp_train = data_process( ld_train,parameters)
print ("Processing Test Data...")
dp_test = data_process(ld_test,parameters)
dp_train.saveData('output/train/')
dp_test.saveData('output/test/')
trainData = dp_train.processedData
testData = dp_test.processedData

# Performing Advanced data analysis
dpa_train = data_process_advanced(trainData,parameters_advanced )
dpa_train.saveData('output/train/')
trainData = dpa_train.processedData

dpa_test = data_process_advanced(testData,parameters_advanced )
dpa_test.saveData('output/test/')
testData = dpa_test.processedData

print ('Finsihed Data Processing')



