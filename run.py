import training
import testing
import feature_scaling
import numpy as np
import pandas as pd

from sklearn.metrics import accuracy_score

testX = pd.read_csv('./testX.csv', header = None, names = ['speed', 'heading'])
testY = pd.read_csv('./testY.csv', header = None, names = ['ID'])
trainX = pd.read_csv('./trainX.csv', header = None, names = ['speed', 'heading'])
trainY = pd.read_csv('./trainY.csv', header = None, names = ['ID'])

testX = feature_scaling.scale(testX)
trainX = feature_scaling.scale(trainX)


###### Decision Tree Classifier#########

clf = training.dec_tree_train(trainX, trainY)
pred = testing.test(clf, testX)
score = accuracy_score(testY, pred)
print(score)

######### Logistic Regression MultiClass ########

clf = training.logistic_regr(trainX, trainY)
pred = testing.test(clf, testX)
score = accuracy_score(testY, pred)
print('Logistic Regression Score '+ str(score))


