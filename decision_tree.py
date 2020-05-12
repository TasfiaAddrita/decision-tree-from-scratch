from binarytree import BinaryTreeNode, BinarySearchTree

class Node:
    def __init__(self):
        self.gini = None
        self.samples = None

class DecisionTreeClassifier:
    def __init__(self, dataset):
        # self.data = dataset

    def _gini_impurity(self, data, feature, label):
        """Determines the probability of classifying a point incorrectly"""
        data[feature].value_counts()

    def _confusion_matrix(self, y_test, y_test):
        pass

    def fit(self, x_train, y_train):
        pass

    def predict(self, x_test):
        pass

    def visualize(self):
        pass

    def evaluate(self):
        pass

    def compare_with_sklearn(self):
        pass

import pandas as pd
import numpy as np
from sklearn import datasets

if __name__ == "__main__":
    
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data)

    df.columns = iris.feature_names
    X = df[df.columns].values # use numpy instead of pandas for speed

    df["species"] = iris.target
    y = df["species"].values
    