
import pickle
import string
import nltk
import re
import csv

class data_process_advanced:

  def __init__(self, data,parameters):

    # classes = self.dataObject.classes
    # filesPath = self.dataObject.list_of_filepaths_in_each_class
    # filecontents = self.dataObject.data
    self.data=data

    self.processedData = {}
    self.classes=[]
    self.chi_square_dic ={}
    #
    # if parameters['removeLowDistinctiveWords'] ==True:
    #         self.calculateChiSqare(data)

    self.processedDataList = []

    for id in data:
        tokens = data[id]['tokenizedData']
        tokens.extend(data[id]['namedEntities'])
        tokens.extend(data[id]['email'])
        category = data[id]['category']
        self.processedData[id] = {'category':category , 'data' :" ".join(tokens)}


    self.vocabulary={}
    self.vocabulary_categorywise ={}
    self.vocabCountGenerator()

    if parameters['removeLowOccurrenceWords'] ==True:
        self.removeLowOccurrenceWords(parameters['minimumNumberOfOccurrenceOfWords'])

    if parameters['removeCommonWords'] ==True:
        self.removeCommonWords()

    for id in self.processedData:
        self.processedDataList.append([id,self.processedData[id]['category'],self.processedData[id]['data']])





  def vocabCountGenerator(self):

      classesTemp  = {}
      for id in self.data:
          classesTemp[self.data[id]['category']]=1

      self.classes =classesTemp.keys()

      for id in self.processedData:
          tokens = (self.processedData[id]['data']).split(' ')
          category = self.processedData[id]['category']

          for token in tokens:
            if token in self.vocabulary_categorywise:
                self.vocabulary_categorywise[token][category]+=1
                self.vocabulary[token] += 1
            else:
                self.vocabulary_categorywise[token] = {}
                self.vocabulary[token] = {}
                for c in self.classes:
                    self.vocabulary_categorywise[token][c]=0

                self.vocabulary_categorywise[token][category]=1
                self.vocabulary[token] = 1

      print (len(self.vocabulary))
      print (len(self.vocabulary_categorywise))
      return

  def removeLowOccurrenceWords(self,minimum):

      for id in self.processedData:
          tokens = (self.processedData[id]['data']).split(' ')
          token_new=[]

          for token in tokens:
              if self.vocabulary[token]>=minimum:
                  token_new.append(token)

          self.processedData[id]['data'] =" ".join(token_new)


      self.count_vocab()
      return


  def removeCommonWords(self):

      vocabulary_categorywise = self.vocabulary_categorywise
      vocabulary = self.vocabulary
      chi_square_dic = {}
      max = 10000

      for key in vocabulary_categorywise:
        total = vocabulary[key]
        freq_dic = vocabulary_categorywise[key]
        chi_square_dic[key ]={}
        cal_total_ch_value = 0

        for c in  freq_dic:
            cat_count = freq_dic[c]
            nor_cat_count = cat_count/total *max

            expected_count = max/20

            chisquare =( nor_cat_count - expected_count)*( nor_cat_count - expected_count)/(expected_count+1)
            chi_square_dic[key][c]=chisquare
            cal_total_ch_value += chisquare
        chi_square_dic[key]['total']=cal_total_ch_value



      for key in chi_square_dic:
          if chi_square_dic[key]['total']<10000:
              self.chi_square_dic[key]=chi_square_dic[key]

      for id in self.processedData:
          tokens = (self.processedData[id]['data']).split(' ')
          token_new=[]

          for token in tokens:
              if chi_square_dic[token]['total'] >10000:
                  token_new.append(token)

          self.processedData[id]['data'] =" ".join(token_new)


      self.count_vocab()

  def count_vocab(self):
      vocabulary={}

      for id in self.processedData:
          tokens = (self.processedData[id]['data']).split(' ')

          for token in tokens:
            if token in vocabulary:
                vocabulary[token] += 1
            else:
                vocabulary[token] = 1

      print (len(vocabulary))









  def saveData(self,path):

      with open(path+ 'processedData/processedAdvanced.pickle', 'wb') as handle:
        pickle.dump(self.processedData,handle)

      with open(path+ 'processedData/processedAdvancedList.pickle', 'wb') as handle:
        pickle.dump(self.processedDataList,handle)

      with open(path+ 'chi_square_dic.pickle', 'wb') as handle:
            pickle.dump(self.chi_square_dic,handle)

      with open(path+ "chi_square_dic.csv",'w') as resultFile:
          wr = csv.writer(resultFile, dialect='excel')

          for key in self.chi_square_dic:
                row=[key,self.chi_square_dic[key]['total']]

                for c in self.classes:
                    row.append(self.chi_square_dic[key][c])

                wr.writerow(row)




if __name__ == "__main__":
    a=1



