import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPixmap, QPainter


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.states = []
        self.window_width, self.window_height = 800, 600
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.pix = QPixmap(self.rect().size())
        self.pix.fill(Qt.GlobalColor.white)

        self.begin, self.destination = QPoint(), QPoint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.GlobalColor.black)
        painter.drawPixmap(QPoint(), self.pix)

        if not self.begin.isNull() and not self.destination.isNull():
            painter.drawLine(self.begin, self.destination)

    def mousePressEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            for item in self.states:
                if (item["posx"] <= event.pos().x() <= item["posx"]+40) and (item["posy"] <= event.pos().y() <= item["posy"]+40):
                    self.begin.setX(item["posx"] + 20)
                    self.begin.setY(item["posy"] + 20)
                    self.destination = self.begin
                    self.update()
                    break

        if event.button() == Qt.MouseButton.RightButton:
            label = QLabel("q"+str(len(self.states)),self)
            label.move(event.pos().x() - 20, event.pos().y() - 20)
            label.resize(40, 40)
            label.setStyleSheet("""border: 1px solid;
                                        border-radius: 20px;background-color: yellow;color : black;""")
            label.show()
            self.states.append({"name":"q"+str(len(self.states)),"obj":self.label,"posx": event.pos().x() - 20,"posy": event.pos().y() - 20})

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.destination = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() & Qt.MouseButton.LeftButton:
            for item in self.states:
                if (item["posx"] <= event.pos().x() <= item["posx"]+40) and (item["posy"] <= event.pos().y() <= item["posy"]+40):
                    painter = QPainter(self.pix)
                    self.destination.setX(item["posx"] + 20)
                    self.destination.setY(item["posy"] + 20)
                    painter.drawLine(self.begin, self.destination)

                    break

            self.begin, self.destination = QPoint(), QPoint()
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')
