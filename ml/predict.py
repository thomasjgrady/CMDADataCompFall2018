from keras.models import load_model
import numpy as np
import random

with open('data/maxes.txt', 'r') as f:
    x_norm = np.array(eval(f.readline()))
    y_norm = np.array(eval(f.readline()))

model = load_model("models/model1.h5")

# input_fields = ["STRUCTURETYPE", "REGION", "BUILT", "BEDRMS", "LMED", "PER"]

#inp = np.array([[1., 3., 1958., 3., 100000., 4.]])

for _ in range(30):
    inp = np.array([[random.random(), random.random(), random.random(), random.random(), random.random(), random.random()]])

    fmr = model.predict(inp)
    print(fmr*y_norm)