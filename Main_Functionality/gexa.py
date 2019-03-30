import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten, Input, Conv2D, MaxPooling2D, BatchNormalization
from keras import optimizers
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from skimage import color
from skimage import io
import cv2
import os
from skimage import data
import matplotlib.pyplot as plt
print(keras.__version__)
model = keras.models.load_model('gexa_model.h5')
def wrapper(file_name):
    #print("Accessing file from wrapper")
    
    #print("File name is "+file_name)
    #image = cv2.imread(file_name)
    #img_2d = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_2d=data.imread(file_name,as_grey=True)
    #img_2d = color.rgb2gray(io.imread(file_name))
    #test_image = img
    test_image=cv2.resize(img_2d, (64,64))
    test_image_array = test_image.reshape(64, 64)
    test_image = np.expand_dims(test_image, axis = 0)
    test_image = np.expand_dims(test_image, axis = 3)
    result = model.predict(test_image)
    print(str(result[0][0])+" "+str(result[0][1])+" "+str(result[0][2])+" "+str(result[0][3])+" "+str(result[0][4])+" "+str(result[0][5])+" "+str(result[0][6])+" "+str(result[0][7])+" "+str(result[0][8])+" "+str(result[0][9]))
    #plt.imshow(test_image_array, cmap='gray')
    #print ("Alexa , what is the weather? : Confidence Score : "+str(result[0][1]))
    #print("Alexa , set an alarm         : Confidence Score : "+str(result[0][6]))
    decision=np.argmax(result[0])
    if(decision==4 or decision==1):
        print("ALEXA , PLAY SOME MUSIC")
    elif(decision==0):
        print("ALEXA , HOW IS THE WEATHER TODAY")
    elif(decision==6):
        print("NO ACTION PREDICTED")
    elif(decision==2):
        print("ALEXA , INCREASE THE VOLUME")
        #print("ALEXA , SET AN ALARM" +str(result[0][6])) 
    os.remove(file_name)
    return decision


