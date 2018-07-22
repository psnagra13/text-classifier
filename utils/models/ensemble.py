import csv
import pickle



class ensemble:

  def __init__(self, inputPath):

        self.header=[]
        self.inputPath =inputPath

        total={}

        #Loading individual Probabilities
        gssvm = self.readIndividualProbablities('gssvm')
        gs =self.readIndividualProbablities('gs')
        nb = self.readIndividualProbablities('nb')
        svm =self.readIndividualProbablities('svm')
        rf =self.readIndividualProbablities('rf')

        self.header = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']

        for key in nb:
            total[key]={}
            for cat in self.header:
                total[key][cat] = gs[key][cat]+gssvm[key][cat] + rf[key][cat ] + nb[key][cat]  + svm[key][cat]

        predictions={}
        import operator
        for key in total:
            x = total[key]
            sorted_x = sorted(x.items(), key= operator.itemgetter(1),reverse=True)
            predictions[key]= (sorted_x[0][0])

        truth={}

        with open(self.inputPath+'gs.csv', mode='r') as infile:
                reader = csv.reader(infile)
                li = list(reader)
        for l in li:
            truth[l[0]]= l[1]

        true_predictions=0
        for key in truth:
         if truth[key]== predictions[key] :
             true_predictions+=1

        print ('Final Accuracy using all Models = ' +str(true_predictions/len(truth)))
        self.total=total


  def readIndividualProbablities(self,path):
            header=[]
            dic ={}
            with open('output/models/3/' +path+'-probability.csv', mode='r') as infile:
                reader = csv.reader(infile)
                li = list(reader)

            for cat in range (1,21):
                header.append(li[0][cat])

            for i in range (1,len(li)):
                row=li[i]
                dic[row[0]] = {}

                for j in range (1,21):
                    dic[row[0]][header[j-1]]= float(row[j])

            return dic

  def getFinalProbabilities(self,finalCsvPath):

      FinalProb ={}
      for key in self.total:
          id = key.split('/')[3]
          pr = self.total[key]

          temp=0
          for cat in self.header:
              temp +=pr[cat]

          tempDic={}
          for cat in self.header:
              tempDic[cat] =    pr[cat]/temp

          FinalProb[id]=tempDic


      with open(finalCsvPath, 'wt') as csv_file:

                writer = csv.writer(csv_file)

                header = ['document_id']
                for c in self.header:
                    header.append(c)
                writer.writerow(header)

                for i in FinalProb:
                    row=[i]
                    temp_dic = FinalProb[i]
                    for c in self.header:
                        row.append(temp_dic[c])
                    writer.writerow(row)















