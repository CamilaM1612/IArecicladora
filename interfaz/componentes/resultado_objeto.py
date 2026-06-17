from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)

from PyQt5.QtCore import Qt

import qtawesome as qta


class ResultadoObjeto(QFrame):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("""
            QFrame{
                background-color:#0f172a;
                border:1px solid #334155;
                border-radius:18px;
            }

            QLabel{
                border:none;
                background:transparent;
            }
        """)

        layout = QHBoxLayout()

        icono_container = QFrame()

        icono_container.setFixedSize(
            100,
            100
        )

        icono_container.setStyleSheet("""
            background-color:#16351f;
            border:none;
            border-radius:50px;
        """)

        icono_layout = QVBoxLayout()
        icono_layout.setContentsMargins(0, 0, 0, 0)

        self.icono_objeto = QLabel()

        self.icono_objeto.setAlignment(
            Qt.AlignCenter
        )

        self.icono_objeto.setStyleSheet("""
            border:none;
            background:transparent;
        """)

        icono_layout.addWidget(
            self.icono_objeto
        )

        icono_container.setLayout(
            icono_layout
        )

        texto_layout = QVBoxLayout()

        titulo = QLabel(
            "Objeto Detectado"
        )

        titulo.setStyleSheet("""
            color:#94a3b8;
            font-size:13px;
            border:none;
            background:transparent;
        """)

        self.objeto_label = QLabel("---")

        self.objeto_label.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
            color:#22c55e;
            border:none;
            background:transparent;
        """)

        self.categoria_label = QLabel("---")

        self.categoria_label.setFixedWidth(
            170
        )

        self.categoria_label.setAlignment(
            Qt.AlignCenter
        )

        self.categoria_label.setStyleSheet("""
            background-color:#22c55e;
            color:black;
            font-size:14px;
            font-weight:bold;
            border:none;
            border-radius:8px;
            padding:6px;
        """)

        texto_layout.addStretch()

        texto_layout.addWidget(
            titulo
        )

        texto_layout.addWidget(
            self.objeto_label
        )

        texto_layout.addWidget(
            self.categoria_label
        )

        texto_layout.addStretch()

        layout.addWidget(
            icono_container
        )

        layout.addLayout(
            texto_layout
        )

        self.setLayout(
            layout
        )

    def actualizar(
        self,
        nombre,
        categoria,
        icono
    ):

        self.objeto_label.setText(
            nombre
        )

        self.icono_objeto.setPixmap(
            icono.pixmap(60, 60)
        )

        self.categoria_label.setText(
            categoria
        )