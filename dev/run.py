from keras.models import load_model
import tensorflow as tf
import numpy as np
from keras.models import Sequential
from keras.utils import np_utils
from keras.layers import Dense, Activation , LSTM , Dropout , AveragePooling3D
import pandas as pd
import json
import shutil
import urllib

import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import os
from pathlib import Path

# !pip install pytest-shutil
loc = "test_reso/"


model = load_model('Epilepsy.h5') #this folder has been saved fron the model we ran in the model ipy file

dirs = listdir(loc)
path = Path(loc+dirs[1])
print(path)

df=pd.read_csv(path)
df.head()

# X=df.drop(['y'],axis=1)
X=df.values
X=X[:,1:-1]
X = np.asarray(X).astype(np.float32)
# X=X[:,1:-1]

y=np.array(df['y'])
Y=np_utils.to_categorical(y)
y_pred = model.predict((X[:,::4]-X.mean())/X.std())
yp=np.zeros((Y.shape[0]))
yo=np.ones((Y.shape[0]))
for i in range(Y.shape[0]):
    yp[i]=np.argmax(y_pred[i])+1
    yo[i]=np.argmax(Y[i])

res_final = yp[0]

arr=[]
out_path = "Out/"
if res_final == 1.0:
    res = "Yes"
else:
    res = "No"
# json file input
j_dict = {
         "result" : res,
         "Name" : "Name-i",
    }
arr.append(j_dict)
json_object = json.dumps(arr, indent = 4)

with open("out.json", "w") as outfile:
      outfile.write(json_object)

# # deleting data info
# shutil.rmtree(loc)
# os.mkdir(loc)
