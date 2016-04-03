from PyQt4 import QtCore, QtGui
import sys
import subprocess

class PIWindow(QtGui.QWidget):
    def __init__(self):
        super(PIWindow, self).__init__()
        self.pathRoot = QtCore.QDir.homePath()
        self.model = QtGui.QFileSystemModel(self)
        self.model.setRootPath(self.pathRoot)
        self.indexRoot = self.model.index(self.model.rootPath())
        self.treeView = QtGui.QTreeView(self)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.indexRoot)
        self.treeView.clicked.connect(self.on_treeView_clicked)
        self.labelFileName = QtGui.QLabel(self)
        self.lineEditFileName = QtGui.QLineEdit(self)
        self.labelFilePath = QtGui.QLabel(self)
        self.labelFilePath.setText("File Path:")
        self.lineEditFilePath = QtGui.QLineEdit(self)
        self.installButton = QtGui.QPushButton('Install', self)
        self.installButton.clicked.connect(self.install_package)
        self.aboutButton = QtGui.QPushButton('About', self)
        self.aboutButton.clicked.connect(self.about)
        self.githubLabel = QtGui.QLabel()
        self.githubLabel.setText('''View source code on <a href='https://github.com/nicat97/packageinstaller'>GitHub!</a>''')
        self.githubLabel.setOpenExternalLinks(True)
        self.labelFileName.setText("File Name:")
        self.setWindowTitle("Package Installer")
        self.resize(550, 250)
        self.move(200, 100)

        grid = QtGui.QGridLayout()
        grid.setSpacing(1)
        grid.addWidget(self.labelFileName, 0, 0)
        grid.addWidget(self.lineEditFileName, 0, 1)
        grid.addWidget(self.labelFilePath, 1, 0)
        grid.addWidget(self.lineEditFilePath, 1, 1)
        grid.addWidget(self.aboutButton, 2, 0)
        grid.addWidget(self.githubLabel, 2, 1)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.treeView)
        layout.addWidget(self.installButton)
        layout.addLayout(grid)

        self.show()

    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)
        self.lineEditFileName.setText(fileName)
        self.lineEditFilePath.setText(filePath)

    def about(self):
        QtGui.QMessageBox.information(self, "About Package Installer", """Package Installer helps you to install '.deb', '.sh', 'tar.bz2' files via Terminal without typing command. It only tested on Ubuntu 15.10.""")

    def install_package(self):
        doc = QtGui.QTextDocument()
        doc.setHtml(self.lineEditFilePath.text())
        PackagePath = doc.toPlainText()

        try:
            FILE = open(PackagePath, 'rb')
            DATA = FILE.read(100)
            if DATA[:21] in [b'!<arch>\ndebian-binary']:
                subprocess.call(['gksudo', 'sudo dpkg -i {}'.format(PackagePath)])
            elif DATA[:6] == [b"BZh91AY&SY"]:
                QtGui.QMessageBox.critical(self, "Error", "asdasdasdasd!")
            else:
                QtGui.QMessageBox.critical(self, "Error", "Unsupported file type!")
        except FileNotFoundError:
            QtGui.QMessageBox.critical(self, "Error", "No file chosen!")
        except IsADirectoryError:
            QtGui.QMessageBox.critical(self, "Error", "It's a directory!")

PI = QtGui.QApplication(sys.argv)
PIWindow = PIWindow()
PI.exec_()
