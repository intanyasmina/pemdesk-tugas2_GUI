import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def window():
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QHBoxLayout()

    tl = QLabel(window)
    tl.setText("Kotak Angka")
    tl.move(25,50)

    for i in range (5):
        button=QPushButton(str(i+1))
        layout.addWidget(button)
        button.setGeometry(100,100,200,100)
        button.setFont(QFont('Gadugi',35))
        button.setStyleSheet("font-size: 24pt; background-color: #bdb76b; color: yellow")

    #__menentukan ukuran window, + title dan menampilkan
    window.setGeometry(100,100,200,200)
    window.setWindowTitle("PyQt Example")
    window.setLayout(layout)
    window.setStyleSheet("background-color: grey")
    window.show()
    app.exec_()
	
if __name__ == '__main__':
    window()
