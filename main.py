import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6.QtCore import QFile, QIODevice
from GUI import *
from EngineSimGUI_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

#My Imports
from Engine import Engine
from Fuel import Fuel
from Injector import Injector
from Turbocharger import Turbocharger
from Reactor import Reactor

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

#fuel = Fuel('nDodecane_Reitz.yaml', 'nDodecane_IG', 'o2:1, n2:3.76', 'c12h26:1')
# injector = Injector(600, 1600e5, fuel.composition_fuel, 350, 365, 3.2e-5)
# turbocharger = Turbocharger(600, 1.3e5, 1.2e5, fuel.composition_air)
    def submitValues(self):
        #check if fields are filled here-----

        self.make_components()


    def make_components(self):
        self.make_engine()
        self.make_fuel()
        self.make_injector()
        self.make_turbocharger()

        self.make_reactor()
        self.reactor.create_sim()


    def make_reactor(self):
        self.reactor = Reactor(
            self.fuel, self.turbocharger, self.engine, self.injector
        )

    def make_fuel(self):
        self.fuel = Fuel(
            ui.filebrowsefilename.text(),
            ui.rxnmechedit.text(),
            ui.aircompedit.text(),
            ui.fuelcompedit.text()
        )
        
    def make_engine(self):
        self.engine = Engine(
            float(ui.boreedit.text()),
            float(ui.strokeedit.text()), 
            float(ui.cratioedit.text()), 
            int(ui.cylcountedit.text())
            )
        
    def make_injector(self):
        self.injector = Injector(
            float(ui.injectortempedit.text()),
            float(ui.injectorpressureedit.text()),
            float(ui.injectorfuelcompedit.text()),
            float(ui.opetimingedit.text()),
            float(ui.closetimingedit.text()),
            float(ui.fuelmassedit.text())
        )

    def make_turbocharger(self):
        self.turbocharger = Turbocharger(
            float(ui.turboinletpressureedit_2.text()), #wrong name but represents temp lol
            float(ui.turboinletpressureedit.text()),
            float(ui.turbooutlettempedit.text()),
            float(ui.turbooutletedit.text())
        )

    def startSimulation(self):
        self.reactor.run_sim()

    def plotValues(self):
        pass

    def pregeneratedPlots(self):
        pass

    def newStudy(self):
        pass

    def selectFile(self):
        dialog = QFileDialog()
        dialog.setNameFilter("YAML Files (*.yaml)")
        fileName, _ = dialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "YAML Files (*.yaml)"
        )
        ui.filebrowsefilename.setText(fileName)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Window()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()