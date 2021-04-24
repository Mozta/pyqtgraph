from ventana_ui import *
import pyqtgraph as pg
from random import randint

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        #self.plot([1,2,3,4,5,6,7,8,9,10], [45,25,56,34,67,23,67,34,63,78],'temp','hora')

        self.x = list(range(100))
        self.y = [randint(0,100) for _ in range(100)]
        self.plot(self.x, self.y,'temp','hora')

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def plot(self, x, y, lbl_x, lbl_y):
        self.graphWidget.setBackground('w')
        pen = pg.mkPen(color=(255,0,0), width=2)
        self.graphWidget.setTitle("Gráfica 1", color='b', size="24pt")

        style = {'color':'r', 'font-size':'22px'}
        self.graphWidget.setLabel('left', lbl_y, **style)
        self.graphWidget.setLabel('bottom', lbl_x, **style)

        self.data_line = self.graphWidget.plot(x,y, pen=pen)

    def update_plot(self):
        self.x.pop(0)
        self.x.append(self.x[-1] + 1)

        self.y.pop(0)
        self.y.append(randint(0,100))

        self.data_line.setData(self.x, self.y)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()