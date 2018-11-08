import csv
import numpy as np

# Where the data file is located
data_file_path = "data/thads2011.txt"

# Input fields and input fields in human readable format
input_fields = ["STRUCTURETYPE", "REGION", "BUILT", "BEDRMS", "LMED", "PER"]
num_input_fields = len(input_fields)

# Output fields and output fields in human readable format
output_fields = ["FMR"]
num_output_fields = len(output_fields)

# Create the dictionary mapping the headers to their indeces within the line
def create_fields_dict():

    fields_dict = {}

    with open(data_file_path, "rt") as datafile:
        reader = csv.reader(datafile)
        fields = next(reader)
        for i, field in enumerate(fields):
            fields_dict[field] = i

    return fields_dict


"""
Creates the datasets needed to train a model using the thads2011 dataset
Returns a tuple containg the following in order:
    x_train - The training dataset of dimension (train_size, num_input_fields)
    y_train - The training dataset of dimension (train_size, num_output_fields)
    x_test  - The testing dataset of dimension (test_size, num_input_fields)
    y_test  - The training dataset of dimension (test_size, num_output_fields)
    x_train_normalized - The normalized training dataset of dimension (train_size, num_input_fields)
    y_train_normalized - The normalized training dataset of dimension (train_size, num_output_fields)
    x_test_normalized  - The nomralized testing dataset of dimension (test_size, num_input_fields)
    y_test_normalized  - The normalized training dataset of dimension (test_size, num_output_fields)
"""
def create_datasets(train_size, test_size, fields_dict):

    x_train = np.zeros((train_size, num_input_fields), dtype=float)
    y_train = np.zeros((train_size, num_output_fields), dtype=float)
    x_test = np.zeros((test_size, num_input_fields), dtype=float)
    y_test = np.zeros((test_size, num_output_fields), dtype=float)
    x_train_normalized = np.zeros((train_size, num_input_fields), dtype=float)
    y_train_normalized = np.zeros((train_size, num_output_fields), dtype=float)
    x_test_normalized = np.zeros((test_size, num_input_fields), dtype=float)
    y_test_normalized = np.zeros((test_size, num_output_fields), dtype=float)

    with open(data_file_path, "rt") as datafile:
        reader = csv.reader(datafile)
        _fields = next(reader)

        for i in range(train_size):
            line = next(reader)
            
            for j, field in enumerate(input_fields):
                x_train[i,j] = float(line[fields_dict[field]].strip("\'"))

            for k, field in enumerate(output_fields):
                y_train[i,k] = float(line[fields_dict[field]].strip("\'"))

        for i in range(test_size):
            line = next(reader)
            
            for j, field in enumerate(input_fields):
                x_test[i,j] = float(line[fields_dict[field]].strip("\'"))

            for k, field in enumerate(output_fields):
                y_test[i,k] = float(line[fields_dict[field]].strip("\'"))
    
    # Get the infinity norm of each created dataset
    x_train_norm = x_train.max(axis=0)
    y_train_norm = y_train.max(axis=0)
    x_test_norm = x_test.max(axis=0)
    y_test_norm = y_test.max(axis=0)
    
    with open("data/maxes.txt", "w") as maxes:
        maxes.write(str(x_train_norm))
        maxes.write(str(y_train_norm))
        maxes.write(str(x_test_norm))
        maxes.write(str(y_test_norm))

    # Normalize each dataset
    x_train_normalized = x_train/x_train_norm
    y_train_normalized = y_train/y_train_norm
    x_test_normalized = x_test/x_test_norm
    y_test_normalized = y_test/y_test_norm

    return (x_train, x_test, y_train, y_test, x_train_normalized, y_train_normalized, x_test_normalized,
            y_test_normalized)


if __name__ == "__main__":
    f_d = create_fields_dict()
    datasets = create_datasets(10, 3, f_d)
    print(datasets)
