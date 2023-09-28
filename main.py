from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import *
from PySide6.QtWidgets import *


SI_W = {'kg':10**3, 'g': 1.0, 'T': 10**6, 'P': 453}
SI_L = {'mm': 10**-3, 'cm': 10**-2, 'm': 1.0, 'km': 10**3, 'in': 0.17}
SI_T = { 'C': 1.0 , 'F':-17.22, 'K':-272.15}
SI_D = {'byte': 1, 'bit': 0.125 , 'KByte': 10**3, 'MByte': 10**6,'GByte':10**9, 'TByte':10**12}


class Unit_Canverter(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()

        self.ui = loader.load('design.ui')
        self.ui.setWindowTitle('Unit Converter')
        self.ui.show()

        self.ui.combo_change.currentTextChanged.connect(self.Change)
        self.ui.btn_convert.clicked.connect(self.converter)

        self.From = self.ui.combo_from.currentText()
        self.To = self.ui.combo_to.currentText()

        self.ui.combo_change.addItems(['Temperature', 'Weight', 'Digital Storage', 'Lenght'])


    def Change(self):
        
        self.ui.combo_from.clear()
        self.ui.combo_to.clear()
        
        if self.ui.combo_change.currentText() == 'Weight':
            self.ui.combo_from.addItems(['g', 'kg', 'T', 'P'])
            self.ui.combo_to.addItems(['g', 'kg', 'T', 'P'])

        elif self.ui.combo_change.currentText() == 'Lenght':
            self.ui.combo_from.addItems(['mm', 'cm', 'm', 'km', 'in'])
            self.ui.combo_to.addItems(['mm', 'cm', 'm', 'km', 'in'])

        elif self.ui.combo_change.currentText() == 'Temperature':
            self.ui.combo_from.addItems(['C', 'F', 'K'])
            self.ui.combo_to.addItems(['C', 'F', 'K'])

        elif self.ui.combo_change.currentText() == 'Digital Storage':
            self.ui.combo_from.addItems(['byte', 'bit', 'KByte', 'MByte', 'GByte', 'TByte'])
            self.ui.combo_to.addItems(['byte', 'bit', 'KByte', 'MByte', 'GByte', 'TByte'])


    def converter(self):
        if self.ui.combo_change.currentText() == 'Weight':
            number = int(self.ui.tb_in.text()) 
            number *= SI_W[self.ui.combo_from.currentText()] / SI_W[self.ui.combo_to.currentText()]
            number = str(number)
            self.ui.tb_out.setText(number)

        elif self.ui.combo_change.currentText() == 'Lenght':
            number = int(self.ui.tb_in.text()) 
            number *= SI_L[self.ui.combo_from.currentText()] / SI_L[self.ui.combo_to.currentText()]
            number = str(number)
            self.ui.tb_out.setText(number)

        elif self.ui.combo_change.currentText() == 'Temperature':
            number = int(self.ui.tb_in.text()) 
            number *= (SI_T[self.ui.combo_from.currentText()] / SI_T[self.ui.combo_to.currentText()])
            number = str(number)
            self.ui.tb_out.setText(number)
        
        elif self.ui.combo_change.currentText() == 'Digital Storage':
            number = int(self.ui.tb_in.text()) 
            number *= SI_D[self.ui.combo_from.currentText()] / SI_D[self.ui.combo_to.currentText()]
            number = str(number)
            self.ui.tb_out.setText(number)

app = QApplication([])
window = Unit_Canverter()
app.exec()