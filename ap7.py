from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLabel, QPushButton 
from PySide6.QtGui import QPixmap, QMovie

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Aplicacion con entrada de datos")
        label = QLabel("hola hola", self)
        label.setGeometry( 10, 20, 100, 20 )
        input=QLineEdit(self)
        input.setMaxLength(50)
        
        input.resize(100,input.size().height())

        # input.setPlaceholderText("Ingrese su nombre")
        # input.setReadOnly(True)
        # input.setText("Texto de lectura")
        # input.returnPressed.connect(lambda:self.return_pressed(input))
        # input.selectionChanged.connect(lambda:self.selection_changed(input))
        input.setGeometry( 60, 60, 60, 60)
        # input.textChanged.connect(label.setText)
        input.textEdited.connect(label.setText)
        #boton de changed///////////////////
        button = QPushButton ("poner texto", self)
        button.move (10, 70)
        button.clicked.connect(lambda: input.setText("sin editar"))
    def return_pressed(self, input):
        print("return pressed")
        input.setText ("BOOM!")
    def selection_changed (self, input):
        print ("selected changed")
        input.setText (f"texto seleccionado: {input.selectedText()}")
        #label///////////////////////////////////////////////////////////////////////
    
if __name__=="__main__":
    app=QApplication()
    window=MainWindow()
    window.show()
    app.exec()