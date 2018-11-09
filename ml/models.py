import numpy as np
import random
import time
import sys

from thads2011 import *

from ann_visualizer.visualize import ann_viz
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout
from keras.optimizers import SGD
from keras.callbacks import TensorBoard

def create_model():

    dropout_rate = 0.75

    model = Sequential()
    model.add(Dense(10, activation="relu", input_dim=num_input_fields))
    model.add(Dropout(dropout_rate))
    model.add(Dense(7, activation="relu"))
    model.add(Dropout(dropout_rate))
    model.add(Dense(5, activation="relu"))
    model.add(Dropout(dropout_rate))
    model.add(Dense(3, activation="relu"))
    model.add(Dropout(dropout_rate))
    model.add(Dense(1))

    return model

def create_optimizer(learning_rate, decay, momentum):
    sgd = SGD(lr=learning_rate, decay=decay, momentum=momentum, nesterov=True)
    return sgd

def train_model(model, optimizer, x_train, y_train, epochs, batch_size):
    tb_call_back = TensorBoard(log_dir='./models/graphs', histogram_freq=0, write_graph=True, write_images=True)
    model.compile(optimizer=optimizer, loss="mean_squared_error")
    start = time.time()
    hist = model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, callbacks=[tb_call_back], verbose=4)
    end = time.time()
    print("Model took %0.2f seconds to train" % (end - start))

    return hist
    
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
    
    # Set up SGD optimizer
    learning_rate = 0.2
    decay = (learning_rate/epochs)/2
    optimizer = create_optimizer(learning_rate, decay, 0.9)
    
    # Create datasets
    fields_dict = create_fields_dict()
    datasets = create_datasets(train_size, test_size, fields_dict)  
    x_train, x_test, y_train, y_test, x_train_normalized, y_train_normalized, x_test_normalized, y_test_normalized = datasets
    
    hist = train_model(model, optimizer, x_train_normalized, y_train_normalized, epochs, batch_size) 
    score = test_model(model, x_test_normalized, y_test_normalized, batch_size)
    fname = "{}_{}".format(sys.argv[1], sys.argv[2])
    with open('data/scores/'+fname+".txt", 'w') as f:
        f.write(str(score))
    print(str(score))

    loss = hist.history['loss']
    loss_final = loss[len(loss) - 1]

    with open('data/loss/'+fname+'.txt', 'w') as f:
        f.write(str(loss_final))

    model.save("models/{}.h5".format(fname))
    
    # img_fname = "images/{}.gv".format(fname)
    # ann_viz(model, title=fname, filename=img_fname)
