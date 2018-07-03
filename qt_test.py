import sys
from Qt import QtCore, QtGui, QtWidgets

class MyDialog(QtWidgets.QDialog):
	def __init__(self, api):
		super(MyDialog, self).__init__()

		self.api = api

		self.lv = QtWidgets.QListView()
		self.button = QtWidgets.QPushButton("Blah")

		lyt = QtWidgets.QVBoxLayout()
		lyt.addWidget(self.lv)
		lyt.addWidget(self.button)
		self.setLayout(lyt)


		self.lv.setModel(self.api.model)
		self.button.clicked.connect(self.on_button_pressed)

	def on_button_pressed(self):
		self.api.add_item()

class MyApi(object):
	def __init__(self):
		self.model = QtGui.QStandardItemModel()
		self.count = 0

	def add_item(self):
		self.count += 1
		self.model.appendRow(
			QtGui.QStandardItem(
				'Item {0}'.format(self.count)
			)
		)


if __name__ == "__main__":

	qApp = QtWidgets.QApplication(sys.argv)
	api = MyApi()
	md = MyDialog(api)
	md.show()
	sys.exit(qApp.exec_())
