import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QMessageBox
from grafo import G, casas, bfs_caminho, desenhar_grafo

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'CAMINHOS DE WESTEROS'
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()

        self.label = QLabel("Selecione a região inicial/casa inicial e  região destino/casa destino:", self)
        layout.addWidget(self.label)

        self.labelInicio = QLabel("Região Inicial", self)
        layout.addWidget(self.labelInicio)
        
        self.comboBoxInicio = QComboBox(self)
        self.comboBoxInicio.addItems(casas)
        layout.addWidget(self.comboBoxInicio)
        
        self.labelFim = QLabel("Região destino", self)
        layout.addWidget(self.labelFim)
        
        self.comboBoxFim = QComboBox(self)
        self.comboBoxFim.addItems(casas)
        layout.addWidget(self.comboBoxFim)

        self.button = QPushButton('CAMINHO MINIMO', self)
        self.button.clicked.connect(self.on_click)
        layout.addWidget(self.button)

        self.quit_button = QPushButton('SAIR', self)
        self.quit_button.clicked.connect(self.close)
        layout.addWidget(self.quit_button)
        
        self.setLayout(layout)
    
    def on_click(self):
        casa_inicial = self.comboBoxInicio.currentText()
        casa_final = self.comboBoxFim.currentText()

        try:
            path = bfs_caminho(G, casa_inicial, casa_final)
            print(f"Caminho mínimo de {casa_inicial} para {casa_final}: {path}")
            desenhar_grafo(path)
        except ValueError as e:
            QMessageBox.warning(self, "Erro", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro inesperado: {str(e)}")

app = QApplication(sys.argv)
ex = App()
ex.show()
sys.exit(app.exec_())
