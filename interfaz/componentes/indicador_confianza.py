from PyQt5.QtWidgets import QWidget

from PyQt5.QtGui import (
    QPainter,
    QPen,
    QColor,
    QFont
)

from PyQt5.QtCore import Qt


class IndicadorConfianza(QWidget):

    def __init__(self):

        super().__init__()

        self.valor = 0

        self.setMinimumSize(
            180,
            180
        )

    def set_valor(self, valor):

        self.valor = valor

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )

        ancho = self.width()
        alto = self.height()

        margen = 25

        tamaño = min(
            ancho,
            alto
        ) - margen

        x = (ancho - tamaño) // 2
        y = (alto - tamaño) // 2

        pen_fondo = QPen(
            QColor("#1e293b"),
            14
        )

        painter.setPen(
            pen_fondo
        )

        painter.drawEllipse(
            x,
            y,
            tamaño,
            tamaño
        )

        if self.valor >= 80:

            color = "#22c55e"

        elif self.valor >= 50:

            color = "#facc15"

        else:

            color = "#ef4444"

        pen_progreso = QPen(
            QColor(color),
            14
        )

        pen_progreso.setCapStyle(
            Qt.RoundCap
        )

        painter.setPen(
            pen_progreso
        )

        angulo = int(
            360 * self.valor / 100
        )

        painter.drawArc(
            x,
            y,
            tamaño,
            tamaño,
            90 * 16,
            -angulo * 16
        )

        painter.setPen(
            QColor("white")
        )

        fuente = QFont()

        fuente.setPointSize(18)

        fuente.setBold(True)

        painter.setFont(
            fuente
        )

        painter.drawText(
            self.rect(),
            Qt.AlignCenter,
            f"{self.valor:.1f}%"
        )