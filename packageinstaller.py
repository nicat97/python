from PyQt4 import QtCore, QtGui
import sys
import os
import subprocess
import tarfile

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
        self.lineEditFileName.setReadOnly(True)
        self.labelFilePath = QtGui.QLabel(self)
        self.labelFilePath.setText("File Path:")
        self.lineEditFilePath = QtGui.QLineEdit(self)
        self.lineEditFilePath.setReadOnly(True)
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

        QtGui.QMessageBox.information(self, "Information", "For use the Package Installer you must be install 'gksu' package by the typing <b>sudo apt-get install gksu</b> command on terminal.")

        self.show()

    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)
        self.lineEditFileName.setText(fileName)
        self.lineEditFilePath.setText(filePath)

    def about(self):
        QtGui.QMessageBox.information(self, "About Package Installer", """Package Installer helps you to install '.deb', '.sh', 'tar' files via Terminal without typing command. It only tested on Ubuntu 15.10. Firstly, you must be install 'gksu' package by the typing <b>sudo apt-get install</b> command on terminal.""")

    def install_package(self):
        doc = QtGui.QTextDocument()
        doc.setHtml(self.lineEditFilePath.text())
        PackagePath = doc.toPlainText()
        doc2 = QtGui.QTextDocument()
        doc2.setHtml(self.lineEditFileName.text())
        PackageName = doc2.toPlainText()
        Path_tar_bz2 = PackageName[:-8]
        Path_tgz = PackageName[:-4]
        Path_tbz2 = PackageName[:-5]
        Path_tar_gz = PackageName[:-7]
        try:
            FILE = open(PackagePath, 'rb')
            DATA = FILE.read(25)
            Path = os.path.dirname(PackagePath)
            if DATA[:21] in [b'!<arch>\ndebian-binary']:
                subprocess.call(['gksudo', 'sudo dpkg -i {}'.format(PackagePath)])
            elif tarfile.is_tarfile(PackagePath):
                if PackagePath.lower().endswith('.tar.gz'):
                    Question = QtGui.QMessageBox.question(self, 'Tar file installation', "Installation of 'tar' files with Package Installer can be unsuccessful. You can install it by typing these commands step by step on terminal:<b><p>tar zxf *.tgz</p><p>cd *</p><p>./configure</p><p>make</p><p>make install</p><p></b>Do you want to continue with Package Installer?</p>", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                    if Question == QtGui.QMessageBox.Yes:
                        os.system('tar zxf {}'.format(PackagePath))
                        os.system('cd {}'.format(Path_tar_gz))
                        os.system('./configure')
                        os.system('make')
                        os.system('make install')
                    else:
                        pass
                elif PackagePath.lower().endswith('.tgz'):
                    Question = QtGui.QMessageBox.question(self, 'Tar file installation', "Installation of 'tar' files with Package Installer can be unsuccessful. You can install it by typing these commands step by step on terminal:<b><p>tar zxf *.tgz</p><p>cd *</p><p>./configure</p><p>make</p><p>make install</p><p></b>Do you want to continue with Package Installer?</p>", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                    if Question == QtGui.QMessageBox.Yes:
                        os.system('tar zxf {}'.format(PackagePath))
                        os.system('cd {}'.format(Path_tgz))
                        os.system('./configure')
                        os.system('make')
                        os.system('make install')
                    else:
                        pass
                elif PackagePath.lower().endswith('.tar.bz2'):
                    Question = QtGui.QMessageBox.question(self, 'Tar file installation', "Installation of 'tar' files with Package Installer can be unsuccessful. You can install it by typing these commands step by step on terminal:<b><p>tar jxf *.tar.bz2</p><p>cd *</p><p>./configure</p><p>make</p><p>make install</p><p></b>Do you want to continue with Package Installer?</p>", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                    if Question == QtGui.QMessageBox.Yes:
                        os.system('tar jxf {}'.format(PackagePath))
                        os.system('cd {}'.format(Path_tar_bz2))
                        os.system('./configure')
                        os.system('make')
                        os.system('make install')
                    else:
                        pass
                elif PackagePath.lower().endswith('.tbz2'):
                    Question = QtGui.QMessageBox.question(self, 'Tar file installation', "Installation of 'tar' files with Package Installer can be unsuccessful. You can install it by typing these commands step by step on terminal:<b><p>tar jxf *.tgz</p><p>cd *</p><p>./configure</p><p>make</p><p>make install</p><p></b>Do you want to continue with Package Installer?</p>", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                    if Question == QtGui.QMessageBox.Yes:
                        os.system('tar jxf {}'.format(PackagePath))
                        os.system('cd {}'.format(Path_tbz2))
                        os.system('./configure')
                        os.system('make')
                        os.system('make install')
                    else:
                        pass
                else:
                    QtGui.QMessageBox.critical(self, "Error", "Unsupported tar file.")
            elif Data[:8] in [b'#!/bin/sh']:
                os.system('cd {}'.format(Path))
                os.system('chmod +x {}'.format(PackageName))
                os.system('./{}'.format(PackageName))
            else:
                QtGui.QMessageBox.critical(self, "Error", "Unsupported file type!")
        except FileNotFoundError:
            QtGui.QMessageBox.critical(self, "Error", "No file chosen!")
        except IsADirectoryError:
            QtGui.QMessageBox.critical(self, "Error", "It's a directory!")

PI = QtGui.QApplication(sys.argv)
PIWindow = PIWindow()
PI.exec_()
