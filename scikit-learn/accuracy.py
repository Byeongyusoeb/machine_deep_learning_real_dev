'''
Delvelopment environment
 - Ubuntu with below packages
    * Scikit-learn
    * Scikit-image
    * Matplotlib
    * Scipy
    * Pandas
'''

'''
XOR

0 0 = 1
1 0 = 0
0 1 = 0
1 1 = 1
'''

from sklearn import svm, metrics
import warnings

def warn(*args, **kwargs):
    # To avoid scikit-learn future warning
    pass

warnings.warn = warn

data = [[0,0], [0,1], [1,0], [1,1]]

labels = [0, 1, 1, 0]

example_data = [[0, 0], [0, 1]]

example_labels = [0, 1]

# Core code

classifier = svm.SVC()

classifier.fit(data, labels) # sklearn.svm.SVC.fit([Q], [A])

results = classifier.predict(example_data)

accuracy = metrics.accuracy_score(example_labels, results) 

print('accuracy : ',accuracy)