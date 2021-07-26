from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Signal, QTimer
import sys
from datetime import datetime


class Clock(QWidget):
    clock_updated = Signal()

    def __init__(self):
        super(Clock, self).__init__()
        self.current_time = datetime.now()

        self.timer = QTimer()
        self.timer.timeout.connect(self.set_current_time)
        self.timer.start(1000)

    def set_current_time(self):
        self.current_time = datetime.now()
        self.clock_updated.emit()


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.resize(300, 300)

        self.clock = Clock()
        self.clock.clock_updated.connect(self.print_time)

    def print_time(self):
        print(self.clock.current_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = OtherWindow()
    win.show()

    app.exec()