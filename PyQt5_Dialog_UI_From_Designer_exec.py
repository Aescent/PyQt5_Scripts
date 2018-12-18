#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyQt
from PyQt5.QtWidgets import QDialog, QApplication

# "untitled" is your ui file, here this is untitled.ui.
# Ui_Dialog is the Class of your ui file with setupUi function
# which describe your ui form.
from untitled import Ui_Dialog

class MainDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(MainDialog,self).__init__()
	
	# Initializing Ui form
        self.setupUi(self)
		
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv) 
    maindial = MainDialog()
    maindial.show()
    sys.exit(app.exec())
