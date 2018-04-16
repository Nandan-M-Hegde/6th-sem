import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.colors as mcol
from sklearn import svm, datasets
from sklearn.metrics import accuracy_score
import numpy as np

def visualize_data(X, Y, ax, xlabel, ylabel, title):
    for a,b in zip(X, Y):
        if b==0:
            ax.scatter(a[0], a[1], marker='+', color='red', s=25, edgecolors='k')
        elif b==1:
            ax.scatter(a[0], a[1], marker='o', color='green', s=25, edgecolors='k')
        elif b==2:
            ax.scatter(a[0], a[1], marker='^', color='blue', s=25, edgecolors='k')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

#load dataset into pandas dataframe
iris = datasets.load_iris()

#Seperating features
features = iris.data

#seperating target
target = iris.target

#Function to plot the data w.r.t to sepal length and sepal width
fig1, ax1 = plt.subplots()
visualize_data(features[:, 0:2], target, ax1, 'Sepal Length', 'Sepal Width', "Sepal Length vs Width")

#Function to plot the data w.r.t to petal length and petal width
fig2, ax2 = plt.subplots()
visualize_data(features[:, 2:4], target, ax2, 'Petal Length', 'Petal width', 'Petal length vs Petal width')

#standardizing features
features = StandardScaler().fit_transform(features)

#Creating pca object
pca = PCA(n_components=2)

#Performing pca on features
principal_components = pca.fit_transform(features)

df = pd.DataFrame(data=principal_components, columns=['pc1', 'pc2'])

features = df[df.columns].values
fig3, ax3 = plt.subplots()
visualize_data(features, target, ax3, 'PCA1', 'PCA2', 'Principal components of IRIS')

plt.show()