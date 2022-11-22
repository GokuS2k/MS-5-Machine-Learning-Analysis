import numpy as np
import tensorflow as tf
from tensorflow import keras


def predict_rec(a, b):
    x = np.array(a)
    y = np.array(b)
    model = tf.keras.Sequential()
    model.add(keras.layers.Dense(16, input_shape=(1,)))
    model.add(keras.layers.Dropout(0.1))
    model.add(keras.layers.Dense(16))
    model.add(keras.layers.Dropout(0.1))
    model.add(keras.layers.Dense(1))
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    # model.summary()

    model.fit(x, y, epochs=200, verbose=0)
    result = model.predict(x)
    # print("Pred val:")
    # print(sum(result)/2)
    # pred_val = np.floor(result)
    return sum(result) / 2
