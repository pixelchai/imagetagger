from qtpy import QtWidgets, QtGui
from qtpy.QtCore import Qt, QTimer

class Tagger(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ImageTagger")

        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.resize(960, 540)
        self.center()

    def center(self):
        """
        centres the window on the active screen
        """
        # https://stackoverflow.com/a/55172738/5013267
        frame_gm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        frame_gm.moveCenter(QtWidgets.QApplication.desktop().screenGeometry(screen).center())
        self.move(frame_gm.topLeft())