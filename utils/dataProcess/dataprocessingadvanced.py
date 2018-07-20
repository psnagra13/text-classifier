
import pickle
import string
import nltk
import re

class data_process_advanced:

  def __init__(self, data,parameters):

    # classes = self.dataObject.classes
    # filesPath = self.dataObject.list_of_filepaths_in_each_class
    # filecontents = self.dataObject.data
    self.data=data

    self.vocabulary={}
    self.vocabulary_categorywise ={}
    self.vocabCountGenerator()

    self.processedData = {}
    #
    # if parameters['removeLowDistinctiveWords'] ==True:
    #         self.calculateChiSqare(data)

    self.processedDataList = []

    for id in data:
        tokens = data[id]['tokenizedData']
        tokens.extend(data[id]['namedEntities'])
        tokens.extend(data[id]['email'])

        category = data[id]['category']

        # if parameters['removeLowDistinctiveWords'] ==True:
        #     self.calculateChiSqare()

        self.processedData[id] = {'category':category , 'data' :" ".join(tokens)}


    for id in self.processedData:
        self.processedDataList.append([id,self.processedData[id]['category'],self.processedData[id]['data']])



  def vocabCountGenerator(self):
      return






  def saveData(self,path):

      with open(path+ 'processedData/processedAdvanced.pickle', 'wb') as handle:
        pickle.dump(self.processedData,handle)

      with open(path+ 'processedData/processedAdvancedList.pickle', 'wb') as handle:
        pickle.dump(self.processedDataList,handle)




if __name__ == "__main__":
    a=1



