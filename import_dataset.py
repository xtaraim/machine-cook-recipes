from sklearn.datasets import load_iris
>>> iris = load_iris()
>>> print(iris.feature_names)
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
>>> print(iris.target_names)
['setosa' 'versicolor' 'virginica']
>>> print(iris.data[0])
[5.1 3.5 1.4 0.2]
>>> print(iris.target[0])
0
>>> for i in range(len(iris.target)):
        print ("Example %d: label %s, features %s" %(i, iris.target[i], iris.data[i]))
        
        #https://en.wikipedia.org/wiki/Iris_flower_data_set#Data_set
