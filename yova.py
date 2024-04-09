from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

def getWidgetColor(color, texto, color_l="white"):
    widget = QWidget()
    label = QLabel(texto, widget)
    font = label.font()
    font.setPointSize(20)
    font.setBold(True)
    label.setFont(font)
    widget.setAutoFillBackground(True)
    palette = widget.palette()
    palette.setColor(QPalette.Window, color)
    palette.setColor(QPalette.WindowText, color_l)
    widget.setPalette(palette)
    widget.setMinimumSize(50, 30)
    return widget

class miVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_hBox()

    def setup_hBox(self):
        layout_h = QHBoxLayout()

        # Crear los layouts verticales
        layout_v1 = QVBoxLayout()
        layout_v2 = QVBoxLayout()
        layout_v3 = QVBoxLayout()

        # Configurar los widgets del primer layout vertical (izquierda)
        layout_v1.addWidget(getWidgetColor("red", "0", "white"))  # Rojo
        layout_v1.addWidget(getWidgetColor("yellow", "1", "white"))  # Amarillo
        layout_v1.addWidget(getWidgetColor("purple", "2", "white"))  # Morado

        # Configurar los widgets del segundo layout vertical (centro)
        layout_v2.addWidget(getWidgetColor("green", "3", "white"))  # Verde
        # Aquí puedes agregar otro widget si lo necesitas

        # Configurar los widgets del tercer layout vertical (derecha)
        layout_v3.addWidget(getWidgetColor("red", "4", "white"))  # Rojo
        layout_v3.addWidget(getWidgetColor("purple", "5", "white"))  # Morado
        layout_v3.addWidget(getWidgetColor("yellow", "6", "white"))  # Amarillo

        # Agregar los layouts verticales al layout horizontal
        layout_h.addLayout(layout_v1)
        layout_h.addLayout(layout_v2)
        layout_h.addLayout(layout_v3)

        self.setLayout(layout_h)


if __name__ == "__main__":
    app = QApplication([])
    window = miVentana()
    window.show()
    app.exec()
