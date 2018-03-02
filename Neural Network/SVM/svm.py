import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np
import matplotlib.colors as mcol

def plot_svc_decision_function(model, ax):
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # create grid to evaluate model
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    P = model.decision_function(xy).reshape(X.shape)
    
    #plot decision boundary and margins
    ax.contour(X, Y, P, colors='k', levels=[-1, 0, 1], linestyles=['--', '-', '--'])

    #plot support vectors
    ax.scatter(model.support_vectors_[:, 0],
                model.support_vectors_[:, 1],
                s=300, linewidth=1, facecolors='none')

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

cm1 = mcol.LinearSegmentedColormap.from_list("cm1",["r","b"])
data = pd.read_csv('owndata.txt', sep='\t', names=['x', 'y', 'class'])

X = data[data.columns[0:2]].values
y = data[['class']].values

fig1, ax1 = plt.subplots()
ax1.scatter(X[:, 0], X[:, 1], c=y.ravel(), s=50, cmap=cm1)
ax1.set_xlabel('X', fontsize = 20)
ax1.set_ylabel('Y', fontsize = 20)

model = svm.SVC(kernel='linear', C=1.0)
model.fit(X, y)
print(model.support_vectors_)
print('\n\n')

fig2, ax2 = plt.subplots()
ax2.scatter(X[:, 0], X[:, 1], c=y.ravel(), s=50, cmap=cm1)
ax2.set_xlabel('X', fontsize = 20)
ax2.set_ylabel('Y', fontsize = 20)
plot_svc_decision_function(model, ax2)

#Now adding a new data point to dataset
r,c = data.shape
data.loc[r] = [35.567, 45.789, 1.0]

X = data[data.columns[0:2]].values
y = data[['class']].values

fig3, ax3 = plt.subplots()
ax3.scatter(X[:, 0], X[:, 1], c=y.ravel(), s=50, cmap=cm1)
ax3.set_xlabel('X', fontsize = 20)
ax3.set_ylabel('Y', fontsize = 20)

model = svm.SVC(kernel='linear', C=1.0)
model.fit(X, y)
print(model.support_vectors_)
print('\n\n')

fig4, ax4 = plt.subplots()
ax4.scatter(X[:, 0], X[:, 1], c=y.ravel(), s=50, cmap=cm1)
ax4.set_xlabel('X', fontsize = 20)
ax4.set_ylabel('Y', fontsize = 20)
plot_svc_decision_function(model, ax4)

#Now adding a new data point to dataset
r,c = data.shape
data.loc[r] = [1.00, 39.000, 1.0]

X = data[data.columns[0:2]].values
y = data[['class']].values

fig7, ax7 = plt.subplots()
ax7.scatter(X[:, 0], X[:, 1], c=y.ravel(), s=50, cmap=cm1)
ax7.set_xlabel('X', fontsize = 20)
ax7.set_ylabel('Y', fontsize = 20)

model = svm.SVC(kernel='linear', C=1.0)
model.fit(X, y)
print(model.support_vectors_)
print('\n\n')

fig8, ax8 = plt.subplots()
ax8.scatter(X[:, 0], X[:, 1], c=y.ravel(), s=50, cmap=cm1)
ax8.set_xlabel('X', fontsize = 20)
ax8.set_ylabel('Y', fontsize = 20)
plot_svc_decision_function(model, ax8)

#Now adding a new data point to dataset
r,c = data.shape
data.loc[r] = [25.567, 67.789, 0.0]

X = data[data.columns[0:2]].values
y = data[['class']].values

fig5, ax5 = plt.subplots()
ax5.scatter(X[:, 0], X[:, 1], c=y.ravel(), s=50, cmap=cm1)
ax5.set_xlabel('X', fontsize = 20)
ax5.set_ylabel('Y', fontsize = 20)

model = svm.SVC(kernel='linear', C=1.0)
model.fit(X, y)
print(model.support_vectors_)
print('\n\n')

fig6, ax6 = plt.subplots()
ax6.scatter(X[:, 0], X[:, 1], c=y.ravel(), s=50, cmap=cm1)
ax6.set_xlabel('X', fontsize = 20)
ax6.set_ylabel('Y', fontsize = 20)
plot_svc_decision_function(model, ax6)

plt.show()
