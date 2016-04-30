import sys
from PySide import QtGui

class Window(QtGui.QMainWindow):
  def __init__(self):
    super(Window,self).__init__()
    self.initUI()
  def initUI(self):
    self.setGeometry(200,500,400,400)
    self.setWindowTitle("A Grid Layout")
    l1 = QtGui.QLabel("Label 1")
    l2 = QtGui.QLabel("Label 2")
    l3 = QtGui.QLabel("Label 3")
    le1 = QtGui.QLineEdit()
    grid = QtGui.QGridLayout()
    grid.setSpacing(10)
    grid.addWidget(l1,1,0)#widget,row,column
    grid.addWidget(l2,2,0)
    grid.addWidget(l3,3,0)
    grid.addWidget(le1,4,0,1,2)#row,column span

    centralWidget = QtGui.QWidget()
    centralWidget.setLayout(grid)
    self.setCentralWidget(centralWidget)

    self.show()

def main():
  app = QtGui.QApplication(sys.argv)
  win = Window()
  exit(app.exec_())

if __name__ == "__main__":
  main()