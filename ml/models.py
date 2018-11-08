import numpy as np

from thads2011 import *
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout
from keras.optimizers import SGD

def create_model():
    model = Sequential()
    model.add(Dense(num_input_fields*2, activation="relu", input_dim=num_input_fields))
    model.add(Dropout(0.5))
    model.add(Dense(num_input_fields, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(num_input_fields//2, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(4, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(2, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(2, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(1))

    return model

def create_optimizer(learning_rate, decay, momentum):
    sgd = SGD(lr=learning_rate, decay=decay, momentum=momentum, nesterov=True)
    return sgd

def train_model(model, x_train, y_train, epochs, batch_size):
    model.compile(loss="mean_squared_error", optimizer="adam")
    model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)
    
def test_model(model, x_test, y_test, batch_size):
    score = model.evaluate(x_test, y_test, batch_size=batch_size)
    return score

if __name__ == "__main__":

    train_size = 130000
    test_size = 10000

    epochs = 20
    batch_size = 1000

    model = create_model()
    optimizer = create_optimizer(0.01, 1e-6, 0.9)
    fields_dict = create_fields_dict()
    datasets = create_datasets(train_size, test_size, fields_dict)  
    
    x_train, x_test, y_train, y_test, x_train_normalized, y_train_normalized, x_test_normalized, y_test_normalized = datasets
    
    train_model(model, x_train_normalized, y_train_normalized, epochs, batch_size) 
    score = test_model(model, x_test_normalized, y_test_normalized, batch_size)
    print(score)

    model.save("models/model1.h5")
