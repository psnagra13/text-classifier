import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import csv
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import SGDClassifier



class gssvm:

  def __init__(self, trainData,testData,path):

      train = pd.DataFrame.from_records(trainData)
      test = pd.DataFrame.from_records(testData)
      numpy_array = train.as_matrix()
      X_train = numpy_array[:,2]
      Y_train = numpy_array[:,1]
      docid_train=numpy_array[:,0]

      text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf-svm', SGDClassifier(loss='modified_huber', penalty='l2', alpha=1e-3, n_iter=5, random_state=0)),])

      text_clf = text_clf.fit(X_train,Y_train)



      parameters_svm = {'vect__ngram_range': [(1, 1), (1, 2)],
               'tfidf__use_idf': (True, False),
               'clf-svm__alpha': (1e-2, 1e-3),
                     }

      gs_clf = GridSearchCV(text_clf, parameters_svm, n_jobs=-1)
      gs_clf = gs_clf.fit(X_train, Y_train)

      numpy_array = test.as_matrix()
      X_eval = numpy_array[:,2]
      Y_eval = numpy_array[:,1]
      docid_eval=numpy_array[:,0]

      predicted_eval = gs_clf.predict(X_eval)
      print (np.mean(predicted_eval == Y_eval))
      print(predicted_eval)


      with open(path +'gssvm.csv', 'wt') as csv_file:

                writer = csv.writer(csv_file)
                header = ['id','category', 'predicted']
                for i in range(0, len(X_eval)):
                    row =[docid_eval[i] , Y_eval[i], predicted_eval[i]]
                    writer.writerow(row)



      classes = gs_clf.classes_
      predicted_prob = gs_clf.predict_proba(X_eval)

      with open(path +'gssvm-probability.csv', 'wt') as csv_file:

                writer = csv.writer(csv_file)
                header = ['id']
                for c in classes:
                    header.append(c)
                writer.writerow(header)

                for i in range(0, len(predicted_prob)):
                    row =[docid_eval[i] ]
                    for x in predicted_prob[i]:
                        row.append(x)
                    writer.writerow(row)



