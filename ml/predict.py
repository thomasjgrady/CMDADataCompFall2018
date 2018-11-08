from keras.models import load_model
import numpy as np

model = load_model("models/model1.h5")

maxes = np.array([6., 4., 2011., 8., 126600., 17.])

fmr = model.predict(np.array([[1., 3., 1958., 3., 190258., 4.]/maxes]))
print(fmr*3586)
