#-------------------------------------------------------------------------
# AUTHOR: Siddharth Kekre
# FOR: CS 4210- Assignment #4
#-----------------------------------------------------------*/


# Importing Necessary Libraries
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def build_model(n_hidden, n_neurons_hidden, n_neurons_output, learning_rate):

    # Creating the Neural Network using the Sequential API
    model = keras.models.Sequential()
    model.add(keras.layers.Flatten(input_shape=[28, 28])) # Input Layer

    # Iterate over the number of hidden layers to create the hidden layers:
    for _ in range(n_hidden):
        model.add(keras.layers.Dense(n_neurons_hidden, activation="relu"))  # hidden layers

    # Output Layer with one neural for each class and the softmax activation function since the classes are exclusive
    model.add(keras.layers.Dense(n_neurons_output, activation="softmax"))  # output layer               

    # Defining the Learning Rate and Optimizer
    opt = keras.optimizers.SGD(learning_rate)

    # Compiling the Model specifying the loss function and the optimizer to use.
    model.compile(loss="sparse_categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
    return model


'''
Using Keras to Load the Dataset. 
Every image is represented as a 28x28 array rather than a 1D array of size 784. 
Moreover, the pixel intensities are represented as integers (from 0 to 255) rather than floats (from 0.0 to 255.0).
'''
fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()

# Creating a Validation Set and Scaling the Features
X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:] / 255.0
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

# For Fashion MNIST, we need the list of class names to know what we are dealing with. For instance, class_names[y_train[0]] = 'Coat'
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

# Initialize Parametrs
n_hidden = [2, 5, 10]
n_neurons = [10, 50, 100]
l_rate = [0.01, 0.05, 0.1]
highestAccuracy = 0.0  
best_params = (0, 0, 0)  
best_model = None  
best_history = None  

# Iterate here over number of hidden layers, number of neurons in each hidden layer and the learning rate.
for h in n_hidden:          # looking for the best parameters w.r.t the number of hidden layers
    for n in n_neurons:     # looking for the best parameters w.r.t the number of neurons
        for l in l_rate:    # looking for the best parameters w.r.t the learning rate

            # Build the Model for Each Combination
            model = build_model(h, n, len(class_names), l)

            # Train the Model for 5 epochs
            history = model.fit(X_train, y_train, epochs=5, validation_data=(X_valid, y_valid))

            # Calculate the accuracy of this neural network and store its value if it is the highest so far. 
            class_predicted = np.argmax(model.predict(X_test), axis=-1)

            test_accuracy = np.sum(class_predicted == y_test) / len(y_test)
            if test_accuracy > highestAccuracy:
                highestAccuracy = test_accuracy
                best_model = model
                best_params = (h, n, l)
                best_history = history

            print("Highest accuracy so far: " + str(highestAccuracy))
            print("Parameters: " + "Number of Hidden Layers: " + str(h) + ", number of neurons: " + str(n) + ", learning rate: " + str(l)+ "\n")

'''
After generating all neural networks, print the summary of the best model found.
The model's summary() method displays 
    - all the model's layers
        - including each layer's name (which is automatically generated unless you set it when creating the layer)
    - its output shape (None means the batch size can be anything).
    - its number of parameters. 

Note that Dense layers often have a lot of parameters. This gives the model quite a lot of flexibility to fit the training data, 
but it also means that the model runs the risk of overfitting, especially when you do not have a lot of training data.
'''
print(best_model.summary())
img_file = './model_arch.png'
tf.keras.utils.plot_model(best_model, to_file=img_file, show_shapes=True, show_layer_names=True)

# Plotting the learning curves of the best model
pd.DataFrame(best_history.history).plot(figsize=(8, 5))
plt.grid(True)
plt.gca().set_ylim(0, 1)  # set the vertical range to [0-1]
plt.show()

