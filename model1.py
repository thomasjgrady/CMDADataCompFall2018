import csv
import matplotlib.pyplot as plt
import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

data_filename = "data/thads2011.txt"

# Fields used as input to train the model
# city/suburb, num persons, owner status, type of structure, number of bedrooms, census region
train_input_fields = ["METRO3", "PER", "OWNRENT", "STRUCTURETYPE", "BEDRMS", "REGION"]

# Response variable
# The burden of housing on the individual
train_output_fields = ["BURDEN"]

# Define the arrays that will hold train and test data
train_size = 130000
test_size = 10000
x_train = np.zeros((len(train_input_fields), train_size), dtype=float)
y_train = np.zeros((train_size), dtype=float)
x_test = np.zeros((len(train_input_fields), test_size), dtype=float)
y_test = np.zeros((test_size), dtype=float)

# Stores indeces of fields
fields_d = {}

# Get indeces of fields
with open(data_filename, 'rt') as f:

    csvreader = csv.reader(f)
    fields = next(csvreader)

    for i, field in enumerate(fields):
        fields_d[field] = i

    # Make train dataset
    for i in range(train_size):
        line = next(csvreader)
        for j in range(len(train_input_fields)):
            x_train[i,j] = float(line[fields_d[train_input_fields[j]]])
        
        y_train[i] =  float(line[fields_d[train_output_fields[0]]])
            
    # Make test dataset
    for i in range(test_size):
        line = next(csvreader)
        for j in range(len(train_input_fields)):
            x_test[i,j] = float(line[fields_d[train_input_fields[j]]])
        
        y_test[i] =  float(line[fields_d[train_output_fields[0]]])
            
print(x_train)


# Form the keras model
model = Sequential()
model.add(Dense(10, activation="relu", input_dim=len(train_input_fields)))
model.add(Dropout(0.25))
model.add(Dense(20, activation="relu"))
model.add(Dropout(0.25))
model.add(Dense(10, activation="relu"))
model.add(Dropout(0.25))
model.add(Dense(5, activation="relu"))
model.add(Dropout(0.25))
model.add(Dense(1))

# Hyperparameters
learning_rate = 0.01
decay = 1e-6
momentum = 0.9

# Optimizer
stochastic_gradient_descent = SGD(lr=learning_rate, decay=decay, momentum=momentum, nesterov=True)

# Compile the model
model.compile(loss="mean_squared_error", optimizer=stochastic_gradient_descent)
