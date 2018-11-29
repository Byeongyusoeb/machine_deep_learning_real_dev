import glob, os.path, re, json
from sklearn import svm, metrics
import matplotlib.pyplot
import pandas 

train_data = list()
train_label = list()

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

# Plotting 

graph_dict = dict()

for index in range(0, len(train_label)):

    label = train_label[index]

    data = train_data[index]

    if not (label in graph_dict):
        graph_dict[label] = data

asclist = [[chr(n) for n in range(97, 97+26)]]

df = pandas.DataFrame(graph_dict, index = asclist)

matplotlib.pyplot.style.use('ggplot')

df.plot(kind = 'bar', subplots = True, ylim = (0, 0.15))

matplotlib.pyplot.savefig('./download/lang/lang-plot.png')