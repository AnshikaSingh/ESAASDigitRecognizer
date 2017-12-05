from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from PIL import Image as aa
from PIL import ImageTk
import os
import os.path
import PIL.Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv
from numpy import genfromtxt
import sys
import pandas as pd

def modeltraining():    
    dataset = pd.read_csv("train.csv")
    X = dataset.iloc[:, 1:]
    y = dataset['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(X_train, y_train)
    return rf
#name is path of image
    
def inputimage(name,rf):
    
    img = aa.open(name).convert('L')
    
    
    iar=np.array(img)
    fp=open('result.txt','w')
    a='pixel'
    l=[]
    for i in range(0,784):
        b=','
        if i<=782:
            c=a+str(i)+b
            fp.write(c)
        else:
            c=a+str(i)
            fp.write(c)
    fp.close()    
    
    fp=open('result.txt','a')
    fp.write("\n")
    for  i in range(0,28):
        for j in range(0,28):
            e=','
            if i==27 & j==27:
                f=str(iar[i][j])
                fp.write(f)
            else:
                f=str(iar[i][j])+e
                fp.write(f)
    fp.close()	    

    thisfile="result.txt"
    if os.path.exists('csv_file.csv') :
        os.remove('csv_file.csv')
    
    os.rename(thisfile,"csv_file.csv")
    
    test = pd.read_csv("csv_file.csv").values
    
    pred = rf.predict(test)
    return pred[0]


                    
ans=inputimage(rf)


