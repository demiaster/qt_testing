import sys
from Qt import load_ui, QtGui, QtWidgets


class MyWindow(QtWidgets.QMainWindow):
	def __init__(self, api):
		super(MyWindow, self).__init__()

		self.form = load_ui('form.ui')
		self.setCentralWidget(self.form)

		self.api = api

		self.form.lv.setModel(self.api.model)
		self.form.button.clicked.connect(self.on_button_pressed)

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

	# Something happens before UI
	api.add_item()

	md = MyWindow(api)
	md.show()
	sys.exit(qApp.exec_())
