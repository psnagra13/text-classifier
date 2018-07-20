
import pickle
import string
import nltk
import re

class data_process:

  def __init__(self, dataObject,parameters):

    # classes = self.dataObject.classes
    # filesPath = self.dataObject.list_of_filepaths_in_each_class
    # filecontents = self.dataObject.data


    self.processedData ={}


    i=0

    for file in dataObject.data:
        i=i+1
        if(i%100 ==0):
            print (str(i) + '  files processed..')


        fileContents = dataObject.data[file]['content']
        category = dataObject.data[file]['category']

        self.processedData[file] ={ 'rawData' : fileContents , 'category' : category}

        if parameters['extractNamedEntities']== True:
            self.processedData[file]['namedEntities'] = self.nerUtil(fileContents)

        if parameters['toLower'] ==True:
            fileContents = self.lowerCaseUtil(fileContents)

        if parameters['extractEmails']== True:
            self.processedData[file]['email'] = self.extractEmailUtil(fileContents)

        if parameters['removePunctuations'] ==True:
            fileContents = self.removePunctuationsUtil(fileContents)

        # Tokenize the data
        tokenList = self.tokenizeUtil(fileContents)

        self.processedData[file]['tokenizedData']=tokenList


  def removePunctuationsUtil(self,text):
      return text.translate(str.maketrans('','',string.punctuation))


  def tokenizeUtil(self,text):
      return nltk.word_tokenize(text)


  def lowerCaseUtil(self,text):
      return text.lower()

  def extractEmailUtil(self,text):
        lines = text.lower().splitlines()
        email = ''
        for line in lines :
            if line.startswith('from:') or line.startswith('re:') :
                match = re.search(r'[\w\.\+-]+@[\w\.-]+', email)
                if(match):
                    email = match.group(0)
                    return email
                else:
                    return email

        return email

  def nerUtil(self,text):

      parse_tree = nltk.ne_chunk(nltk.tag.pos_tag(text.split()), binary=True)  # POS tagging before chunking!

      named_entities = []

      for t in parse_tree.subtrees():
            if t.label() == 'NE':
                #named_entities.append(t)
                # named_entities.append(list(t))  # if you want to save a list of tagged words instead of a tree
                for n in list(t):
                    named_entities.append((n[0].lower()))

      return named_entities


  def saveData(self,path):

      with open(path+ 'processedData/processed.pickle', 'wb') as handle:
        pickle.dump(self.processedData,handle)


if __name__ == "__main__":
    a=1



