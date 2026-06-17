from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QPushButton
)

from PyQt5.QtCore import Qt

import qtawesome as qta


class MenuLateral(QFrame):

    def __init__(self):

        super().__init__()

        self.setFixedWidth(220)

        self.setStyleSheet("""
            QFrame{
                background-color:#111827;
                border-radius:20px;
            }

            QLabel{
                border:none;
                background:transparent;
            }

            QPushButton{
                background-color:transparent;
                color:white;
                border:none;
                padding:15px;
                text-align:left;
                font-size:15px;
                border-radius:10px;
            }

            QPushButton:hover{
                background-color:#1e293b;
            }

            QPushButton:pressed{
                background-color:#22c55e;
            }
        """)

        layout = QVBoxLayout()

        layout.setContentsMargins(
            15,
            20,
            15,
            20
        )

        layout.setSpacing(10)

        titulo = QLabel(
            "EcoVision"
        )

        titulo.setAlignment(
            Qt.AlignCenter
        )

        titulo.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#22c55e;
        """)

        layout.addWidget(
            titulo
        )

        layout.addSpacing(20)

        btn_inicio = QPushButton(
            qta.icon(
                "fa5s.home",
                color="white"
            ),
            " Inicio"
        )

        btn_historial = QPushButton(
            qta.icon(
                "fa5s.history",
                color="white"
            ),
            " Historial"
        )

        btn_estadisticas = QPushButton(
            qta.icon(
                "fa5s.chart-bar",
                color="white"
            ),
            " Estadísticas"
        )

        btn_configuracion = QPushButton(
            qta.icon(
                "fa5s.cog",
                color="white"
            ),
            " Configuración"
        )

        layout.addWidget(
            btn_inicio
        )

        layout.addWidget(
            btn_historial
        )

        layout.addWidget(
            btn_estadisticas
        )

        layout.addWidget(
            btn_configuracion
        )

        layout.addStretch()

        self.setLayout(
            layout
        )