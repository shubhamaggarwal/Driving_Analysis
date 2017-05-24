from sklearn import tree
from sklearn import datasets, linear_model
from sklearn.svm import SVC

import numpy


def dec_tree_train(trainX, trainY):
    clf = tree.DecisionTreeClassifier()
    clf.fit(trainX, trainY)
    return clf

def linear_reg_train(trainX,trainY):
    regr = linear_model.LinearRegression()
    regr.fit(trainX, trainY)
    return regr

def SVC_train(trainX,trainY):
    clf = SVC()
    clf.fit(trainX,trainY)
    return clf

def logistic_regr(trainX, trainY):
    clf = linear_model.LogisticRegression()
    clf.fit(trainX, trainY)
    return clf