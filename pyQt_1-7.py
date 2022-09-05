# 툴 바

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        editAction = QAction(QIcon('edit.png'), 'Edit', self)
        editAction.setShortcut('Ctrl+W')
        editAction.setStatusTip('Edit application')

        saveAction = QAction(QIcon('save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+E')
        saveAction.setStatusTip('Save application')

        self.statusBar()

        self.toolbar = self.addToolBar('Exit'+'Edit'+'Save')


        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(editAction)
        self.toolbar.addAction(saveAction)


        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())