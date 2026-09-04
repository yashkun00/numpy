numpy in tensorflow, doing image prediction

import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Densex = np.array([[1], [1], [3], [4]])y = np.array([[2], [4], [6], [8]])
model = Sequential([Dense(1, input_shape=(2, ))])
model.compile(optimizer='sgd', loss='mse')
model.fit(x, y, epochs=10, verbose=0)
print(model.predict(np.array([[6]])))
