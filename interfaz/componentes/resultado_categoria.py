from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)

from PyQt5.QtCore import Qt

import qtawesome as qta


class ResultadoCategoria(QFrame):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("""
            QFrame{
                background-color:#0f172a;
                border:1px solid #334155;
                border-radius:18px;
            }
        """)

        layout = QVBoxLayout()

        layout.setContentsMargins(
            12,
            12,
            12,
            12
        )

        titulo = QLabel(
            "Categoría"
        )

        titulo.setStyleSheet("""
            color:#94a3b8;
            font-size:13px;
            border:none;
            background:transparent;
        """)

        self.icono_categoria = QLabel()

        self.icono_categoria.setAlignment(
            Qt.AlignCenter
        )

        self.icono_categoria.setStyleSheet("""
            border:none;
            background:transparent;
            padding:0px;
            margin:0px;
        """)

        self.descripcion_categoria = QLabel(
            "---"
        )

        self.descripcion_categoria.setAlignment(
            Qt.AlignCenter
        )

        self.descripcion_categoria.setStyleSheet("""
            font-size:15px;
            color:white;
            font-weight:bold;
            border:none;
            background:transparent;
            padding:0px;
            margin:0px;
        """)

        layout.addWidget(
            titulo
        )

        layout.addStretch()

        layout.addWidget(
            self.icono_categoria,
            alignment=Qt.AlignCenter
        )

        layout.addWidget(
            self.descripcion_categoria
        )

        layout.addStretch()

        self.setLayout(
            layout
        )

    def actualizar(
        self,
        reciclable=True
    ):

        if reciclable:

            self.icono_categoria.setPixmap(
                qta.icon(
                    "fa5s.recycle",
                    color="#22c55e"
                ).pixmap(32, 32)
            )

            self.descripcion_categoria.setText(
                "Reciclable"
            )

        else:

            self.icono_categoria.setPixmap(
                qta.icon(
                    "fa5s.times-circle",
                    color="#ef4444"
                ).pixmap(32, 32)
            )

            self.descripcion_categoria.setText(
                "No reciclable"
            )