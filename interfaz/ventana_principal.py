from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QLabel
)

from PyQt5.QtCore import QTimer

from camara_ia import CamaraIA

from interfaz.componentes.panel_webcam import PanelWebcam
from interfaz.componentes.panel_resultados import (
    PanelResultados
)


class VentanaPrincipal(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "EcoVision"
        )

        self.resize(1200, 700)

        self.camara = CamaraIA()

        self.setStyleSheet("""
            QWidget{
                background-color:#0f172a;
                color:white;
                font-family:Segoe UI;
            }
        """)

        self.webcam = PanelWebcam()

        self.resultados = PanelResultados()

        self.crear_ui()

        self.webcam.btn_iniciar.clicked.connect(
        self.iniciar_camara
        )

        self.webcam.btn_detener.clicked.connect(
        self.detener_camara
        )

        self.resultados.archivo_soltado.connect(
            self.procesar_imagen_archivo
        )

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.actualizar_video
        )

        self.timer.start(100)

    def crear_ui(self):

        layout_principal = QHBoxLayout()

        layout_principal.setSpacing(20)

        layout_principal.setContentsMargins(
            15,
            15,
            15,
            15
        )

        contenido = QVBoxLayout()

        contenido.setSpacing(20)

        header = QFrame()

        header.setFixedHeight(100)

        header.setStyleSheet("""
            background-color:#111827;
            border-radius:12px;
        """)

        header_layout = QVBoxLayout()

        titulo = QLabel(
            "♻ EcoVision"
        )

        titulo.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            color:#22c55e;
        """)

        subtitulo = QLabel(
            "Sistema Inteligente de Clasificación de Residuos"
        )

        subtitulo.setStyleSheet("""
            font-size:14px;
            color:#94a3b8;
        """)

        header_layout.addWidget(
            titulo
        )

        header_layout.addWidget(
            subtitulo
        )

        header.setLayout(
            header_layout
        )

        contenido.addWidget(
            header
        )

        panel = QHBoxLayout()

        panel.addWidget(
            self.webcam,
            3
        )

        panel.addWidget(
            self.resultados,
            1
        )

        contenido.addLayout(
            panel
        )

        layout_principal.addLayout(
            contenido
        )

        self.setLayout(
            layout_principal
        )

    def actualizar_video(self):

        frame, clase, categoria, confianza = (
            self.camara.obtener_frame()
        )

        if frame is None:
            return

        self.webcam.actualizar_frame(
            frame
        )

        self.resultados.actualizar_datos(
            clase,
            categoria,
            confianza
        )

    def iniciar_camara(self):

        if not self.timer.isActive():

            self.timer.start(100)


    def detener_camara(self):

        if self.timer.isActive():

            self.timer.stop()

    def procesar_imagen_archivo(self, ruta_archivo):
        
        # Detener la cámara automáticamente
        if self.timer.isActive():
            self.timer.stop()
        
        frame, clase, categoria, confianza = (
            self.camara.procesar_imagen_archivo(ruta_archivo)
        )
        
        if frame is not None:
            
            self.webcam.actualizar_frame(frame)
            
            self.resultados.actualizar_datos(
                clase,
                categoria,
                confianza
            )
    
    def closeEvent(self, event):

        self.camara.liberar()

        event.accept()