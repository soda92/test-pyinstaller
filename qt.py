from PyQt6 import QtCore
import sys


class Main(QtCore.QObject):
    def __init__(self) -> None:
        super().__init__()
        print("Hello World")


def main():
    app = QtCore.QCoreApplication(sys.argv)
    Main()
    QtCore.QTimer.singleShot(0, app.exit)
    app.exec()


if __name__ == "__main__":
    main()
