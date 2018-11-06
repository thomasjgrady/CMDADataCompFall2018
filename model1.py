import csv
import matplotlib.pyplot as plt
import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation

data_filename = "data/thads2011.txt"

# Fields used as input to train the model
# city/suburb, num persons, owner status, type of structure, number of bedrooms, census region
train_input_fields = ["METRO3", "PER", "OWNRENT", "STRUCTURETYPE", "BEDRMS", "REGION"]
num_fields = len(train_input_fields)


# Response variable
# The burden of housing on the individual
train_output_fields = ["BURDEN"]

# Define the arrays that will hold train and test data
train_size = 130000
test_size = 10000
x_train = np.zeros((train_size, num_fields), dtype=float)
y_train = np.zeros((train_size), dtype=float)
x_test = np.zeros((test_size, num_fields), dtype=float)
y_test = np.zeros((test_size), dtype=float)

# Stores indeces of fields
fields_d = {}

# Get indeces of fields
with open(data_filename, 'rt') as f:

    csvreader = csv.reader(f)
    fields = next(csvreader)

    for i, field in enumerate(fields):
        fields_d[field] = i

    ex_line = next(csvreader)
    for field in train_input_fields:
        print(ex_line[fields_d[field]])

    # Make train dataset
    for i in range(train_size):
        line = next(csvreader)
        for j in range(num_fields):
            x_train[i,j] = float(line[fields_d[train_input_fields[j]]].strip("\'"))
        
        y_train[i] =  float(line[fields_d[train_output_fields[0]]].strip("\'"))
            
    # Make test dataset
    for i in range(test_size):
        line = next(csvreader)
        for j in range(num_fields):
            x_test[i,j] = float(line[fields_d[train_input_fields[j]]].strip("\'"))
        
        y_test[i] =  float(line[fields_d[train_output_fields[0]]].strip("\'"))

# Get infinity norm of each column
x_train_column_maxes = x_train.max(axis=0)
y_train_column_maxes = y_train.max(axis=0)

# Create normalized data
x_train_norm = x_train/x_train_column_maxes
y_train_norm = y_train/y_train_column_maxes

# Form the keras model
model = Sequential()
model.add(Dense(10, activation="relu", input_dim=num_fields))
model.add(Dropout(0.25))
model.add(Dense(20, activation="relu"))
model.add(Dropout(0.25))
model.add(Dense(10, activation="relu"))
model.add(Dropout(0.25))
model.add(Dense(5, activation="relu"))
model.add(Dropout(0.25))
model.add(Dense(1))

# Compile the model
model.compile(loss="mean_squared_error", optimizer="adam")

# Train the model
model.fit(x_train_norm, y_train_norm, epochs=10, batch_size=100)

# Test the fitted model
score = model.evaluate(x_test, y_test)

# Save the model
model.save("models/model1.h5")
