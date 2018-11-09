import numpy as np
import random
import time
import sys

from thads2011 import *
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout
from keras.optimizers import SGD

def create_model():
    model = Sequential()
    model.add(Dense(5, activation="relu", input_dim=num_input_fields))
    model.add(Dense(5, activation="relu"))

    # model.add(Dense(num_input_fields*2, activation="relu", input_dim=num_input_fields))
    # model.add(Dropout(0.5))
    # model.add(Dense(num_input_fields, activation="relu"))
    # model.add(Dropout(0.5))
    # model.add(Dense(num_input_fields//2, activation="relu"))
    # model.add(Dropout(0.5))
    # model.add(Dense(4, activation="relu"))
    # model.add(Dropout(0.5))
    # model.add(Dense(2, activation="relu"))
    # model.add(Dropout(0.5))
    # model.add(Dense(2, activation="relu"))
    # model.add(Dropout(0.5))
    model.add(Dense(1))

    return model

def create_optimizer(learning_rate, decay, momentum):
    sgd = SGD(lr=learning_rate, decay=decay, momentum=momentum, nesterov=True)
    return sgd

def train_model(model, x_train, y_train, epochs, batch_size):
    model.compile(loss="mean_squared_error", optimizer="adam")
    start = time.time()
    model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)
    end = time.time()
    print("Model took %0.2f seconds to train" % (end - start))
    
def test_model(model, x_test, y_test, batch_size):
    score = model.evaluate(x_test, y_test, batch_size=batch_size)
    return score

if __name__ == "__main__":

    total_size = 145531
    train_size = int(total_size * 0.8)
    test_size = int(total_size * 0.2)

    epochs = int(sys.argv[1])
    batch_size = int(sys.argv[2])

    model = create_model()
    optimizer = create_optimizer(0.01, 1e-6, 0.9)
    fields_dict = create_fields_dict()
    datasets = create_datasets(train_size, test_size, fields_dict)  
    
    x_train, x_test, y_train, y_test, x_train_normalized, y_train_normalized, x_test_normalized, y_test_normalized = datasets
    
    train_model(model, x_train_normalized, y_train_normalized, epochs, batch_size) 
    score = test_model(model, x_test_normalized, y_test_normalized, batch_size)
    fname = "{}_{}.txt".format(sys.argv[1], sys.argv[2])
    with open('data/scores/'+fname, 'w') as f:
        f.write(str(score))
    print(str(score))

    model.save("models/{}.h5".format(fname))
