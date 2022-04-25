from PyQt6 import QtCore
import sys


class Main(QtCore.QObject):
    def __init__(self) -> None:
        super().__init__()
        print("Hello World")


def main():
    from pathlib import Path

    CURRENT = Path(__file__).resolve().parent
    data = CURRENT.joinpath("data").joinpath("data.txt")
    with open(str(data), mode="r", encoding="utf-8") as f:
        print(f.read())
    
    if len(sys.argv) >= 2:
        breakpoint()
    dll = CURRENT.joinpath("pdist").joinpath("libapp.dll")
    import ctypes

    dll = ctypes.CDLL(str(dll))
    dll.print_hello()

    from data import func

    func.hello_data()

    app = QtCore.QCoreApplication(sys.argv)
    Main()
    QtCore.QTimer.singleShot(0, app.exit)
    app.exec()


if __name__ == "__main__":
    main()
