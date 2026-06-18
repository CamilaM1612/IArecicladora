import cv2
import numpy as np
from collections import deque


class CamaraIA:

    def __init__(self):

        import tensorflow as tf

        self.tf = tf

        self.modelo = self.tf.keras.models.load_model(
            "modelo/modelo_reciclaje.keras"
        )

        self.clases = [
            "basura_domestica",   # 0
            "botella_plastico",   # 1
            "metalico",           # 2
            "organico",           # 3  ← movido aquí
            "papel_carton",       # 4  ← movido aquí
            "vidrio"              # 5  ← movido aquí
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

        self.historial = deque(maxlen=5)

    def _preprocesar(self, recorte_bgr):
        """
        OpenCV lee en BGR.
        Keras image_dataset_from_directory carga en RGB.
        Se convierte una sola vez aqui, en ningun otro lado.
        """
        rgb = cv2.cvtColor(
            recorte_bgr,
            cv2.COLOR_BGR2RGB
        )

        img = cv2.resize(
            rgb,
            (224, 224)
        )

        img = img.astype("float32")

        img = np.expand_dims(
            img,
            axis=0
        )

        return img

    def _predecir(self, img):

        pred = self.modelo.predict(
            img,
            verbose=0
        )[0]

        self.historial.append(pred)

        pred_suavizada = np.mean(
            self.historial,
            axis=0
        )

        indice = int(np.argmax(pred_suavizada))
        confianza = float(np.max(pred_suavizada) * 100)
        clase = self.clases[indice]
        categoria = self.categorias[clase]

        return clase, categoria, confianza

    def _dibujar_roi(self, frame, confianza):

        alto, ancho, _ = frame.shape

        x1 = int(ancho * 0.30)
        x2 = int(ancho * 0.70)
        y1 = int(alto * 0.15)
        y2 = int(alto * 0.85)

        if confianza >= 70:
            color = (0, 255, 0)
        elif confianza >= 40:
            color = (0, 200, 255)
        else:
            color = (0, 0, 255)

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            color,
            2
        )

        largo = 20
        grosor = 4

        cv2.line(frame, (x1, y1), (x1 + largo, y1), color, grosor)
        cv2.line(frame, (x1, y1), (x1, y1 + largo), color, grosor)

        cv2.line(frame, (x2, y1), (x2 - largo, y1), color, grosor)
        cv2.line(frame, (x2, y1), (x2, y1 + largo), color, grosor)

        cv2.line(frame, (x1, y2), (x1 + largo, y2), color, grosor)
        cv2.line(frame, (x1, y2), (x1, y2 - largo), color, grosor)

        cv2.line(frame, (x2, y2), (x2 - largo, y2), color, grosor)
        cv2.line(frame, (x2, y2), (x2, y2 - largo), color, grosor)

        return frame, x1, y1, x2, y2

    def obtener_frame(self):

        ret, frame = self.cap.read()

        if not ret:
            return None, None, None, None

        alto, ancho, _ = frame.shape

        x1 = int(ancho * 0.30)
        x2 = int(ancho * 0.70)
        y1 = int(alto * 0.15)
        y2 = int(alto * 0.85)

        # Recorte va al modelo, frame.copy() se muestra al usuario
        recorte = frame[y1:y2, x1:x2]

        img = self._preprocesar(recorte)

        clase, categoria, confianza = self._predecir(img)

        frame_mostrado = frame.copy()

        frame_mostrado, _, _, _, _ = self._dibujar_roi(
            frame_mostrado,
            confianza
        )

        return frame_mostrado, clase, categoria, confianza

    def procesar_imagen_archivo(self, ruta_imagen):

        img_original = cv2.imread(ruta_imagen)

        if img_original is None:
            return None, "sin_objeto", "NO DETECTADO", 0

        self.historial.clear()

        alto, ancho, _ = img_original.shape

        x1 = int(ancho * 0.30)
        x2 = int(ancho * 0.70)
        y1 = int(alto * 0.15)
        y2 = int(alto * 0.85)

        # Mismo recorte que en camara para consistencia
        recorte = img_original[y1:y2, x1:x2]

        img = self._preprocesar(recorte)

        clase, categoria, confianza = self._predecir(img)

        frame_mostrado = img_original.copy()

        frame_mostrado, _, _, _, _ = self._dibujar_roi(
            frame_mostrado,
            confianza
        )

        return frame_mostrado, clase, categoria, confianza

    def liberar(self):

        self.cap.release()