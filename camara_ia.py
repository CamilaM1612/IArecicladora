import cv2
import numpy as np

class CamaraIA:

    def __init__(self):

        import tensorflow as tf

        self.tf = tf

        self.modelo = self.tf.keras.models.load_model(
            "modelo/modelo_reciclaje.keras"
        )

        self.clases = [
            'basura_domestica',
            'botella_plastico',
            'envase_carton',
            'metalico',
            'papel_carton',
            'vidrio'
        ]

        self.categorias = {
            "basura_domestica": "NO RECICLABLE",
            "botella_plastico": "RECICLABLE",
            "envase_carton": "RECICLABLE",
            "metalico": "RECICLABLE",
            "papel_carton": "RECICLABLE",
            "vidrio": "RECICLABLE"
        }

        self.cap = cv2.VideoCapture(0)

    def obtener_frame(self):

        ret, frame = self.cap.read()

        if not ret:
            return None, None, None, None

        img = cv2.resize(frame, (224, 224))
        img = img.astype("float32")
        img = np.expand_dims(img, axis=0)

        pred = self.modelo.predict(
            img,
            verbose=0
        )

        indice = np.argmax(pred)

        confianza = float(
            np.max(pred) * 100
        )

        clase = self.clases[indice]

        categoria = self.categorias[clase]

        return frame, clase, categoria, confianza

    def liberar(self):
        self.cap.release()