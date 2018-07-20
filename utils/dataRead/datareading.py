import os
from os import listdir
from os.path import isfile, join
import pickle
import string


class load_data:

  def __init__(self, path):
    self.datapath = path
    self.classes = self.getClasses()
    print ('---------------------------------------------------------------- ')
    print ('---------------------------------------------------------------- ')
    print ('Number of Classes in ' + path+ ' = ' + str(len(self.classes)))
    print ('Class List')
    print (self.classes)
    print ('---------------------------------------------------------------- ')
    self.list_of_filepaths_in_each_class = self.getListOfFilesInEachClass()
    print ('Number of documents in each class = ')
    for c in self.classes:
        print (c + ' = ' + str(len(self.list_of_filepaths_in_each_class[c])))
    print ('---------------------------------------------------------------- ')

    self.data =self.readDataFromFiles()

    print ('Number of files in ' + self.datapath +' = ' + str(len(self.data)))





  def getClasses(self):
      subfolders = [dI for dI in os.listdir(self.datapath) if os.path.isdir(os.path.join(self.datapath,dI))]
      return subfolders

  def getListOfFilesInEachClass(self):

      list_of_filepaths_in_each_class = {} # {cat1:{}, cat2:{}}

      for c in self.classes:
          c_path = join(self.datapath, c)
          list_of_filespath_in_c = [join(c_path, f) for f in listdir(c_path) if isfile(join(c_path, f))]
          list_of_filepaths_in_each_class[c]= list_of_filespath_in_c

      return list_of_filepaths_in_each_class

  def readDataFromFiles(self):
    files_data ={}
    for c in self.classes:
        files_list = self.list_of_filepaths_in_each_class[c]
        for file_path in files_list:
            file_content = open(file_path, encoding='ISO-8859-1').read()
            files_data[file_path] ={'content':file_content ,'category':c}
    return files_data




if __name__ == "__main__":
    ld= load_data('../../dataset/train')
