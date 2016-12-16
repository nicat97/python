#!/usr/bin/bash
echo "'gksu', 'PyQt4' packages and 'sh' module must be installed on your system to use Package Installer."
sudo apt-get install gksu
sudo apt-get install build-essential, qt4-qmake, qt4-dev-tools
sudo apt-get install python3-pip
pip3 install sh
echo "Now you can use Package Installer."
exit
