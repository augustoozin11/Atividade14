import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton

class JanelaPrincipal(QMainWindow):
    def _init_(self):
        super()._init_()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Janela Principal')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.nome_label = QLineEdit(self)
        self.nome_label.setPlaceholderText('Nome')
        self.layout.addWidget(self.nome_label)

        self.mensagem_label = QLineEdit(self)
        self.mensagem_label.setPlaceholderText('Mensagem')
        self.layout.addWidget(self.mensagem_label)

        self.enviar_button = QPushButton('Enviar', self)
        self.enviar_button.clicked.connect(self.abrirJanelaEnvio)
        self.layout.addWidget(self.enviar_button)

        self.display_text = QTextEdit(self)
        self.layout.addWidget(self.display_text)

        self.central_widget.setLayout(self.layout)

    def abrirJanelaEnvio(self):
        nome = self.nome_label.text()
        mensagem = self.mensagem_label.text()
        janela_envio = JanelaEnvio(nome, mensagem, self)
        janela_envio.show()

class JanelaEnvio(QWidget):
    def _init_(self, nome, mensagem, main_janela):
        super()._init_()
        self.nome = nome
        self.mensagem = mensagem
        self.main_janela = main_janela
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Janela de Envio')
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        mensagem_label = QTextEdit(self)
        mensagem_label.setPlainText(f'Nome: {self.nome}\nMensagem: {self.mensagem}')
        layout.addWidget(mensagem_label)

        enviar_button = QPushButton('Enviar para Main Janela', self)
        enviar_button.clicked.connect(self.enviarParaMain)
        layout.addWidget(enviar_button)

        self.setLayout(layout)

    def enviarParaMain(self):
        self.main_janela.display_text.append(f'Nome: {self.nome}\nMensagem: {self.mensagem}')
        self.close()

if _name_ == '_main_':
    app = QApplication(sys.argv)
    main_window = JanelaPrincipal()
    main_window.show()
    sys.exit(app.exec_())