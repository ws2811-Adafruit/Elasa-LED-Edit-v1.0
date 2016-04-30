#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

import sys,time
from PySide import QtCore,QtGui
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QLabel,QToolTip,QFont,QMessageBox,QDesktopWidget
from PySide.QtGui import QApplication, QWidget, QIcon,QPushButton,QImageReader
from PySide.QtGui import  QMainWindow, QStatusBar,QTextEdit,QAction, QIcon, QKeySequence
from PySide.QtGui import *
from PySide.QtCore import *

import chooseoption

class Form(QDialog):
 def __init__(self, parent = None):
    super(Form,self).__init__(parent)

    self.usernamelabel = QLabel("Username : ")
    self.passwordlabel = QLabel("Password : ")
    self.username = QLineEdit()
    self.password = QLineEdit()
    self.okbutton = QPushButton("Login")
    self.username.setPlaceholderText("Enter Username Here")
    self.password.setPlaceholderText("Enter Password Here")

    layout = QGridLayout()
    layout.addWidget(self.usernamelabel,0,0)
    layout.addWidget(self.passwordlabel,1,0)
    layout.addWidget(self.username,0,1)
    layout.addWidget(self.password,1,1)
    layout.addWidget(self.okbutton)
    self.setLayout(layout)

    self.usernamelist = ['priyank','stupendo','ayaan']
    self.passwordlist = ['priyank','stupendo','ayaan']

    self.connect(self.okbutton, SIGNAL("clicked()"),self.loginfunction)

 def loginfunction(self):
    usernamestatus = False
    usernameindex = -1
    passwordstatus = False
    passwordindex = -1
    for currentusername in range(len(self.usernamelist)):
        if self.passwordlist[currentusername] == self.username.text():
            usernamestatus = True
            usernameindex = self.usernamelist.index(self.passwordlist[currentusername])

    for currentpassword in range(len(self.passwordlist)):
        if self.usernamelist[currentpassword] ==self.password.text():
            passwordstatus = True
            passwordindex = self.passwordlist.index(self.usernamelist[currentpassword])

    if usernamestatus == True and passwordstatus ==True and usernameindex == passwordindex:
        self.hide()
        w2 = chooseoption.Form1(self)
        w2.show()


    else:
        self.msgBox = QMessageBox()
        self.msgBox.setText("Bloody Hacker!!!")
        self.msgBox.exec_()




class W1(QWidget):
    def __init__(self, parent=None):
        super(W1, self).__init__(parent)
        self.btn = QPushButton('Click1')

        vb = QVBoxLayout()
        vb.addWidget(self.btn)
        self.setLayout(vb)

        self.btn.clicked.connect(self.fireupWindows2)

    def fireupWindows2(self):
        w2 = W2()
        if w2.exec_():
            self.w3 = W3()
            self.w3.show()

class W2(QDialog):
    def __init__(self, parent=None):
        super(W2, self).__init__(parent)

        self.btn = QPushButton('Click2')

        vb = QVBoxLayout()
        vb.addWidget(self.btn)
        self.setLayout(vb)

        self.btn.clicked.connect(self.fireupWindows3)

    def fireupWindows3(self):
        self.accept()

class W3(QWidget):
    def __init__(self, parent=None):
        super(W3, self).__init__(parent)
        self.resize(300, 300)
        self.btn = QLabel('The Last Window')

        vb = QVBoxLayout()
        vb.addWidget(self.btn)
        self.setLayout(vb)

class MyWorkerThread(QtCore.QThread):
    message = QtCore.Signal(str)

    def __init__(self, id, parent=None):
        super(MyWorkerThread, self).__init__(parent)
        self.id = id

    def run(self):
        for i in range(10):
            self.message.emit("%d: %d" % (self.id, i))
            time.sleep(0.2)
class SampleWindow(QMainWindow):
 """ Our main window class
 """
 def __init__(self,fileName=None):
    """ Constructor Function
    """
    # QWidget.__init__(self)
    # self.setWindowTitle("Icon Sample")
    # self.setGeometry(300, 300, 200, 150)
    QMainWindow.__init__(self)
    self.setWindowTitle("Icon Sample")
    self.setGeometry(300, 300, 200, 150)
    QToolTip.setFont(QFont("Decorative", 8, QFont.Bold))
    self.setToolTip('Our Main Window')
    self.icon='C:\Users\Hamed\Documents\soheil sites image\imageedit__9411602959.gif'
    self.textEdit = QTextEdit()
    self.setCentralWidget(self.textEdit)
    self.fileName = None
    self.filters = "Text files (*.txt)"

    openFile = QAction(QIcon('open.png'), 'Open', self)
    openFile.setShortcut('Ctrl+O')
    openFile.setStatusTip('Open new File')
    openFile.triggered.connect(self.showDialog)
    menubar = self.menuBar()
    # fileMenu = menubar.addMenu('&File')
    # fileMenu.addAction(openFile)
    self.setGeometry(300, 300, 350, 300)
    self.setWindowTitle('Example - File Dialog')

    # self.myNameLE = QLineEdit(self)
    # self.myAgeLE = QLineEdit(self)
    # self.myChoiceLE = QLineEdit(self)

    self.statusLabel = QLabel('Showing Progress')
    self.progressBar = QProgressBar()
    self.progressBar.setMinimum(0)
    self.progressBar.setMaximum(100)
##################@@@@@@@@@@@@@@2
    self.threads = []

    self.addWorker(MyWorkerThread(1))
    self.addWorker(MyWorkerThread(2))
#######################@@@@@@@@@@@@@
    self.show()
##########################@@@@@@@@@@
 def addWorker(self, worker):
        worker.message.connect(self.printMessage, QtCore.Qt.QueuedConnection)
        # connect the finished signal to method so that we are notified
        worker.finished.connect(self.workersFinished)
        self.threads.append(worker)

 def startWorkers(self):
        for worker in self.threads:
            worker.start()
            # no wait, no finished. you start the threads and leave.

 def workersFinished(self):
        if all(worker.isFinished() for worker in self.threads):
            # wait until all the threads finished
            QtCore.QCoreApplication.instance().quit()

 @QtCore.Slot(str)
 def printMessage(self, text):
        sys.stdout.write(text+'\n')
        sys.stdout.flush()
################################

 def openAbout(self):
    aboutDialog = QtGui.QDialog(self)
    # aboutUi = about.About_Dialog()
    # aboutUi.setupUi(aboutDialog)
    aboutDialog.show()

 def newwindow(self):
        # w = W1()
        # w.show()
        # self.hide()
        # form = Form()
        # form.show()

        w2 = chooseoption.Form1(self)
        w2.show()
        import webbrowser
        your_swf_url='E:\soheil\web_site_root\ieee\all_functions\linux server\python GUI\Double_angle_off.swf'
        webbrowser.open(your_swf_url)
        # self.wid = QWidget()
        # self.wid.resize(250, 150)
        # self.wid.setWindowTitle('NewWindow')
        # self.wid.show()
        # self.actionAbout.triggered.connect(self.openAbout)
 def retranslateUi(self, Dialog):
    Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
    self.aboutLbl.setText(QtGui.QApplication.translate("Dialog", "Mailer version 0.0.1 by .....", None, QtGui.QApplication.UnicodeUTF8))

 def showNameDialog(self):
    text, ok = QInputDialog.getText(self, 'Input Text Dialog',
    'Enter your name:')
    if ok:
        self.myNameLE.setText(str(text))

 def showDialog(self):
    fileName, _ = QFileDialog.getOpenFileName(self, "Open Text Files", "c:/", "Text files(*.txt)")
    try:
        contents = open(fileName, 'r')
        with contents:
            data = contents.read()
            self.textEdit.setText(data)
    except:
        pass

 def CreateStatusBar(self):
    """ Function to create the status bar
    """
    self.myStatusBar = QStatusBar()
    self.progressBar.setValue(10)
    self.myStatusBar.addWidget(self.statusLabel, 1)
    self.myStatusBar.addWidget(self.progressBar, 2)
    self.setStatusBar(self.myStatusBar)
 def ShowProgress(self):
    """ Function to show progress
    """
    import time
    while(self.progressBar.value() < self.progressBar.maximum()):
        self.progressBar.setValue(self.progressBar.value() + 10)
        # time.sleep(1)
    self.statusLabel.setText('Ready')
 def SetupComponents(self):
    """ Function to setup status bar, central widget, menu bar
    """
    self.myStatusBar = QStatusBar()
    self.setStatusBar(self.myStatusBar)
    self.myStatusBar.showMessage('Ready', 10000)
    self.textEdit = QTextEdit()
    self.setCentralWidget(self.textEdit)
    # self.CreateActions()
    # self.CreateMenus()
    # self.fileMenu.addAction(self.newAction)
    # self.fileMenu.addSeparator()
    # self.fileMenu.addAction(self.exitAction)
    # self.editMenu.addAction(self.copyAction)
    # self.fileMenu.addSeparator()
    # self.editMenu.addAction(self.pasteAction)
    # self.helpMenu.addAction(self.aboutAction)



    self.myStatusBar = QStatusBar()
    self.setStatusBar(self.myStatusBar)
    self.myStatusBar.showMessage('Ready', 10000)
    self.CreateActions()
    self.CreateMenus()
    self.CreateToolBar()
    self.fileMenu.addAction(self.newAction)
    self.fileMenu.addAction(self.openAction)
    self.fileMenu.addAction(self.saveAction)
    self.fileMenu.addSeparator()
    self.fileMenu.addAction(self.exitAction)
    self.editMenu.addAction(self.cutAction)
    self.editMenu.addAction(self.copyAction)
    self.editMenu.addAction(self.pasteAction)
    self.editMenu.addSeparator()
    self.editMenu.addAction(self.undoAction)
    self.editMenu.addAction(self.redoAction)
    self.editMenu.addAction(self.ss_image)

    self.editMenu.addSeparator()
    self.editMenu.addAction(self.selectAllAction)
    self.formatMenu.addAction(self.fontAction)
    self.helpMenu.addAction(self.aboutAction)
    self.helpMenu.addSeparator()
    self.helpMenu.addAction(self.aboutQtAction)
    self.mainToolBar.addAction(self.newAction)
    self.mainToolBar.addAction(self.openAction)
    self.mainToolBar.addAction(self.saveAction)
    self.mainToolBar.addSeparator()
    self.mainToolBar.addAction(self.cutAction)
    self.mainToolBar.addAction(self.copyAction)
    self.mainToolBar.addAction(self.pasteAction)
    self.mainToolBar.addSeparator()
    self.mainToolBar.addAction(self.undoAction)
    self.mainToolBar.addAction(self.redoAction)


 def openFile(self):
    self.fileName, self.filterName =QFileDialog.getOpenFileName(self)
    try:
        self.textEdit.setText(open(self.fileName).read())
    except:
        pass
    # Slots called when the menu actions are triggered
 def newFile(self):
    self.textEdit.setText('')
 def exitFile(self):
    self.close()
 def aboutHelp(self):
    QMessageBox.about(self, "About Simple Text Editor",
    "This example demonstrates the use "
    "of Menu Bar")

 def fontChange(self):
    (font, ok) = QFontDialog.getFont(QFont("Helvetica [Cronyx]", 10), self)
    if ok:
        self.textEdit.setCurrentFont(font)

 def saveFile(self):
    if self.fileName == None or self.fileName == '':
        self.fileName, self.filterName = QFileDialog.getSaveFileName(self, \
        filter=self.filters)
    if(self.fileName != ''):
        file = open(self.fileName, 'w')
        file.write(self.textEdit.toPlainText())
        self.statusBar().showMessage("File saved", 2000)
 def image_ss(self):
    from PySide import QtGui, QtCore

    import wxpython_flash_Simple_working
    hbox = QtGui.QHBoxLayout(self)
    pixmap = QtGui.QPixmap('C:\Users\Hamed\Pictures\LED\led.jpg')

    lbl = QtGui.QLabel(self)
    lbl.setPixmap(pixmap)

    hbox.addWidget(lbl)
    self.setLayout(hbox)

    self.setGeometry(300, 300, 280, 170)
    self.setWindowTitle('Red Rock')

    self.show()


    # from PIL import Image
    # from PySide.QtGui import QImage, QImageReader, QLabel, QPixmap, QApplication
    #
    # im = Image.open('C:\Users\Hamed\Documents\soheil sites image\imageedit__9411602959.gif')
    # data = im.tostring('raw')
    #
    ##app = QApplication([])
    ## image = QImage(data);
    # image = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    # pix = QPixmap.fromImage(image)
    # lbl = QLabel()
    # lbl.setPixmap(pix)
    # lbl.show()
 def image_ss_main(self):
    from PySide import QtGui, QtCore
    hbox = QtGui.QHBoxLayout(self)
    pixmap = QtGui.QPixmap('C:\Users\Hamed\Pictures\LED\led.jpg')

    lbl = QtGui.QLabel(self)
    lbl.setPixmap(pixmap)

    hbox.addWidget(lbl)
    self.setLayout(hbox)

    self.setGeometry(300, 300, 280, 170)
    self.setWindowTitle('Red Rock')

    self.show()


    # from PIL import Image
    # from PySide.QtGui import QImage, QImageReader, QLabel, QPixmap, QApplication
    #
    # im = Image.open('C:\Users\Hamed\Documents\soheil sites image\imageedit__9411602959.gif')
    # data = im.tostring('raw')
    #
    ##app = QApplication([])
    ## image = QImage(data);
    # image = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    # pix = QPixmap.fromImage(image)
    # lbl = QLabel()
    # lbl.setPixmap(pix)
    # lbl.show(
 def CreateActions(self):
    """ Function to create actions for menus
    """
    self.newAction = QAction( QIcon('new.png'), '&New',
    self, shortcut=QKeySequence.New,
    statusTip="Create a New File",
    triggered=self.newFile)
    self.exitAction = QAction( QIcon(self.icon), 'E&xit',
    self, shortcut="Ctrl+Q",
    statusTip="Exit the Application",
    triggered=self.exitFile)
    self.copyAction = QAction( QIcon('copy.png'), 'C&opy',
    self, shortcut="Ctrl+C",
    statusTip="Copy",
    triggered=self.textEdit.copy)
    self.pasteAction = QAction( QIcon('paste.png'), '&Paste',
    self, shortcut="Ctrl+V",
    statusTip="Paste",
    triggered=self.textEdit.paste)
    self.aboutAction = QAction( QIcon('about.png'), 'A&bout',
    self, statusTip="Displays info about text editor",
    triggered=self.aboutHelp)

    self.openAction = QAction( QIcon('open.png'), 'O&pen',
    self, shortcut=QKeySequence.Open,
    statusTip="Open an existing file",
    triggered=self.openFile)

    self.saveAction = QAction( QIcon('save.png'), '&Save',
    self, shortcut=QKeySequence.Save,
    statusTip="Save the current file to disk",
    triggered=self.saveFile)

    self.cutAction = QAction( QIcon('cut.png'), 'C&ut',
    self, shortcut=QKeySequence.Cut,
    statusTip="Cut the current selection to clipboard",
    triggered=self.textEdit.cut)

    self.undoAction = QAction( QIcon('undo.png'),'Undo', self,
    shortcut=QKeySequence.Undo,
    statusTip="Undo previous action",
    triggered=self.textEdit.undo)

    self.redoAction = QAction( QIcon('redo.png'),'Redo', self,
    shortcut=QKeySequence.Redo,
    statusTip="Redo previous action",
    triggered=self.textEdit.redo)

    self.selectAllAction = QAction( QIcon('selectAll.png'),
    'Select All',
    self, statusTip="Select All",
    triggered=self.textEdit.selectAll)

    self.fontAction = QAction( 'F&ont', self,
    statusTip = "Modify font properties",
    triggered = self.fontChange)

    self.aboutAction = QAction( QIcon('about.png'), 'A&bout',
    self, statusTip="Displays info about text editor",
    # triggered=self.aboutHelp)
    triggered=self.newwindow)

    self.aboutQtAction = QAction("About &Qt", self,
    statusTip="Show the Qt library's About box",
    triggered=qApp.aboutQt)

    self.ss_image = QAction("Insert &.SWF(flash)", self,
    statusTip="Show the Qt library's About box",
    triggered=self.image_ss)

    self.actionAbout = QAction("image &Qt", self,
    statusTip="Show the Qt library's About box",
    triggered=self.openAbout)


# Actual menu bar item creation
 def CreateToolBar(self):
    """ Function to create actual menu bar
    """
    self.mainToolBar = self.addToolBar('Main')
    self.mainToolBar.addAction(self.newAction)
    self.mainToolBar.addSeparator()
    self.mainToolBar.addAction(self.copyAction)
    self.mainToolBar.addAction(self.pasteAction)

# Actual menu bar item creation
 def CreateMenus(self):
    """ Function to create actual menu bar
    """
    self.fileMenu = self.menuBar().addMenu("&File")
    self.fileMenu.addSeparator()
    self.editMenu = self.menuBar().addMenu("&Edit")
    self.helpMenu = self.menuBar().addMenu("&Help")
    self.formatMenu = self.menuBar().addMenu("F&ormat")
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
    from  PySide.QtGui import QPixmap
    pixmap = QPixmap(r'C:\Users\Hamed\Pictures\LED\led.jpg')
    # appIcon = QIcon('C:\Users\Hamed\Documents\soheil sites image\imageedit__9411602959.gif')
    appIcon = QIcon(pixmap)
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
        myWindow.SetupComponents()
        myWindow.CreateToolBar()

        myWindow.CreateStatusBar()


        myWindow.show()
        myWindow.ShowProgress()

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