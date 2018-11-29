import glob, os.path, re, json
from sklearn import svm, metrics
import matplotlib.pyplot
import pandas 

train_data = list()
train_label = list()
test_data = list()
test_label = list()

files = glob.glob('./download/lang/train/*.txt') # Collect all file in directory

code_a = ord('a')
code_z = ord('z')

for file_name in files:
    base_name = os.path.basename(file_name) # Extract file name w/o directory path
    lang = base_name.split('-')[0]

    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.lower() # If there are mixed up Uppercase and Lowercase, could be mad to encode to ASCII

        # Alphabet frequency 

        count = [0 for _ in range(0, 26)] 

        for character in text:
            code_current = ord(character)

            if code_a <= code_current <= code_z:
                count[code_current - code_a] += 1

        # Normalization
        
        total = sum(count)
        count = list(map(lambda n : n/total, count))

        train_data.append(count)
        train_label.append(lang)

files = glob.glob('./download/lang/test/*.txt') # Collect all file in directory

code_a = ord('a')
code_z = ord('z')

for file_name in files:
    base_name = os.path.basename(file_name) # Extract file name w/o directory path
    lang = base_name.split('-')[0]

    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.lower() # If there are mixed up Uppercase and Lowercase, could be mad to encode to ASCII

        # Alphabet frequency 

        count = [0 for _ in range(0, 26)] # List for each alphabet count

        for character in text:
            code_current = ord(character)

            if code_a <= code_current <= code_z: 
                count[code_current - code_a] += 1 # ASCII 'a' is 97, if code_current is 'a' then count up 1 for count[0]

        # Normalization
        
        total = sum(count)
        count = list(map(lambda n : n/total, count))

        test_data.append(count)
        test_label.append(lang)

# Training

classifier = svm.SVC()

classifier.fit(train_data, train_label)

predict = classifier.predict(test_data)

score = metrics.accuracy_score(test_label, predict)

report = metrics.classification_report(test_label, predict)

print('Posibility :', score * 100, '%', end ='\n\n\n')
print('--- report ---\n\n', report)