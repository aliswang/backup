import numpy
import os
import random
from PIL import Image

label = ['daisy','dandelion','rose','sunflower','tulip']
batch_count = 0
x_train_size = 0
x_train = 0

def get_array(file_name, format_size):
    path = "./" + file_name + "/"
    images = []
    for r, d, f in os.walk(path):
        for file in f:
            if('.jpg' in file):
                image = Image.open(os.path.join(r, file))
                image = image.resize((format_size, format_size))
                image = list(numpy.asarray(image))
                images.append(image)
    return images

def one_hot_(a):
    global label
    b = numpy.zeros((a.size, len(label)))
    for i in range(len(a)):
        b[i][label.index(a[i])]= 1
    return b

def get_data(test_cut=0.8, normalize=True, one_hot=False, format_size=28):
    global x_train_size
    global x_train
    all_img = []
    all_label = []
    for i in label:
        img_tmp = get_array(i, format_size)
        label_tmp = list(numpy.full(len(img_tmp), i))
        all_img += img_tmp
        all_label += label_tmp
    img_random = []
    label_random = []
    #random data
    r = random.sample(range(0, len(all_label)), len(all_label))
    for i in range(len(r)):
        img_random += [all_img[int(r[i])]]
        label_random += [all_label[int(r[i])]]
    img_random = numpy.asarray(img_random)
    label_random = numpy.asarray(label_random)
    if(normalize == True):
        img_random = img_random.astype('float32') / 255.0
    num = int(len(label_random) * test_cut)
    x_train = img_random[:num]
    y_train = label_random[:num]
    x_test = img_random[num:]
    y_test = label_random[num:]
    x_train_size = len(x_train)
    if(one_hot == True):
        y_train = one_hot_(y_train)
        y_test = one_hot_(y_test)
    return (x_train, y_train), (x_test, y_test)

def  next_batch(batch_size):
    global batch_count
    global x_train_size
    global x_train
    if(x_train_size == 0):
        get_data()
    if(batch_count + batch_size) >= x_train_size:
        batch_count = 0
    tmp = x_train[batch_count:batch_count + batch_size]
    batch_count += batch_size

    return tmp
