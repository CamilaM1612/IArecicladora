from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton
)

from PyQt5.QtCore import Qt

from PyQt5.QtGui import (
    QImage,
    QPixmap
)

import cv2


class PanelWebcam(QFrame):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("""
            QFrame{
                background-color:#111827;
                border:2px solid #334155;
                border-radius:20px;
            }
        """)

        layout_principal = QVBoxLayout()

        # ==========================
        # TITULO
        # ==========================

        titulo = QLabel(
            "📹 Cámara en tiempo real"
        )
        estado = QLabel(
            "🟢 Cámara Activa"
        )

        estado.setStyleSheet("""
            color:#22c55e;
            font-size:14px;
            padding-left:10px;
            border:none;
        """)

        layout_principal.addWidget(
            estado
        )
        titulo.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
            color:white;
            padding:10px;
            border:none;
        """)

        layout_principal.addWidget(
            titulo
        )

        # ==========================
        # VIDEO
        # ==========================

        self.video_label = QLabel()

        self.video_label.setAlignment(
            Qt.AlignCenter
        )

        self.video_label.setMinimumSize(
            800,
            500
        )

        self.video_label.setStyleSheet("""
            background-color:#020617;
            border-radius:15px;
            border:2px solid #1e293b;
        """)

        layout_principal.addWidget(
            self.video_label
        )

        # ==========================
        # BOTONES
        # ==========================

        botones_layout = QHBoxLayout()

        self.btn_iniciar = QPushButton(
            "📷 Iniciar Cámara"
        )

        self.btn_detener = QPushButton(
            "⏹ Detener Cámara"
        )

        self.btn_iniciar.setStyleSheet("""
            QPushButton{
                background-color:#22c55e;
                color:white;
                border:none;
                padding:14px;
                border-radius:12px;
                font-size:15px;
                font-weight:bold;
            }

            QPushButton:hover{
                background-color:#16a34a;
            }
        """)

        self.btn_detener.setStyleSheet("""
            QPushButton{
                background-color:#1e293b;
                color:white;
                border:none;
                padding:14px;
                border-radius:12px;
                font-size:15px;
                font-weight:bold;
            }

            QPushButton:hover{
                background-color:#334155;
            }
        """)

        botones_layout.addWidget(
            self.btn_iniciar
        )

        botones_layout.addWidget(
            self.btn_detener
        )

        layout_principal.addLayout(
            botones_layout
        )

        self.setLayout(
            layout_principal
        )

    def actualizar_frame(self, frame):

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

        pixmap = QPixmap.fromImage(
            imagen_qt
        )

        self.video_label.setPixmap(
            pixmap.scaled(
                self.video_label.width(),
                self.video_label.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )