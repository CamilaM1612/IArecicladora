from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
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

        layout = QVBoxLayout()

        self.video_label = QLabel()

        self.video_label.setAlignment(
            Qt.AlignCenter
        )

        self.video_label.setMinimumSize(
            800,
            500
        )

        self.video_label.setStyleSheet("""
            background-color:black;
            border-radius:15px;
        """)

        layout.addWidget(
            self.video_label
        )

        self.setLayout(layout)

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

        self.video_label.setPixmap(
            QPixmap.fromImage(
                imagen_qt
            )
        )