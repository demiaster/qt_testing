import sys
from Qt import QtCore, QtGui, QtWidgets

class MyDialog(QtWidgets.QDialog):
	def __init__(self):
		super(MyDialog, self).__init__()

		self.button = QtWidgets.QPushButton("Blah")

		lyt = QtWidgets.QVBoxLayout()
		lyt.addWidget(self.button)
		self.setLayout(lyt)

		self.button.clicked.connect(self.on_button_pressed)

	def on_button_pressed(self):
		print "Someone Pressed the Button!"

if __name__ == "__main__":

	qApp = QtWidgets.QApplication(sys.argv)
	md = MyDialog()
	md.show()
	sys.exit(qApp.exec_())
