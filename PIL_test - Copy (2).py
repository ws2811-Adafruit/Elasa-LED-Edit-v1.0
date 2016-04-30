#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QLabel,QToolTip,QFont,QMessageBox,QDesktopWidget
from PySide.QtGui import QApplication, QWidget, QIcon,QPushButton
from PySide.QtGui import  QMainWindow, QStatusBar,QTextEdit,QAction, QIcon, QKeySequence

class SampleWindow(QWidget):
 """ Our main window class
 """
 def __init__(self):
    """ Constructor Function
    """
    # QWidget.__init__(self)
    # self.setWindowTitle("Icon Sample")
    # self.setGeometry(300, 300, 200, 150)
    QWidget.__init__(self)
    self.setWindowTitle("Icon Sample")
    self.setGeometry(300, 300, 200, 150)
    QToolTip.setFont(QFont("Decorative", 8, QFont.Bold))
    self.setToolTip('Our Main Window')
    self.icon='C:\Users\Hamed\Documents\soheil sites image\imageedit__9411602959.gif'

# Actual menu bar item creation
 def CreateMenus(self):
    """ Function to create actual menu bar
    """
    self.fileMenu = self.menuBar().addMenu("&File")
    self.editMenu = self.menuBar().addMenu("&Edit")
    self.helpMenu = self.menuBar().addMenu("&Help")

 def setAboutButton(self):
    """ Function to set About Button
    """
    self.aboutButton = QPushButton("About", self)
    self.aboutButton.move(110, 100)
    self.aboutButton.clicked.connect(self.showAbout)
 def showAbout(self):
        """ Function to show About Box
        """
        QMessageBox.about(self.aboutButton, "About PySide",
        "PySide is a cross-platform tool for generating GUI Programs.")

 def center(self):
    """ Function to center the application
    """
    qRect = self.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qRect.moveCenter(centerPoint)
    self.move(qRect.topLeft())
 def quitApp(self):
    """ Function to confirm a message from the user
    """
    userInfo = QMessageBox.question(self, 'Confirmation',
    "This will quit the application. Do you want to Continue?",
    QMessageBox.Yes | QMessageBox.No)
    if userInfo == QMessageBox.Yes:
        myApp.quit()
    if userInfo == QMessageBox.No:
       pass
 def setIconModes(self):
    myIcon1 = QIcon( self.icon)
    myLabel1 = QLabel('sample', self)
    pixmap1 = myIcon1.pixmap(50, 50, QIcon.Active, QIcon.On)
    myLabel1.setPixmap(pixmap1)
    myIcon2 = QIcon( self.icon)
    myLabel2 = QLabel('sample', self)
    pixmap2 = myIcon2.pixmap(50, 50, QIcon.Disabled, QIcon.Off)
    myLabel2.setPixmap(pixmap2)
    myLabel2.move(50, 0)
    myIcon3 = QIcon( self.icon)
    myLabel3 = QLabel('sample', self)
    pixmap3 = myIcon3.pixmap(50, 50, QIcon.Selected, QIcon.On)
    myLabel3.setPixmap(pixmap3)
    myLabel3.move(100, 0)
 def setIcon(self):
    """ Function to set Icon
    """
    appIcon = QIcon('C:\Users\Hamed\Documents\soheil sites image\imageedit__9411602959.gif')
    self.setWindowIcon(appIcon)

 def setButton(self):
    """ Function to add a quit button
    """
    myButton = QPushButton('Quit', self)
    myButton.move(20, 100)
    # myButton.clicked.connect(myApp.quit)
    myButton.clicked.connect(self.quitApp)

if __name__ == '__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myWindow = SampleWindow()
        myWindow.setIcon()

        myWindow.setButton()
        myWindow.setIconModes()
        myWindow.center()
        myWindow.setAboutButton()
        
        myWindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
# Main Function
if __name__ == '__main2__':
    # Create the main application
    myApp = QApplication(sys.argv)
    # Create a Label and set its properties
    appLabel = QLabel()
    appLabel.setText("Hello, World!!!\n Look at my first app using PySide")
    appLabel.setAlignment(Qt.AlignCenter)
    appLabel.setWindowTitle("My First Application")
    appLabel.setGeometry(300, 300, 250, 175)
    # Show the Label
    appLabel.show()
    # Execute the Application and Exit
    myApp.exec_()
    sys.exit()