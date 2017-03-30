import training
import testing
import feature_scaling
import numpy as np

from sklearn.metrics import accuracy_score

testX = np.genfromtxt('./testX.csv', delimiter=',', dtype=float)
testY = np.genfromtxt('./testY.csv', delimiter=',', dtype=str)
trainX = np.genfromtxt('./trainX.csv', delimiter=',', dtype=float)
trainY = np.genfromtxt('./trainY.csv', delimiter=',', dtype=str)

testX = feature_scaling.scale(testX)
trainX = feature_scaling.scale(trainX)

###### Decision Tree Classifier#########

clf = training.dec_tree_train(trainX, trainY)
pred = testing.test(clf, testX)
score = accuracy_score(testY, pred)
print(score)

###############################
regr = training.SVC_train(trainX, trainY)
pred = testing.test(regr, testX)
score = accuracy_score(testY, pred)
print(score)


