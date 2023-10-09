import numpy as np
import tensorflow as tf


def classify_image(path):
    image = tf.keras.preprocessing.image.load_img(path)
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)

    model = tf.keras.models.load_model("models/model.h5")
    prediction = model.predict(image)
    category = prediction.argmax()

    return category
