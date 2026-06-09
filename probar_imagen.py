import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

clases = [
    'basura_domestica',
    'botella_plastico',
    'envase_carton',
    'metalico',
    'papel_carton',
    'vidrio'
]

modelo = tf.keras.models.load_model("modelo_reciclaje.keras")

img = image.load_img(
    "prueba.jfif",
    target_size=(224,224)
)

img_array = image.img_to_array(img)

img_array = np.expand_dims(img_array, axis=0)

pred = modelo.predict(img_array)

indice = np.argmax(pred)

print("Clase:", clases[indice])
print("Confianza:", np.max(pred)*100)