import numpy as np
from sklearn import svm, datasets
import matplotlib.pyplot as plt
import matplotlib.colors as mcol
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class PCA_demo:
    def __init__(self):
        #Loads the dataset from sklearn library
        self.iris = datasets.load_iris()
        #self.cm1 = mcol.LinearSegmentedColormap.from_list("cm1",["cyan", "yellow", "lightblue"])

        #Seperates features and target class
        self.X = self.iris.data
        self.Y = self.iris.target

    # Classifying using SVM from sklearn library
    def classify(self):
        '''
            Linear kernel
            Lmodel1 classifies using sepal length and width, Lmodel2 classifies using petal length and width
            Lmodel classifies using all 4 features
            All models use linear kernels with regularization parameter = 1

            RBF kernel
            rbfmodel1 classifies using sepal length and width, rbfmodel2 classifies using petal length and width
            rbfmodel classifies using all 4 features
            All models use RBF kernels with regularization parameter = 1
            
            Polynomial kernel
            polymodel1 classifies using sepal length and width, polymodel2 classifies using petal length and width
            polymodel classifies using all 4 features
            All models use Polynomials kernels with regularization parameter = 1
        '''
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
        '''
            y1 is the classifier output for test set using sepal length and sepal width.
            y2 uses petal length and petal width where as y uses all the features
        '''
        y1 = self.Lmodel1.predict(self.X[:, :2])
        y2 = self.Lmodel2.predict(self.X[:, 2:4])
        y = self.Lmodel.predict(self.X)
        print("\nLinear model")
        print("Accuracy with respect to sepal length and width = ",accuracy_score(self.Y, y1, normalize=True))
        print("Accuracy with respect to petal length and width = ",accuracy_score(self.Y, y2, normalize=True))
        print("Accuracy with respect to all features = ",accuracy_score(self.Y, y, normalize=True))

        y1 = self.rbfmodel1.predict(self.X[:, :2])
        y2 = self.rbfmodel2.predict(self.X[:, 2:4])
        y = self.rbfmodel.predict(self.X)
        print('\nRBF model')
        print("Accuracy with respect to sepal length and width = ",accuracy_score(self.Y, y1, normalize=True))
        print("Accuracy with respect to petal length and width = ",accuracy_score(self.Y, y2, normalize=True))
        print("Accuracy with respect to all features = ",accuracy_score(self.Y, y, normalize=True))

        y1 = self.polymodel1.predict(self.X[:, :2])
        y2 = self.polymodel2.predict(self.X[:, 2:4])
        y = self.polymodel.predict(self.X)
        print('\nPolynomial model')
        print("Accuracy with respect to sepal length and width = ",accuracy_score(self.Y, y1, normalize=True))
        print("Accuracy with respect to petal length and width = ",accuracy_score(self.Y, y2, normalize=True))
        print("Accuracy with respect to all features = ",accuracy_score(self.Y, y, normalize=True))

    def accuracy_pca(self):
        print('\n\nPCA')
        y1 = self.Lmodel_pca.predict(self.PX)
        print("Accuracy (Linear model) = ", accuracy_score(self.Y, y1, normalize=True))
        y2 = self.rbfmodel_pca.predict(self.PX)
        print("Accuracy (RBF model) = ", accuracy_score(self.Y, y2, normalize=True))
        y3 = self.polymodel_pca.predict(self.PX)
        print("Accuracy (Polynomial kernel) = ", accuracy_score(self.Y, y3, normalize=True))

    def calssify_pca(self):
        self.Lmodel_pca = svm.SVC(kernel='linear', C=1).fit(self.PX, self.Y)
        self.rbfmodel_pca = svm.SVC(kernel='rbf', C=1).fit(self.PX, self.Y)
        self.polymodel_pca = svm.SVC(kernel='poly', C=1).fit(self.PX, self.Y)

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

    def pca(self):
        X = StandardScaler().fit_transform(self.X)
        pca_model = PCA(n_components=2)
        self.PX = pca_model.fit_transform(X)
        return

p = PCA_demo()
p.classify()
p.accuracy()

fig1, ax1 = plt.subplots()
p.plot_contours(p.Lmodel1, ax1, p.X[:, 0], p.X[:, 1])
p.plot_data(ax1, p.X[:, :2],  "Sepal Length", "Sepal Width", "Linear kernel")

fig2, ax2 = plt.subplots()
p.plot_contours(p.Lmodel2, ax2, p.X[:, 2], p.X[:, 3])
p.plot_data(ax2, p.X[:, 2:4], "Petal Length", "Petal Width", "Linear kernel")

fig3, ax3 = plt.subplots()
p.plot_contours(p.rbfmodel1, ax3, p.X[:, 0], p.X[:, 1])
p.plot_data(ax3, p.X[:, :2], "Sepal Length", "Sepal Width", "RBF kernel")

fig4, ax4 = plt.subplots()
p.plot_contours(p.rbfmodel2, ax4, p.X[:, 2], p.X[:, 3])
p.plot_data(ax4, p.X[:, 2:4], "Petal Length", "Petal Width", "RBF kernel")

fig5, ax5 = plt.subplots()
p.plot_contours(p.polymodel1, ax5, p.X[:, 0], p.X[:, 1])
p.plot_data(ax5, p.X[:, :2], "Sepal Length", "Sepal Width", "Polynomial kernel")

fig6, ax6 = plt.subplots()
p.plot_contours(p.polymodel2, ax6, p.X[:, 2], p.X[:, 3])
p.plot_data(ax6, p.X[:, 2:4], "Petal Length", "Petal Width", "Polynomial kernel")

p.pca()
p.calssify_pca()
p.accuracy_pca()

fig7, ax7 = plt.subplots()
p.plot_contours(p.Lmodel_pca, ax7, p.PX[:, 0], p.PX[:, 1])
p.plot_data(ax7, p.PX, "Principal component 1", "Principal component 2", "Linear kernel")

fig8, ax8 = plt.subplots()
p.plot_contours(p.rbfmodel_pca, ax8, p.PX[:, 0], p.PX[:, 1])
p.plot_data(ax8, p.PX, "Principal component 1", "Principal component 2", "RBF kernel")

fig9, ax9 = plt.subplots()
p.plot_contours(p.polymodel_pca, ax9, p.PX[:, 0], p.PX[:, 1])
p.plot_data(ax9, p.PX, "Principal component 1", "Principal component 2", "Polynomial kernel")
plt.show()