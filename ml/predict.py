from keras.models import load_model
import numpy as np
import random
import sys

with open('data/maxes.txt', 'r') as f:
    x_norm = np.array(eval(f.readline()))
    y_norm = np.array(eval(f.readline()))

epochs = sys.argv[1]
batch_size = sys.argv[2]
fname = "{}_{}".format(epochs, batch_size)

model = load_model("models/{}.h5".format(fname))

inp = np.array([[3., 1958., 5., 50000.]])
lmed = model.predict(inp/x_norm)
print(lmed*y_norm)

# for _ in range(30):
#     inp = np.array([[random.random(), random.random(), random.random(), random.random(), random.random(), random.random()]])
# 
#     fmr = model.predict(inp)
#     print(fmr*y_norm)
