 import sklearn
 #features = [[140, "smooth"], [130, "smooth"], [150, "bumy"], [170, "bumpy"]
#labels = ["apple", "apple","orange","orange"]
 features = [[140, 1], [130, 1], [150, 0], [170, 0]]
 labels = [0, 0, 1, 1]
 from sklearn import tree
clf = tree.DecisionTreeClassifier()	
clf =  clf.fit(features, labels)
print(clf.predict([[150, 0]]))
