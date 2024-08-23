from sys import argv
from PySide6.QtWidgets import QApplication

from windows.main_window import ChatForm

if __name__ == '__main__':
    app = QApplication(argv)
    my_pyqt_form = ChatForm()
    my_pyqt_form.show()
    app.exec()
