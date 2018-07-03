import sys
from Qt import QtCore, QtGui, QtWidgets

class MyDialog(QtWidgets.QDialog):
	def __init__(self):
		super(MyDialog, self).__init__()

		self.model = QtGui.QStandardItemModel()

		self.lv = QtWidgets.QListView()
		self.button = QtWidgets.QPushButton("Blah")

		lyt = QtWidgets.QVBoxLayout()
		lyt.addWidget(self.lv)
		lyt.addWidget(self.button)
		self.setLayout(lyt)


		self.lv.setModel(self.model)
		self.button.clicked.connect(self.on_button_pressed)

	def on_button_pressed(self):
		self.model.appendRow(
			QtGui.QStandardItem('Blah')
		)

if __name__ == "__main__":

	qApp = QtWidgets.QApplication(sys.argv)
	md = MyDialog()
	md.show()
	sys.exit(qApp.exec_())
