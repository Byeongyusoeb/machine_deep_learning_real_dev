import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

csv = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv')

data = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]

label = csv['Name']

# train_data, test_data, train_label, test_label = train_test_split(data, label)

classifier = svm.SVC()

classifier.fit(data, label)

results = classifier.predict([[5.1, 3.0, 1.3, 0.2]])

# score = metrics.accuracy_score(results, test_label) # about 97.3% accuracy 

print(results)