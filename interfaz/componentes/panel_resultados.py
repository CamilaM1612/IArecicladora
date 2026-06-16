from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)

from PyQt5.QtCore import Qt

from interfaz.componentes.indicador_confianza import (
    IndicadorConfianza
)


class PanelResultados(QFrame):

    def __init__(self):

        super().__init__()

        self.setFixedWidth(420)

        self.setStyleSheet("""
            QFrame{
                background-color:#111827;
                border-radius:20px;
            }
        """)

        layout = QVBoxLayout()

        # ======================
        # TITULO
        # ======================

        titulo = QLabel(
            "♻ Resultado de la clasificación"
        )

        titulo.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
            color:white;
            padding:10px;
        """)

        layout.addWidget(titulo)

        # ======================
        # CARD PRINCIPAL
        # ======================

        self.card_objeto = QFrame()

        self.card_objeto.setStyleSheet("""
            background-color:#0f172a;
            border:1px solid #334155;
            border-radius:20px;
        """)

        objeto_layout = QVBoxLayout()

        self.icono_objeto = QLabel("♻")

        self.icono_objeto.setAlignment(
            Qt.AlignCenter
        )

        self.icono_objeto.setStyleSheet("""
            font-size:60px;
        """)

        self.objeto_label = QLabel("---")

        self.objeto_label.setAlignment(
            Qt.AlignCenter
        )

        self.objeto_label.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            color:white;
        """)

        self.categoria_label = QLabel("---")

        self.categoria_label.setAlignment(
            Qt.AlignCenter
        )

        self.categoria_label.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
            color:#22c55e;
            padding:8px;
        """)

        objeto_layout.addWidget(
            self.icono_objeto
        )

        objeto_layout.addWidget(
            self.objeto_label
        )

        objeto_layout.addWidget(
            self.categoria_label
        )

        self.card_objeto.setLayout(
            objeto_layout
        )

        layout.addWidget(
            self.card_objeto
        )

        # ======================
        # FILA CENTRAL
        # ======================

        fila = QHBoxLayout()

        # Confianza

        confianza_card = QFrame()

        confianza_card.setStyleSheet("""
            background-color:#0f172a;
            border:1px solid #334155;
            border-radius:20px;
        """)

        confianza_layout = QVBoxLayout()

        lbl_conf = QLabel(
            "Confianza"
        )

        lbl_conf.setStyleSheet("""
            color:#94a3b8;
            font-size:14px;
        """)

        self.indicador = (
            IndicadorConfianza()
        )

        confianza_layout.addWidget(
            lbl_conf
        )

        confianza_layout.addWidget(
            self.indicador
        )

        confianza_card.setLayout(
            confianza_layout
        )

        # Categoria

        categoria_card = QFrame()

        categoria_card.setStyleSheet("""
            background-color:#0f172a;
            border:1px solid #334155;
            border-radius:20px;
        """)

        categoria_layout = QVBoxLayout()

        titulo_cat = QLabel(
            "Categoría"
        )

        titulo_cat.setStyleSheet("""
            color:#94a3b8;
            font-size:14px;
        """)

        self.descripcion_categoria = QLabel(
            "---"
        )

        self.descripcion_categoria.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
            color:white;
        """)

        categoria_layout.addWidget(
            titulo_cat
        )

        categoria_layout.addWidget(
            self.descripcion_categoria
        )

        categoria_card.setLayout(
            categoria_layout
        )

        fila.addWidget(
            confianza_card
        )

        fila.addWidget(
            categoria_card
        )

        layout.addLayout(
            fila
        )

        # ======================
        # CONTENEDOR
        # ======================

        self.card_contenedor = QFrame()

        self.card_contenedor.setStyleSheet("""
            background-color:#13281d;
            border:2px solid #22c55e;
            border-radius:20px;
        """)

        cont_layout = QVBoxLayout()

        titulo_cont = QLabel(
            "🗑 Contenedor sugerido"
        )

        titulo_cont.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        self.contenedor_label = QLabel(
            "---"
        )

        self.contenedor_label.setStyleSheet("""
            font-size:26px;
            font-weight:bold;
            color:#22c55e;
        """)

        self.descripcion_contenedor = QLabel(
            ""
        )

        self.descripcion_contenedor.setStyleSheet("""
            font-size:15px;
            color:white;
        """)

        cont_layout.addWidget(
            titulo_cont
        )

        cont_layout.addWidget(
            self.contenedor_label
        )

        cont_layout.addWidget(
            self.descripcion_contenedor
        )

        self.card_contenedor.setLayout(
            cont_layout
        )

        layout.addWidget(
            self.card_contenedor
        )

        layout.addStretch()

        self.setLayout(layout)

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

        iconos = {
            "basura_domestica": "🗑",
            "botella_plastico": "🧴",
            "envase_carton": "📦",
            "metalico": "🥫",
            "papel_carton": "📄",
            "vidrio": "🍾"
        }

        self.objeto_label.setText(
            nombres[clase]
        )

        self.icono_objeto.setText(
            iconos[clase]
        )

        self.indicador.set_valor(
            confianza
        )

        if categoria == "RECICLABLE":

            self.categoria_label.setText(
                "RECICLABLE ♻"
            )

            self.descripcion_categoria.setText(
                "Puede ser reciclado"
            )

            self.contenedor_label.setText(
                "🟢 VERDE"
            )

            self.descripcion_contenedor.setText(
                "Depositar en reciclables"
            )

        else:

            self.categoria_label.setText(
                "NO RECICLABLE"
            )

            self.descripcion_categoria.setText(
                "Desecho común"
            )

            self.contenedor_label.setText(
                "🔴 ROJO"
            )

            self.descripcion_contenedor.setText(
                "Depositar en basura común"
            )