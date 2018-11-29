def downlaod():
    import urllib.request
    import gzip, os, os.path

    # Basic factor
    save_path = './download/handwriting'
    base_url = 'http://yann.lecun.com/exdb/mnist'
    files = [
        'train-images-idx3-ubyte.gz',
        'train-labels-idx1-ubyte.gz',
        't10k-images-idx3-ubyte.gz',
        't10k-labels-idx1-ubyte.gz',
    ]

    # Download 
    if not os.path.exists(save_path): os.mkdir(save_path)

    for file in files:
        url = base_url + '/' + file
        location = save_path + '/' + file

        if not os.path.exists(location): urllib.request.urlretrieve(url, location)

    # Unzip
    for file in files:
        gz_file = save_path + '/' +file
        raw_file = save_path + '/' + file.replace('.gz', '')

        with gzip.open(gz_file, 'rb') as r:
            body = r.read()

            with open(raw_file, 'wb') as w:
                w.write(body)


def to_csv(name, maxdata):
    import struct
    
    # Image and Label file open
    label_file = open('./download/handwriting/' + name + '-labels-idx1-ubyte', 'rb')
    image_file = open('./download/handwriting/' + name + '-images-idx3-ubyte', 'rb')
    csv_file = open('./download/handwriting/' + name + '.csv', 'w', encoding = 'utf-8')

    # Read header 
    mag, label_count = struct.unpack('>II', label_file.read(8))
    mag, image_count = struct.unpack('>II', image_file.read(8))
    rows, cols = struct.unpack('>II', image_file.read(8))

    pixels = rows * cols 

    # Read and write to csv file
    for index in range(label_count):
        if index > maxdata: break

        # Unpack requires a buffer of 1 bytes
        label = struct.unpack('B', label_file.read(1))[0]
        bdata = image_file.read(pixels)
        sdata = list(map(lambda n: str(n), bdata))
        csv_file.write(str(label) + ',')
        csv_file.write(','.join(sdata) + '\r\n')

        # Less than 10th data are made to pgm file to double-check
        if index < 10:
            s = 'P2 28 28 255\n'
            s += ' '.join(sdata)
            iname = './download/handwriting/{}-{}-{}.pgm'.format(name, index, label)

            with open(iname, 'w', encoding = 'utf-8') as f:
                f.write(s)

    csv_file.close()
    label_file.close()
    image_file.close()

# download()
# to_csv('train', 60000)
# to_csv('t10k', 10000)

import pandas
from sklearn import model_selection, svm, metrics

train_csv = pandas.read_csv('./download/handwriting/train.csv', header=None)
tk_csv = pandas.read_csv('./download/handwriting/t10k.csv', header=None)

def convert(l):
    # Normalization
    output = []
    for i in l:
        # The range of data is 0 ~ 255, so we divide with 256 to be ranged 0 ~ 1
        output.append(float(i) / 256)
    return output


train_csv_data = list(map(convert, train_csv.iloc[:, 1:].values))
tk_csv_data = list(map(convert, tk_csv.iloc[:, 1:].values))

# First value of each line is label
train_csv_label = train_csv[0].values
tk_csv_label = tk_csv[0].values

classifier = svm.SVC()

classifier.fit(train_csv_data, train_csv_label)

predict = classifier.predict(tk_csv_data)

score = metrics.accuracy_score(tk_csv_label, predict) 

report = metrics.classification_report(tk_csv_label, predict)

print('This prediction has {}% possibility'.format(score*100))

print(report)