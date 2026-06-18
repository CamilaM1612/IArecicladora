from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog
)

from PyQt5.QtCore import pyqtSignal

import qtawesome as qta

from interfaz.componentes.resultado_objeto import (
    ResultadoObjeto
)

from interfaz.componentes.resultado_categoria import (
    ResultadoCategoria
)

from interfaz.componentes.resultado_contenedor import (
    ResultadoContenedor
)

from interfaz.componentes.indicador_confianza import (
    IndicadorConfianza
)


class PanelResultados(QFrame):

    archivo_soltado = pyqtSignal(str)

    def __init__(self):

        super().__init__()

        self.setFixedWidth(450)

        self.setStyleSheet("""
            background-color:#111827;
            border-radius:20px;
        """)

        layout = QVBoxLayout()

        titulo = QLabel(
            "Resultado de la clasificación"
        )

        titulo.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
            color:white;
        """)

        layout.addWidget(
            titulo
        )

        self.resultado_objeto = (
            ResultadoObjeto()
        )

        layout.addWidget(
            self.resultado_objeto
        )

        fila = QHBoxLayout()

        confianza_card = QFrame()

        confianza_card.setStyleSheet("""
            background-color:#0f172a;
            border:1px solid #334155;
            border-radius:18px;
        """)

        confianza_layout = QVBoxLayout()

        lbl = QLabel(
            "Confianza"
        )

        lbl.setStyleSheet("""
            color:#94a3b8;
            font-size:13px;
            border:none;
            background:transparent;
        """)

        self.indicador = (
            IndicadorConfianza()
        )

        confianza_layout.addWidget(
            lbl
        )

        confianza_layout.addWidget(
            self.indicador
        )

        confianza_card.setLayout(
            confianza_layout
        )

        self.resultado_categoria = (
            ResultadoCategoria()
        )

        fila.addWidget(
            confianza_card
        )

        fila.addWidget(
            self.resultado_categoria
        )

        layout.addLayout(
            fila
        )

        self.resultado_contenedor = (
            ResultadoContenedor()
        )

        layout.addWidget(
            self.resultado_contenedor
        )

        layout.addStretch()

        # ======================
        # BOTÓN DRAG AND DROP
        # ======================

        self.btn_subir_foto = QPushButton("📂 Subir Foto")

        self.btn_subir_foto.setStyleSheet("""
            QPushButton{
                background-color:#0f172a;
                color:#94a3b8;
                border:2px solid #64748b;
                padding:15px;
                border-radius:12px;
                font-size:14px;
            }

            QPushButton:hover{
                color:white;
                border:2px solid #94a3b8;
            }

            QPushButton:pressed{
                background-color:#1e293b;
            }
        """)

        self.btn_subir_foto.setFixedHeight(60)

        self.btn_subir_foto.clicked.connect(
            self.abrir_dialogo_archivo
        )

        layout.addWidget(
            self.btn_subir_foto
        )

        self.setLayout(
            layout
        )

        self.setAcceptDrops(True)

    def actualizar_datos(
        self,
        clase,
        categoria,
        confianza
    ):

        nombres = {
            "basura_domestica": "Basura Doméstica",
            "botella_plastico": "Botella Plástica",
            "metalico": "Metálico",
            "papel_carton": "Papel y Cartón",
            "vidrio": "Vidrio",
            "organico": "Orgánico"
        }

        iconos = {
            "basura_domestica": qta.icon(
                "fa5s.trash",
                color="#ef4444"
            ),

            "botella_plastico": qta.icon(
                "fa5s.wine-bottle",
                color="#eab308"
            ),

            "metalico": qta.icon(
                "fa5s.cube",
                color="#eab308"
            ),

            "papel_carton": qta.icon(
                "fa5s.file",
                color="#3b82f6"
            ),

            "vidrio": qta.icon(
                "fa5s.wine-bottle",
                color="#22c55e"
            ),

            "organico": qta.icon(
                "fa5s.apple-alt",
                color="#92400e"
            )
        }

        contenedores = {

            "papel_carton": {
                "nombre": "AZUL",
                "descripcion": "Depositar papel y cartón",
                "reciclable": True
            },

            "botella_plastico": {
                "nombre": "AMARILLO",
                "descripcion": "Depositar plásticos y envases",
                "reciclable": True
            },

            "metalico": {
                "nombre": "AMARILLO",
                "descripcion": "Depositar metales y latas",
                "reciclable": True
            },

            "vidrio": {
                "nombre": "VERDE",
                "descripcion": "Depositar vidrio",
                "reciclable": True
            },

            "organico": {
                "nombre": "MARRÓN",
                "descripcion": "Depositar residuos orgánicos",
                "reciclable": True
            },

            "basura_domestica": {
                "nombre": "NEGRO",
                "descripcion": "Depositar residuos no reciclables",
                "reciclable": False
            }
        }

        self.resultado_objeto.actualizar(
            nombres[clase],
            categoria,
            iconos[clase]
        )

        self.indicador.set_valor(
            confianza
        )

        info = contenedores[clase]

        self.resultado_categoria.actualizar(
            info["reciclable"]
        )

        self.resultado_contenedor.actualizar(
            info["nombre"],
            info["descripcion"],
            info["reciclable"]
        )

    def dragEnterEvent(self, event):
        
        if event.mimeData().hasUrls():
            event.accept()
            self.btn_subir_foto.setStyleSheet("""
                QPushButton{
                    background-color:#1e293b;
                    color:white;
                    border:2px solid #60a5fa;
                    padding:15px;
                    border-radius:12px;
                    font-size:14px;
                }
            """)
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        
        self.btn_subir_foto.setStyleSheet("""
            QPushButton{
                background-color:#0f172a;
                color:#94a3b8;
                border:2px solid #64748b;
                padding:15px;
                border-radius:12px;
                font-size:14px;
            }

            QPushButton:hover{
                color:white;
                border:2px solid #94a3b8;
            }

            QPushButton:pressed{
                background-color:#1e293b;
            }
        """)

    def dropEvent(self, event):
        
        self.btn_subir_foto.setStyleSheet("""
            QPushButton{
                background-color:#0f172a;
                color:#94a3b8;
                border:2px solid #64748b;
                padding:15px;
                border-radius:12px;
                font-size:14px;
            }

            QPushButton:hover{
                color:white;
                border:2px solid #94a3b8;
            }

            QPushButton:pressed{
                background-color:#1e293b;
            }
        """)
        
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            ruta_archivo = url.toLocalFile()
            
            if ruta_archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                self.archivo_soltado.emit(ruta_archivo)
            
            event.accept()
        else:
            event.ignore()

    def abrir_dialogo_archivo(self):
        
        ruta_archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar Foto",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif);;Todos los archivos (*)"
        )
        
        if ruta_archivo:
            self.archivo_soltado.emit(ruta_archivo)