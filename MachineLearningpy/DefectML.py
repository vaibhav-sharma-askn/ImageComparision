import os
import pandas as pd
import numpy as np
import seaborn as sns
##%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style

# Algorithms
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import GaussianNB



## Importing the datasets
train = pd.read_csv(os.path.join('..\\MachineLearningpy', 'train.csv'))
test = pd.read_csv(os.path.join('..\\MachineLearningpy', 'test.csv'))

train.info()
train.head()
print(train.describe())
print(train.head(10))

Epic = {"Dashboard": 1, "StopCheque": 2, "MoveMoney":3,"SecureMessaging":3,"LostnStolenCard":4}
user_story = {"male": 0, "female": 1}
user_story_priority = {"male": 0, "female": 1}
Bug_Severity = {"male": 0, "female": 1}
Bug_Priority = {"male": 0, "female": 1}
Environment_Fouund = {"male": 0, "female": 1}

