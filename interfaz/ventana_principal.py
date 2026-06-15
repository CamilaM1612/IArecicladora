from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)

from PyQt5.QtCore import QTimer

from PyQt5.QtGui import (
    QImage,
    QPixmap
)

import cv2

from camara_ia import CamaraIA


class VentanaPrincipal(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Clasificador Inteligente de Residuos"
        )

        self.resize(900, 700)

        print("Antes de CamaraIA")

        self.camara = CamaraIA()

        print("Despues de CamaraIA")

        layout = QVBoxLayout()

        self.video_label = QLabel()
        layout.addWidget(self.video_label)

        self.objeto_label = QLabel(
            "Objeto: ---"
        )
        layout.addWidget(self.objeto_label)

        self.categoria_label = QLabel(
            "Categoria: ---"
        )
        layout.addWidget(self.categoria_label)

        self.confianza_label = QLabel(
            "Confianza: ---"
        )
        layout.addWidget(self.confianza_label)

        self.setLayout(layout)

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.actualizar_video
        )

        self.timer.start(100)

    def actualizar_video(self):

        frame, clase, categoria, confianza = (
            self.camara.obtener_frame()
        )

        if frame is None:
            return

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        h, w, ch = rgb.shape

        bytes_per_line = ch * w

        imagen_qt = QImage(
            rgb.data,
            w,
            h,
            bytes_per_line,
            QImage.Format_RGB888
        )

        self.video_label.setPixmap(
            QPixmap.fromImage(imagen_qt)
        )

        self.objeto_label.setText(
            f"Objeto: {clase}"
        )

        self.categoria_label.setText(
            f"Categoria: {categoria}"
        )

        self.confianza_label.setText(
            f"Confianza: {confianza:.1f}%"
        )

    def closeEvent(self, event):

        self.camara.liberar()

        event.accept()