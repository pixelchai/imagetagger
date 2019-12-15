from qtpy import QtWidgets, QtGui
from qtpy.QtWidgets import QSizePolicy
from qtpy.QtCore import Qt

class CentralWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        self.setSizePolicy(size_policy)

        self.image_label = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(1)
        self.image_label.setSizePolicy(size_policy)
        self.image_label.setPixmap(QtGui.QPixmap("res/loading.png")
                                   .scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.image_label, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.button_holder = QtWidgets.QWidget(self)
        self.button_holder.layout = QtWidgets.QHBoxLayout(self.button_holder)

        btn = QtWidgets.QPushButton(self.button_holder)
        btn.setText("wow")
        self.button_holder.layout.addWidget(btn)

        btn = QtWidgets.QPushButton(self.button_holder)
        btn.setText("wow2")
        self.button_holder.layout.addWidget(btn)

        self.layout.addWidget(self.button_holder, 0, Qt.AlignBottom)


class Tagger(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ImageTagger")

        self.central_widget = CentralWidget(self)
        self.setCentralWidget(self.central_widget)
