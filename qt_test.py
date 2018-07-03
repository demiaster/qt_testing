import sys
from Qt import QtCore, QtGui, QtWidgets

if __name__ == "__main__":

	qApp = QtWidgets.QApplication(sys.argv)
	d = QtWidgets.QDialog()
	d.show()
	sys.exit(qApp.exec_())
