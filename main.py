import qtpy
from qtpy import QtWidgets
import ui

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main_window = ui.Tagger()
    main_window.show()
    app.exec_()

