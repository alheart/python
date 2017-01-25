# -*- coding: utf-8 -*-

"""
Module implementing termDialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from Ui_autoterm import Ui_Dialog
from miniterm import Miniterm
from production import Production

class termDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(termDialog, self).__init__(parent)
        self.setupUi(self)
    
        
    def msg(self, msg, color='black', level=''):
        # TODO: not implemented yet
        #_translate = QtCore.QCoreApplication.translate
        textcolor=color
        if ('error' == level):
            textcolor='red'
        elif ('success' == level):
            textcolor='green'
        elif ('normal' == level):
            textcolor='black'
        self.statusLabel.setStyleSheet("QFrame{color:%s}" % textcolor)
        self.statusLabel.setText(msg)
        
    def process(self, value):
        self.prosBar.setValue(value)
    
    @pyqtSlot()
    def on_startBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        port="com5"
        baudrate=115200
        parity="N"
        rtscts=False
        xonxoff=False
        miniterm = Miniterm(port, baudrate, parity, rtscts, xonxoff)
        production = Production(miniterm, self.msg, self.process)
        miniterm.start()
        production.start()

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = termDialog()
    dlg.show()
    sys.exit(app.exec_())
