from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.colors as mcol
from sklearn.metrics import accuracy_score
from sklearn import svm

class KNN:
    def __init__(self, X, Xt, Y, Yt, cm1):
        self.X, self.Xt, self.Y, self.Yt, self.cm1 = X, Xt, Y, Yt, cm1

    def classify(self, n):
        self.knn1 = KNeighborsClassifier(n_neighbors=n).fit(self.X[:, :2], self.Y)
        self.knn2 = KNeighborsClassifier(n_neighbors=n).fit(self.X[:, 2:4], self.Y)
        self.knn = KNeighborsClassifier(n_neighbors=n).fit(self.X, self.Y)

    def accuracy(self, i):
        print("\nKNN with ", i," neighbours ")
        y1 = self.knn1.predict(self.Xt[:, :2])
        y2 = self.knn2.predict(self.Xt[:, 2:4])
        y = self.knn.predict(self.Xt)
        print("Accuracy with respect to sepal length and width = ",accuracy_score(self.Yt, y1, normalize=True))
        print("Accuracy with respect to petal length and width = ",accuracy_score(self.Yt, y2, normalize=True))
        print("Accuracy with respect to all features = ",accuracy_score(self.Yt, y, normalize=True))
        return accuracy_score(self.Yt, y1, normalize=True), accuracy_score(self.Yt, y2, normalize=True), accuracy_score(self.Yt, y, normalize=True)

    def plot_data(self, ax, X, xlabel, ylabel, title):
        for a,b in zip(X, self.Y):
            if b==0:
                ax.scatter(a[0], a[1], marker='+', color='red', s=25, edgecolors='k')
            elif b==1:
                ax.scatter(a[0], a[1], marker='o', color='green', s=25, edgecolors='k')
            elif b==2:
                ax.scatter(a[0], a[1], marker='^', color='blue', s=25, edgecolors='k')
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)

    def plot_contours(self, mdl, ax, X0, X1, h = 0.2):
        xmin, xmax = X0.min()-1, X0.max()+1
        ymin, ymax = X1.min()-1, X1.max()+1
        xx, yy = np.meshgrid(np.arange(xmin, xmax, h), np.arange(ymin, ymax, h))

        Z = mdl.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, colors=['cyan', 'yellow', 'grey', 'green'], levels=[-1, 0, 1, 2], linestyles=['-', '-', '-', '-'])

class SVM:
    def __init__(self, X, Xt, Y, Yt, cm1):
        self.X, self.Xt, self.Y, self.Yt, self.cm1 = X, Xt, Y, Yt, cm1

    def classify(self):
        print("\nSVM")
        self.Lmodel1 = svm.SVC(kernel='linear', C=1).fit(self.X[: , :2], self.Y)
        self.Lmodel2 = svm.SVC(kernel='linear', C=1).fit(self.X[:, 2:4], self.Y)
        self.Lmodel = svm.SVC(kernel='linear', C=1).fit(self.X, self.Y)

        self.rbfmodel1 = svm.SVC(kernel='rbf', C=1).fit(self.X[: , :2], self.Y)
        self.rbfmodel2 = svm.SVC(kernel='rbf', C=1).fit(self.X[:, 2:4], self.Y)
        self.rbfmodel = svm.SVC(kernel='rbf', C=1).fit(self.X, self.Y)

        self.polymodel1 = svm.SVC(kernel='poly', C=1).fit(self.X[: , :2], self.Y)
        self.polymodel2 = svm.SVC(kernel='poly', C=1).fit(self.X[:, 2:4], self.Y)
        self.polymodel = svm.SVC(kernel='poly', C=1).fit(self.X, self.Y)
    
    def accuracy(self):
        y1 = self.Lmodel1.predict(self.Xt[:, :2])
        y2 = self.Lmodel2.predict(self.Xt[:, 2:4])
        y = self.Lmodel.predict(self.Xt)
        print("\nLinear model")
        print("Accuracy with respect to sepal length and width = ",accuracy_score(self.Yt, y1, normalize=True))
        print("Accuracy with respect to petal length and width = ",accuracy_score(self.Yt, y2, normalize=True))
        print("Accuracy with respect to all features = ",accuracy_score(self.Yt, y, normalize=True))

        y1 = self.rbfmodel1.predict(self.Xt[:, :2])
        y2 = self.rbfmodel2.predict(self.Xt[:, 2:4])
        y = self.rbfmodel.predict(self.Xt)
        print('\nRBF model')
        print("Accuracy with respect to sepal length and width = ",accuracy_score(self.Yt, y1, normalize=True))
        print("Accuracy with respect to petal length and width = ",accuracy_score(self.Yt, y2, normalize=True))
        print("Accuracy with respect to all features = ",accuracy_score(self.Yt, y, normalize=True))

        y1 = self.polymodel1.predict(self.Xt[:, :2])
        y2 = self.polymodel2.predict(self.Xt[:, 2:4])
        y = self.polymodel.predict(self.Xt)
        print('\nPolynomial model')
        print("Accuracy with respect to sepal length and width = ",accuracy_score(self.Yt, y1, normalize=True))
        print("Accuracy with respect to petal length and width = ",accuracy_score(self.Yt, y2, normalize=True))
        print("Accuracy with respect to all features = ",accuracy_score(self.Yt, y, normalize=True))
    
    def plot_data(self, ax, X, xlabel, ylabel, title):
        for a,b in zip(X, self.Y):
            if b==0:
                ax.scatter(a[0], a[1], marker='+', color='red', s=25, edgecolors='k')
            elif b==1:
                ax.scatter(a[0], a[1], marker='o', color='green', s=25, edgecolors='k')
            elif b==2:
                ax.scatter(a[0], a[1], marker='^', color='blue', s=25, edgecolors='k')
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)

    def plot_contours(self, mdl, ax, X0, X1, h = 0.2):
        xmin, xmax = X0.min()-1, X0.max()+1
        ymin, ymax = X1.min()-1, X1.max()+1
        xx, yy = np.meshgrid(np.arange(xmin, xmax, h), np.arange(ymin, ymax, h))

        Z = mdl.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, colors=['cyan', 'yellow', 'grey', 'green'], levels=[-1, 0, 1, 2], linestyles=['-', '-', '-', '-'])

iris = load_iris()
X = iris.data
Y = iris.target
Xt = np.vstack((X[25:35], X[75:85], X[125:135]))
Yt = np.hstack((Y[25:35], Y[75:85], Y[125:135]))
X = np.vstack((X[0:25], X[35:75], X[85:125], X[135:150]))
Y = np.hstack((Y[0:25], Y[35:75], Y[85:125], Y[135:150]))
#X, Xt, Y, Yt = train_test_split(X, Y, test_size=0.2)
cm1 = mcol.LinearSegmentedColormap.from_list("cm1",["cyan", "yellow", "grey"])

k = KNN(X, Xt, Y, Yt, cm1)
s = SVM(X, Xt, Y, Yt, cm1)

n= []
accuracies_sepal = []
accuracies_petal = []
accuracies = []
for i in range(1, 15):
    n.append(i)
    k.classify(i)
    a1, a2, a = k.accuracy(i)

    accuracies.append(a)
    accuracies_petal.append(a2)
    accuracies_sepal.append(a1)

    fig0, ax0 = plt.subplots()
    k.plot_contours(k.knn1, ax0, X[:, 0], X[:, 1])
    k.plot_data(ax0, X[:, :2], "Sepal Length", "Sepal Width", ("KNN with n_neighbours = "+str(i)))

    fign, axn = plt.subplots()
    k.plot_contours(k.knn2, axn, X[:, 2], X[:, 3])
    k.plot_data(axn, X[:, 2:4], "Petal Length", "Petal Width", ("KNN with n_neighbours = "+str(i)))

plt.show()

fig01, ax01 = plt.subplots()
ax01.plot(n, accuracies_sepal)
ax01.set_xlabel("Number of neighbours")
ax01.set_ylabel("Accuracy")
ax01.set_title("KNN for sepal length and width")

fig02, ax02 = plt.subplots()
ax02.plot(n, accuracies_petal)
ax02.set_xlabel("Number of neighbours")
ax02.set_ylabel("Accuracy")
ax02.set_title("KNN for petal length and width")

fig03, ax03 = plt.subplots()
ax03.plot(n, accuracies)
ax03.set_xlabel("Number of neighbours")
ax03.set_ylabel("Accuracy")
ax03.set_title("KNN for all features")
plt.show()

s.classify()
s.accuracy()

# fig1, ax1 = plt.subplots()
# s.plot_contours(s.Lmodel1, ax1, X[:, 0], X[:, 1])
# s.plot_data(ax1, X[:, :2],  "Sepal Length", "Sepal Width", "SVM\nLinear kernel")

# fig2, ax2 = plt.subplots()
# s.plot_contours(s.Lmodel2, ax2, X[:, 2], X[:, 3])
# s.plot_data(ax2, X[:, 2:4], "Petal Length", "Petal Width", "SVM\nLinear kernel")
# plt.show()

# fig3, ax3 = plt.subplots()
# s.plot_contours(s.rbfmodel1, ax3, X[:, 0], X[:, 1])
# s.plot_data(ax3, X[:, :2], "Sepal Length", "Sepal Width", "SVM\nRBF kernel")

# fig4, ax4 = plt.subplots()
# s.plot_contours(s.rbfmodel2, ax4, X[:, 2], X[:, 3])
# s.plot_data(ax4, X[:, 2:4], "Petal Length", "Petal Width", "SVM\nRBF kernel")
# plt.show()

# fig5, ax5 = plt.subplots()
# s.plot_contours(s.polymodel1, ax5, X[:, 0], X[:, 1])
# s.plot_data(ax5, X[:, :2], "Sepal Length", "Sepal Width", "SVM\nPolynomial kernel")

# fig6, ax6 = plt.subplots()
# s.plot_contours(s.polymodel2, ax6, X[:, 2], X[:, 3])
# s.plot_data(ax6, X[:, 2:4], "Petal Length", "Petal Width", "SVM\nPolynomial kernel")
# plt.show()

fig, ax = plt.subplots(2, 3)
s.plot_contours(s.Lmodel1, ax[0][0], X[:, 0], X[:, 1])
s.plot_data(ax[0][0], X[:, :2],  "Sepal Length", "Sepal Width", "Linear kernel")

#fig2, ax2 = plt.subplots()
s.plot_contours(s.Lmodel2, ax[1][0], X[:, 2], X[:, 3])
s.plot_data(ax[1][0], X[:, 2:4], "Petal Length", "Petal Width", " ")
#plt.show()

#fig3, ax3 = plt.subplots()
s.plot_contours(s.rbfmodel1, ax[0][1], X[:, 0], X[:, 1])
s.plot_data(ax[0][1], X[:, :2], "Sepal Length", "Sepal Width", "RBF kernel")

#fig4, ax4 = plt.subplots()
s.plot_contours(s.rbfmodel2, ax[1][1], X[:, 2], X[:, 3])
s.plot_data(ax[1][1], X[:, 2:4], "Petal Length", "Petal Width", " ")
#plt.show()

#fig5, ax5 = plt.subplots()
s.plot_contours(s.polymodel1, ax[0][2], X[:, 0], X[:, 1])
s.plot_data(ax[0][2], X[:, :2], "Sepal Length", "Sepal Width", "Polynomial kernel")

#fig6, ax6 = plt.subplots()
s.plot_contours(s.polymodel2, ax[1][2], X[:, 2], X[:, 3])
s.plot_data(ax[1][2], X[:, 2:4], "Petal Length", "Petal Width", " ")
plt.show()