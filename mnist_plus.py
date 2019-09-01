import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Flatten, Dense, Activation
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import pickle
"""
Create the model, train it, and then save (pickle) the model which yields the best accuracy.


best_score = 0
for i in range(50):
    #Loading Data  
    (x_train, y_train), (x_test,y_test) = mnist.load_data()


    #Creating the basic neural network using Keras
    model = Sequential()
    model.add(Flatten(input_shape=(28,28)))
    model.add(Dense(164, activation = "relu"))
    model.add(Dense(10,activation = "softmax"))
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(x_train,y_train,epochs=5)

    loss, score = model.evaluate(x_test,y_test)

    accuracy = score*100

    if accuracy > best_score:
        best_score = accuracy
        print("best accuracy: " + str(accuracy))
        with open("best_model.pickle", "wb") as f:
            pickle.dump(model, f)

"""


(x_train, y_train), (x_test,y_test) = mnist.load_data()

#Loading the fully trained model after 50 iterations
pickled = open("best_model.pickle", "rb")
model = pickle.load(pickled)

loss, score = model.evaluate(x_test, y_test)
accuracy = score*100
#Best accuracy was 73.29%
print(accuracy)
#Now, to implement a gui application that takes drawings (make sure)
#Convert drawings to 28x28 pixels, 