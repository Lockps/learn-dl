import tensorflow as tf
import numpy as np
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense

datain = int(input("what is number : "))

model = Sequential([Dense(units=1 , input_shape = [1])])
model.compile(optimizer='sgd',loss='mean_squared_error')

xs = np.array([-1.0, 0.0 , 1.0 , 2.0, 3.0, 4.0] , dtype=float)
ys = np.array([-3.0 , -1.0 , 1.0 , 3.0, 5.0 , 7.0])

model.fit(xs,ys,epochs = 100000)


print(model.get_config)
print(model.predict([datain]))