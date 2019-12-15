import qtpy
from qtpy import QtWidgets
import ui
from providers import FolderProvider

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    main_window = ui.Tagger(FolderProvider(r"C:\Users\ab\Pictures\clipstudio\out"))

    main_window.show()
    app.exec_()

