# 스타일 변경 + 현재까지 학습한 내용 적용

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyApp(QMainWindow):


    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()


    def initUI(self):

        exitAction = QAction(QIcon('image\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False) 
        filemenu = menubar.addMenu('&File') 
        filemenu.addAction(exitAction)


        btn = QPushButton('Quit', self)
        btn.setToolTip('<b>Quit</b>')
        btn.move(200, 200)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        btn2 = QPushButton('Button', self)
        btn2.setToolTip('<b>Button</b>')
        btn2.move(400, 200)
        btn2.resize(btn.sizeHint())
        btn2.clicked.connect(QCoreApplication.instance().quit)


        label_red = QLabel('Red')
        label_green = QLabel('green')
        label_blue = QLabel('blue')

        label_red.setStyleSheet('color: red; border-style: solid; border-width: 2px; border-color: #FA8072; border-radius: 3px')
        label_green.setStyleSheet('color: green; background-color: #7FFFD4')
        label_blue.setStyleSheet('color: blue; border-style: dashed; border-width: 3px; border-color: #1E90FF')
        # ;(semicolon 세미콜론)은 같은 줄에 여러 인자를 넣고 싶을 때, 구분을 위해 사용.


        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.addWidget(label_red)
        vbox.addWidget(label_green)
        vbox.addWidget(label_blue)

        self.setCentralWidget(widget)
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setWindowTitle('Total_Test_Ver')
        self.setWindowIcon(QIcon('image\instagram_logo.jfif'))
        self.resize(500,500)
        self.center()
        

    def center(self): 
        qr = self.frameGeometry() 
        cp = QDesktopWidget().availableGeometry().center() 
        qr.moveCenter(cp) 
        self.move(qr.topLeft()) 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

