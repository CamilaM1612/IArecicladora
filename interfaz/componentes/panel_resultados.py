from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)


class PanelResultados(QFrame):

    def __init__(self):

        super().__init__()

        self.setFixedWidth(340)

        self.setStyleSheet("""
            QFrame{
                background-color:#111827;
                border-radius:20px;
            }
        """)

        layout = QVBoxLayout()

        titulo = QLabel(
            "RESULTADO"
        )

        titulo.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
            padding:15px;
        """)

        layout.addWidget(titulo)

        objeto_card, self.objeto_label = (
            self.crear_tarjeta("OBJETO")
        )

        categoria_card, self.categoria_label = (
            self.crear_tarjeta("CATEGORÍA")
        )

        confianza_card, self.confianza_label = (
            self.crear_tarjeta("CONFIANZA")
        )

        contenedor_card, self.contenedor_label = (
            self.crear_tarjeta("CONTENEDOR")
        )

        layout.addWidget(objeto_card)
        layout.addWidget(categoria_card)
        layout.addWidget(confianza_card)
        layout.addWidget(contenedor_card)

        layout.addStretch()

        self.setLayout(layout)

    def crear_tarjeta(self, titulo):

        frame = QFrame()

        frame.setStyleSheet("""
            background-color:#0f172a;
            border:1px solid #334155;
            border-radius:15px;
        """)

        layout = QVBoxLayout()

        titulo_lbl = QLabel(titulo)

        titulo_lbl.setStyleSheet("""
            color:#94a3b8;
            font-size:12px;
            font-weight:bold;
        """)

        valor_lbl = QLabel("---")

        valor_lbl.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
            color:white;
        """)

        layout.addWidget(titulo_lbl)
        layout.addWidget(valor_lbl)

        frame.setLayout(layout)

        return frame, valor_lbl

    def actualizar_datos(
        self,
        clase,
        categoria,
        confianza
    ):

        nombres = {
            "basura_domestica": "Basura Doméstica",
            "botella_plastico": "Botella Plástica",
            "envase_carton": "Envase de Cartón",
            "metalico": "Metálico",
            "papel_carton": "Papel y Cartón",
            "vidrio": "Vidrio"
        }

        self.objeto_label.setText(
            nombres[clase]
        )

        self.confianza_label.setText(
            f"{confianza:.1f}%"
        )

        self.categoria_label.setText(
            categoria
        )

        if categoria == "RECICLABLE":

            self.categoria_label.setStyleSheet("""
                font-size:22px;
                font-weight:bold;
                color:#22c55e;
            """)

            self.contenedor_label.setText(
                "🟢 VERDE"
            )

        else:

            self.categoria_label.setStyleSheet("""
                font-size:22px;
                font-weight:bold;
                color:#ef4444;
            """)

            self.contenedor_label.setText(
                "🔴 ROJO"
            )