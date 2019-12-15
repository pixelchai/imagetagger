from qtpy import QtWidgets, QtGui
from qtpy.QtWidgets import QSizePolicy
from qtpy.QtCore import Qt
from providers import Provider
from functools import partial
import string


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

        self.layout.addWidget(self.button_holder, 0, Qt.AlignBottom)


class Tagger(QtWidgets.QMainWindow):
    def __init__(self, provider: Provider, classes=None, copy=True):
        super().__init__()

        self.provider = provider
        self.copy = copy
        if classes is None:
            self.classes = ["True", "False"]
        else:
            self.classes = classes

        self.setWindowTitle("ImageTagger")
        self.central_widget = CentralWidget(self)
        self.setCentralWidget(self.central_widget)

        self._add_buttons()

    @staticmethod
    def _get_shortcut(i):
        if i < 10:
            return str((i + 1) % 10)
        return string.ascii_letters[i-10]

    def _add_buttons(self):
        for i, class_ in enumerate(self.classes):
            meth = partial(self.button_clicked, i)

            key = self._get_shortcut(i)
            btn = QtWidgets.QPushButton(self.central_widget.button_holder)
            btn.setText("{} [{}]".format(class_, key))
            btn.clicked.connect(meth)

            shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(key), self)
            shortcut.activated.connect(meth)

            self.central_widget.button_holder.layout.addWidget(btn)

    def button_clicked(self, i):
        print(i)
