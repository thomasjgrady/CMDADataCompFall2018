import matplotlib.pyplot as plt

epochs = [num for num in range(10, 101, 10)]

y_train_loss = []
y_test_loss = []

for e in epochs:
    fname = "{}_{}".format(e, 10000)
    train_fname = "data/loss/{}.txt".format(fname)
    test_fname = "data/scores/{}.txt".format(fname)

    with open(train_fname, 'r') as f:
        val = float(f.read())
        y_train_loss.append(val)

    with open(test_fname, 'r') as f:
        val = float(f.read())
        y_test_loss.append(val)
        
plt.plot(epochs, y_train_loss)
plt.plot(epochs, y_test_loss)
plt.show()
