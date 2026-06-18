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
            "basura_domestica",
            "botella_plastico",
            "metalico",
            "papel_carton",
            "vidrio",
            "organico"
        ]

        self.categorias = {
            "basura_domestica": "NO RECICLABLE",
            "botella_plastico": "RECICLABLE",
            "metalico": "RECICLABLE",
            "papel_carton": "RECICLABLE",
            "vidrio": "RECICLABLE",
            "organico": "RECICLABLE"
        }

        self.cap = cv2.VideoCapture(0)

    def obtener_frame(self):

        ret, frame = self.cap.read()

        if not ret:
            return None, None, None, None

        img = cv2.resize(
            frame,
            (224, 224)
        )

        img = img.astype(
            "float32"
        )

        img = np.expand_dims(
            img,
            axis=0
        )

        pred = self.modelo.predict(
            img,
            verbose=0
        )

        indice = np.argmax(
            pred
        )

        confianza = float(
            np.max(pred) * 100
        )

        clase = self.clases[
            indice
        ]

        categoria = self.categorias[
            clase
        ]

        return (
            frame,
            clase,
            categoria,
            confianza
        )

    def procesar_imagen_archivo(self, ruta_imagen):
        
        """Procesa una imagen desde archivo"""
        
        img_original = cv2.imread(ruta_imagen)
        
        if img_original is None:
            return None, "sin_objeto", "NO DETECTADO", 0
        
        img = cv2.resize(
            img_original,
            (224, 224)
        )
        
        img = img.astype(
            "float32"
        )
        
        img = np.expand_dims(
            img,
            axis=0
        )
        
        pred = self.modelo.predict(
            img,
            verbose=0
        )
        
        indice = np.argmax(
            pred
        )
        
        confianza = float(
            np.max(pred) * 100
        )
        
        clase = self.clases[
            indice
        ]
        
        categoria = self.categorias[
            clase
        ]
        
        return (
            img_original,
            clase,
            categoria,
            confianza
        )

    def liberar(self):

        self.cap.release()