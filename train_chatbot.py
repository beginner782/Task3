import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random


accuracy=0.7

import os
if accuracy < 0.8:
    os.system("curl --user 'admin:admin@123' http://192.168.0.111:8080/job/task3_job4/build?token=tweak")
else:
    os.system("curl --user 'admin:admin@123' http://192.168.0.111:8080/job/task3_job5/build?token=notify")

