# layout

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 기본 레이아웃
        self.setWindowTitle('QAC Analysis Results/Diagnostics')
        self.resize(1600,800)

        # 툴바, 각 내용별 아이콘, 이벤트 트리거 반영 필요
        checkAction1 = QAction(QIcon('check.png'), 'check1', self)
        checkAction1.triggered.connect(qApp.beep())

        self.toolbar = self.addToolBar('check1')
        self.toolbar.addAction(checkAction1)













        self.show()






# 고정_main

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())