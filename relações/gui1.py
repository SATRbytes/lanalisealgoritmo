import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QComboBox, QLabel, QMessageBox, QInputDialog
from grafo1 import adicionar_conexao, desenhar_grafo, casas_disponiveis

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'RELAÇÕES ENTRE AS FAMÍLIAS'
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()

        self.label = QLabel("Selecione as famílias e a relação entre elas:", self)
        layout.addWidget(self.label)

        self.labelFamilia1 = QLabel("Família 1", self)
        layout.addWidget(self.labelFamilia1)
        
        self.comboBoxFamilia1 = QComboBox(self)
        self.comboBoxFamilia1.addItems(casas_disponiveis)
        layout.addWidget(self.comboBoxFamilia1)
        
        self.labelFamilia2 = QLabel("Família 2", self)
        layout.addWidget(self.labelFamilia2)
        
        self.comboBoxFamilia2 = QComboBox(self)
        self.comboBoxFamilia2.addItems(casas_disponiveis)
        layout.addWidget(self.comboBoxFamilia2)

        self.labelRelacao = QLabel("Relação", self)
        layout.addWidget(self.labelRelacao)
        
        self.comboBoxRelacao = QComboBox(self)
        self.comboBoxRelacao.addItems(["ALIADOS", "INIMIGOS", "NEUTROS"])
        layout.addWidget(self.comboBoxRelacao)

        self.buttonAdicionar = QPushButton('ADD CONEXÃO', self)
        self.buttonAdicionar.clicked.connect(self.on_click_adicionar)
        layout.addWidget(self.buttonAdicionar)

        self.buttonDesenhar = QPushButton('MOSTRAR O GRAFO', self)
        self.buttonDesenhar.clicked.connect(self.on_click_desenhar)
        layout.addWidget(self.buttonDesenhar)

        self.quit_button = QPushButton('SAIR', self)
        self.quit_button.clicked.connect(self.close)
        layout.addWidget(self.quit_button)
        
        self.setLayout(layout)
    
    def on_click_adicionar(self):
        familia_1 = self.comboBoxFamilia1.currentText()
        familia_2 = self.comboBoxFamilia2.currentText()
        relacao = self.comboBoxRelacao.currentText()

        if familia_1 == familia_2:
            QMessageBox.warning(self, "Sério isso?", "As duas familias não podem ser a mesma familia")
            return

        if not adicionar_conexao(familia_1, familia_2, relacao):
            QMessageBox.warning(self, "DE NOVO?", f"Já existe uma relação entre {familia_1} e {familia_2}.")
        else:
            QMessageBox.information(self, "FOI!!!!!!!", f"Relação entre {familia_1} e {familia_2} é {relacao}!")

    def on_click_desenhar(self):
        desenhar_grafo()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
