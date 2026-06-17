from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)

from PyQt5.QtCore import Qt

import qtawesome as qta


class ResultadoContenedor(QFrame):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("""
            QFrame{
                background-color:#13281d;
                border:1px solid #22c55e;
                border-radius:18px;
            }
        """)

        layout = QHBoxLayout()

        layout.setContentsMargins(
            15,
            15,
            15,
            15
        )

        layout.setSpacing(
            15
        )

        self.icono = QLabel()

        self.icono.setAlignment(
            Qt.AlignCenter
        )

        self.icono.setFixedWidth(
            70
        )

        self.icono.setStyleSheet("""
            border:none;
            background:transparent;
        """)

        texto = QVBoxLayout()

        texto.setSpacing(
            2
        )

        titulo = QLabel(
            "Contenedor sugerido"
        )

        titulo.setStyleSheet("""
            color:#94a3b8;
            font-size:13px;
            border:none;
            background:transparent;
        """)

        self.color_label = QLabel("---")

        self.color_label.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            border:none;
            background:transparent;
        """)

        self.descripcion = QLabel("---")

        self.descripcion.setStyleSheet("""
            color:white;
            font-size:14px;
            border:none;
            background:transparent;
        """)

        texto.addWidget(
            titulo
        )

        texto.addWidget(
            self.color_label
        )

        texto.addWidget(
            self.descripcion
        )

        layout.addWidget(
            self.icono,
            alignment=Qt.AlignCenter
        )

        layout.addLayout(
            texto
        )

        self.setLayout(
            layout
        )

    def actualizar(
        self,
        color,
        descripcion,
        reciclable=True
    ):

        configuracion = {

            "AZUL": {
                "texto": "#3b82f6",
                "borde": "#3b82f6",
                "fondo": "#172554",
                "icono": "fa5s.file"
            },

            "AMARILLO": {
                "texto": "#eab308",
                "borde": "#eab308",
                "fondo": "#422006",
                "icono": "fa5s.recycle"
            },

            "VERDE": {
                "texto": "#22c55e",
                "borde": "#22c55e",
                "fondo": "#13281d",
                "icono": "fa5s.wine-bottle"
            },

            "MARRÓN": {
                "texto": "#d97706",
                "borde": "#92400e",
                "fondo": "#2d1606",
                "icono": "fa5s.apple-alt"
            },

            "NEGRO": {
                "texto": "#d1d5db",
                "borde": "#6b7280",
                "fondo": "#111827",
                "icono": "fa5s.trash"
            }
        }

        info = configuracion.get(
            color,
            configuracion["NEGRO"]
        )

        self.color_label.setText(
            color
        )

        self.descripcion.setText(
            descripcion
        )

        self.color_label.setStyleSheet(f"""
            font-size:28px;
            font-weight:bold;
            color:{info['texto']};
            border:none;
            background:transparent;
        """)

        self.icono.setPixmap(
            qta.icon(
                info["icono"],
                color=info["texto"]
            ).pixmap(50, 50)
        )

        self.setStyleSheet(f"""
            QFrame{{
                background-color:{info['fondo']};
                border:1px solid {info['borde']};
                border-radius:18px;
            }}
        """)