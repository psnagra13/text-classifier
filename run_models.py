import pickle
from utils.models.NB import nb
from utils.models.svm import svm
from utils.models.gridsearch import gs
from utils.models.gridsearchsvm import gssvm
from utils.models.RF import rf
from utils.models.DT import dt
import csv

with open('output/train/processedData/processedAdvancedList.pickle', 'rb') as handle:
     trainData =  pickle.load(handle)
with open('output/test/processedData/processedAdvancedList.pickle', 'rb') as handle:
     testData =  pickle.load(handle)

outputPath='output/models/3/'

# gssvm(trainData,testData,outputPath)
# #
# gs(trainData,testData,outputPath)
#
# nb(trainData,testData,outputPath)
#
# svm(trainData,testData,outputPath)
# rf(trainData,testData,outputPath)
# dt(trainData,testData,outputPath)

header=[]

def read(path):
    header=[]
    dic ={}
    with open('output/models/3/' +path+'-probability.csv', mode='r') as infile:
        reader = csv.reader(infile)
        li = list(reader)

    for cat in range (1,21):
        header.append(li[0][cat])
    print (header)
    print(len(header))
    print(len(li))

    for i in range (1,len(li)):
        row=li[i]
        dic[row[0]] = {}

        for j in range (1,21):
            dic[row[0]][header[j-1]]= float(row[j])

    return dic

tot={}

gssvm = read('gssvm')
gs =read('gs')
nb = read('nb')
svm =read('svm')
rf =read('rf')
# dt =read('dt')


header = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']

import operator

for key in nb:
    tot[key]={}
    for cat in header:
        tot[key][cat] = gs[key][cat]  +   svm[key][cat]    +   nb[key][cat]    +   gssvm[key][cat] +   rf[key][cat ] #+   dt[key][cat]

pred={}
pred2={}
for key in tot:
    x = tot[key]
    sorted_x = sorted(x.items(), key=operator.itemgetter(1),reverse=True)
    pred[key]= (sorted_x[0][0])
    pred2[key]= (sorted_x[1][0])


truth={}

with open('output/models/3/gs.csv', mode='r') as infile:
        reader = csv.reader(infile)
        li = list(reader)
for l in li:
    truth[l[0]]= l[1]

print(truth)
i=0
for key in truth:
 print (truth[key] + ' ' + pred[key])
 if truth[key]== pred[key] :
 # if truth[key]== pred[key] or truth[key]== pred2[key]:
     i+=1

print (i)
print (i/len(truth))

with open( 'final.pickle', 'wb') as handle:
        pickle.dump(tot,handle)
