import sys
from PyQt5.QtWidgets import QApplication, QShortcut, QTabWidget, QWidget, QLabel, QMainWindow, QFileDialog, QPushButton
from PyQt5.QtWidgets import QAction, QDoubleSpinBox, QFileDialog, QLineEdit, QSpinBox, QStatusBar, QTabWidget, QTextEdit, QToolBar, QVBoxLayout
from PyQt5.QtGui import QIcon, QFileOpenEvent, QPixmap, QKeySequence
from PyQt5.QtCore import pyqtSlot, QDir
from PyQt5 import QtGui
import os


# Create the main app class inheriting from QMainWindow
app = QApplication([])
widget = QWidget()
label = QLabel("", widget)


class Window(QMainWindow):
    #Add a constructor extending the parent window
    def __init__(self, parent=None):
        super().__init__(parent)
        widget.setWindowTitle('PyQt5 Lab')

    #creat a menu and tabs
        self.createMenu()
        self.createTabs()

    # Method adding the menu panel
    def createMenu(self):
        # Create a menu bar
        self.menu = self.menuBar()
        # Add  Files in  menu
        self.fileMenu = self.menu.addMenu("File")
        self.Tab1Menu = self.menu.addMenu("tab 1")
        self.Tab2Menu = self.menu.addMenu("tab 2")
        self.Tab3Menu = self.menu.addMenu("tab 3")
        # Extend the file menu with exit position
        self.fileMenu.addAction('Exit', self.close)
        self.Tab1Menu.addAction("Open Ctrl+O", self.upload_csv)
        self.Tab2Menu.addAction("Open Ctrl+T",  self.get_text_file)
        self.Tab2Menu.addAction("Save As Ctrl+S" , self.saveFile)
       
        self.Tab2Menu.addAction("Clear Ctrl+M", self.resetTab2)
        self.Tab3Menu.addAction("Clear Ctrl+R",  self.resetTab3)

        #shortcut
        self.openimage = QShortcut(QKeySequence("Ctrl+O"), self)
        self.openimage.activated.connect(self.upload_csv)
        self.opentext = QShortcut(QKeySequence("Ctrl+T"), self)
        self.opentext.activated.connect(self.get_text_file)
        self.cleartab2 = QShortcut(QKeySequence("Ctrl+M"), self)
        self.cleartab2.activated.connect(self.resetTab2)
        self.cleartab3 = QShortcut(QKeySequence("Ctrl+R"), self)
        self.cleartab3.activated.connect(self.resetTab3)
    #method for tabs

    def createTabs(self):

        # Create a tab widget
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.addTab(self.tab3, "Tab 3")
        #
        self.labelimage = QLabel()
        self.textEditor = QTextEdit()
        #
        self.tab1.layout = QVBoxLayout(self)
        self.tab2.layout = QVBoxLayout(self)
        self.tab3.layout = QVBoxLayout(self)
        self.widget()
#

    def widget(self):
        #for tab1
        #creat button
        self.pushButton1 = QPushButton("Import Image")
        self.pushButton1.clicked.connect(self.upload_csv)
        #inside the tab1
        self.tab1.setLayout(self.tab1.layout)
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.layout.addWidget(self.labelimage)

        #for tab2
        #create button
        self.button2 = QPushButton('Import NoteFile')
        self.button3 = QPushButton("Clear")
        self.button2.clicked.connect(self.get_text_file)
        self.button3.clicked.connect(self.textEditor.clear)
        #inside tab2
        self.tab2.setLayout(self.tab2.layout)
        self.tab2.layout.addWidget(self.button2)
        self.tab2.layout.addWidget(self.button3)
        self.tab2.layout.addWidget(self.textEditor)

        #tab3
        self.tab3.setLayout(self.tab3.layout)
        #creat button
        self.btnAdd = QPushButton("Add")
        self.btnSub = QPushButton("Subtract")
        self.btnDiv = QPushButton("Divide")
        self.btnMul = QPushButton("Multiply")
        #creat textfield
        self.txtArea1 = QLineEdit("")
        self.txtArea2 = QLineEdit("")
        self.txtArea3 = QSpinBox(self)
        #add to tab3
        #add button
        self.tab3.layout.addWidget(self.btnAdd)
        self.tab3.layout.addWidget(self.btnSub)
        self.tab3.layout.addWidget(self.btnDiv)
        self.tab3.layout.addWidget(self.btnMul)
        #add textfield
        self.tab3.layout.addWidget(self.txtArea1)
        self.tab3.layout.addWidget(self.txtArea2)
        self.tab3.layout.addWidget(self.txtArea3)
        #label
        self.label = QLabel("")
        self.label.setText("")
        self.tab3.layout.addWidget(self.label)
        ####
        self.btnAdd.setToolTip('Addition')
        self.btnAdd.clicked.connect(self.addition)
        self.btnSub.setToolTip('Subtraction')
        self.btnSub.clicked.connect(self.subtraction)
        self.btnDiv.setToolTip('Division')
        self.btnDiv.clicked.connect(self.division)
        self.btnMul.setToolTip('Multiplication')
        self.btnMul.clicked.connect(self.multiplication)

        # Attach the widget to the main window as central widget
        self.setCentralWidget(self.tabs)

    def resetTab3(self):
        self.txtArea1.clear()
        self.txtArea2.clear()
        self.txtArea3.clear()

    def resetTab2(self):
        self.textEditor.clear()

    #methdo to add

    def addition(self):
        self.num1 = int(self.txtArea1.text())
        self.num2 = int(self.txtArea2.text())
        self.num3 = int(self.txtArea3.text())
        self.label.setFixedWidth(200)
        self.label.setText("Addition: "+str(self.num1 + self.num2 + self.num3))

    #method to sub
    def subtraction(self):
        self.num1 = int(self.txtArea1.text())
        self.num2 = int(self.txtArea2.text())
        self.num3 = int(self.txtArea3.text())
        self.label.setFixedWidth(200)
        self.label.setText(
            "Subtraction: "+str(self.num1 - self.num2 - self.num3))

    #method to multi
    def multiplication(self):
        self.num1 = int(self.txtArea1.text())
        self.num2 = int(self.txtArea2.text())
        self.num3 = int(self.txtArea3.text())
        self.label.setFixedWidth(200)
        self.label.setText("multiplication: " +
                           str(self.num1 * self.num2 * self.num3))

    #method to divide
    def division(self):
        self.num1 = int(self.txtArea1.text())
        self.num2 = int(self.txtArea2.text())
        self.num3 = int(self.txtArea3.text())
        self.label.setFixedWidth(200)
        self.label.setText("Division: "+str(self.num1 / self.num2 / self.num3))

    #method for desplay image
    def upload_csv(self):

        file_name, _ = QFileDialog.getOpenFileName(
            self, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif *.png)")
        self.labelimage.setPixmap(QPixmap(file_name))

    def saveFile(self):
        filename = QFileDialog.getSaveFileName(
            self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.textEditor.toPlainText()
            f.write(my_text)

    #method for display notepade
    def get_text_file(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            file_name = dialog.selectedFiles()

        if file_name[0].endswith('.txt'):
            with open(file_name[0], 'r') as f:
                data = f.read()
                self.textEditor.setPlainText(data)
                f.close()
        else:
            pass

# Run the window


widget = Window()
widget.show()
app.exec_()
