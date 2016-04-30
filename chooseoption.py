import sys
from PySide.QtGui import *
from PySide.QtCore import *

class Form1(QDialog):

 def __init__(self, parent = None):
    super(Form1,self).__init__(parent)

    self.addbutton = QPushButton("Add file in Important list")
    self.removebutton = QPushButton("Remove file from Important list")
    self.changeaddressbutton = QPushButton("Change Location of Important File")

    layout = QVBoxLayout()
    layout.addWidget(self.addbutton)
    layout.addWidget(self.removebutton)
    layout.addWidget(self.changeaddressbutton)
    self.setLayout(layout)