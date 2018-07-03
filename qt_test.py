import sys
from Qt import load_ui, QtCore, QtGui, QtWidgets


class MyWindow(QtWidgets.QMainWindow):
	def __init__(self, api):
		super(MyWindow, self).__init__()

		self.form = load_ui('form.ui')
		self.setCentralWidget(self.form)

		self.api = api

		self.model_filter = QtCore.QSortFilterProxyModel()
		self.model_filter.setSourceModel(self.api.model)		

		self.form.lv.setModel(self.model_filter)
		self.form.comboBox.setModel(self.api.model)
		self.form.button.clicked.connect(self.on_button_pressed)

		self.form.lineEdit.textChanged.connect(self.on_line_edit_changed)

	def on_button_pressed(self):
		self.api.add_item()

	def on_line_edit_changed(self):
		filter_text = self.form.lineEdit.text()
		self.model_filter.setFilterFixedString(filter_text)


class MyApi(object):
	def __init__(self):
		self.model = QtGui.QStandardItemModel()
		self.count = 0

		for i in dir(QtGui):
			self.model.appendRow(
				QtGui.QStandardItem(i)
			)

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
