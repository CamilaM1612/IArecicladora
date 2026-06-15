from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QPushButton
)

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

        titulo = QLabel(
            "♻ EcoVision"
        )

        titulo.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            padding:15px;
            color:#22c55e;
        """)

        layout.addWidget(titulo)

        layout.addWidget(
            QPushButton(
                qta.icon("fa5s.home"),
                " Inicio"
            )
        )

        layout.addWidget(
            QPushButton(
                qta.icon("fa5s.history"),
                " Historial"
            )
        )

        layout.addWidget(
            QPushButton(
                qta.icon("fa5s.chart-bar"),
                " Estadísticas"
            )
        )

        layout.addWidget(
            QPushButton(
                qta.icon("fa5s.cog"),
                " Configuración"
            )
        )

        layout.addStretch()

        self.setLayout(layout)