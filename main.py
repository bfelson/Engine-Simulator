#PySide Stuff for GUI
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6.QtCore import QFile, QIODevice
from GUI import *
from EngineSimGUI_ui import Ui_MainWindow
from PregenPlotsWindow_ui import Ui_PregenPlotsWindow
from PySide6.QtWidgets import QMainWindow
from NewStudy_ui import Ui_newStudy

#Plot!
import matplotlib.pyplot as plt
from scipy.integrate import trapz

#Engine Sim Imports
from Engine import Engine
from Fuel import Fuel
from Injector import Injector
from Turbocharger import Turbocharger
from Reactor import Reactor
from xLet import xLet

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
        print("Making Engine...")
        self.make_engine()
        print("Engine Complete!")
        print("Making Fuel...")
        self.make_fuel()
        print("Fuel Complete!")
        print("Making Fuel Injector...")
        self.make_injector()
        print("Injector Complete!")
        print("Making Turbocharger")
        self.make_turbocharger()
        print("Turbocharger Complete!")

        print("Making Inlet...")
        self.make_inlet()
        print("Inlet Complete!")
        print("Making Outlet")
        self.make_outlet()
        print("Outlet Complete!")

        print("Generating Reactor...")
        self.make_reactor()
        print("Reactor Created!")
        print("Creating Simulator...")
        self.reactor.create_sim()
        print("Simulator Complete!")

        self.simulator = self.reactor.simulator


    def make_reactor(self):
        self.reactor = Reactor(
            self.fuel, self.turbocharger, self.engine, self.injector, self.inlet, self.outlet
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
            ui.injectorfuelcompedit.text(),
            float(ui.opetimingedit.text()),
            float(ui.closetimingedit.text()),
            float(ui.fuelmassedit.text()),
            self.engine
        )

    def make_turbocharger(self):
        self.turbocharger = Turbocharger(
            float(ui.turboinletpressureedit_2.text()), #wrong name but represents temp lol
            float(ui.turboinletpressureedit.text()),
            float(ui.turbooutlettempedit.text()),
            ui.turbooutletedit.text()
        )

    def make_inlet(self):
        self.inlet = xLet(
            'inlet',
            float(ui.inletvalvecoefficientedit.text()),
            float(ui.inletopentimingedit.text()),
            float(ui.inletclosetimingedit.text()),
            self.engine
        )

    def make_outlet(self):
        self.outlet = xLet(
            'outlet',
            float(ui.outletvalvecoefficientedit.text()),
            float(ui.outletopentimingedit.text()),
            float(ui.outletclosetimingedit.text()),
            self.engine
        )


    def startSimulation(self):
        self.reactor.run_sim()
        print("Simulation Done!")


    def pregeneratedPlots(self):
        self.pregenerated_window = PregeneratedWindow()
        self.pregenerated_window.show()

    def newStudy(self):
        self.newstudy_window = NewStudyWindow()
        self.newstudy_window.show()

    def selectFile(self):
        dialog = QFileDialog()
        dialog.setNameFilter("YAML Files (*.yaml)")
        fileName, _ = dialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "YAML Files (*.yaml)"
        )
        ui.filebrowsefilename.setText(fileName)

class PregeneratedWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PregenPlotsWindow()
        self.ui.setupUi(self)

        # self.canvas = self.ui.matplotlibWidget.canvas

        # self.ui.matplotlibWidget.main = MainWindow
        self.main = MainWindow
        self.sim = self.main.simulator
        self.s = self.main.simulator.states

    def plot_ca_pressure(self):
        fig, ax = plt.subplots()
        ax.plot(self.s.t, self.s.P)
        ax.set_xlabel(r'$\phi$ (rad)')
        ax.set_ylabel("Pressure (Pa)")
        ax.set_title('Pressure vs. Crank Angle (rad)')
        plt.show()

    def plot_ca_temp(self):
        fig, ax = plt.subplots()
        ax.plot(self.s.t, self.sim.states.T)
        ax.set_xlabel(r'$\phi$ (deg)')
        ax.set_ylabel('$T$ (K)')
        ax.set_title('Temperature vs. Crank Angle (rad)')
        plt.show()

    def plot_pv_diagram(self):
        fig, ax = plt.subplots()
        ax.plot(self.sim.states.V[self.s.t > 0.04] * 1000,  self.sim.states.P[self.s.t > 0.04])
        ax.set_xlabel('$V$ (L)')
        ax.set_ylabel('$P$ (Pa)')
        ax.set_title('P-V Diagram')
        plt.show()

    def plot_ts_diagram(self):
        fig, ax = plt.subplots()
        ax.plot(self.sim.states.m[self.s.t > 0.04] * self.sim.states.s[self.s.t > 0.04], self.sim.states.T[self.s.t > 0.04])
        ax.set_xlabel("$S$ (J/K)")
        ax.set_ylabel("$T$ (K)")
        ax.set_title('T-S Diagram')
        plt.show()

    def plot_QW(self):
        fig, ax = plt.subplots()
        ax.plot(self.s.t, 1e-3 * self.sim.states.heat_release_rate * self.sim.states.V, label=r'$\dot{Q}$')
        ax.plot(self.s.t, 1e-3 * self.sim.states.dWv_dt, label=r'\dot{W}_v')
        ax.set_xlabel(r'$\phi$ (rad)')
        ax.set_ylabel("kW")
        ax.set_title('Heat of Reaction and Expansion Work vs. Crank Angle')
        plt.show()

    def plot_gas_composition(self):
        fig, ax = plt.subplots()
        ax.plot(self.s.t, self.sim.states('o2').X, label='O2')
        ax.plot(self.s.t, self.sim.states('co2').X, label='CO2')
        ax.plot(self.s.t, self.sim.states('co').X, label='CO')
        ax.plot(self.s.t, self.sim.states('c12h26').X, label='n-Dodecane x10')

        ax.set_xlabel(r'$\phi$ (deg)')
        ax.set_ylabel('Mass Fraction $X_i$ (%)')
        ax.set_title('Gas Compositions')

        ax.legend()
        plt.show()

    def heat_release(self):
        Q = trapz(self.sim.states.heat_release_rate * self.sim.states.V, self.s.t)
        output_format = '{:45s}{:>4.1f} {}'
        self.ui.svalueoutput.setText(output_format.format('Heat Release per Cylinder (est.): ', Q / self.s.t[-1] / 1000., 'kW'))
        return Q / self.s.t[-1] / 1000

    def expansion_power(self):
        W = trapz(self.sim.states.dWv_dt, self.s.t)
        output_format = '{:45s}{:>4.1f} {}'
        self.ui.svalueoutput.setText(output_format.format('Expansion power per cylinder (est.)', W / self.s.t[-1] / 1000., 'kW'))
        return W / self.s.t[-1] / 1000

    def efficiency(self):
        W = trapz(self.sim.states.dWv_dt, self.s.t)
        Q = trapz(self.sim.states.heat_release_rate * self.sim.states.V, self.s.t)
        output_format = '{:45s}{:>4.1f} {}'
        self.ui.svalueoutput.setText(output_format.format('Efficiency (est.): ', W/Q * 100, '%'))
        return W/Q * 100

    def plot_CO(self):
        MW = self.sim.states.mean_molecular_weight
        CO_emission = trapz(MW * self.sim.states.mdot_out * self.sim.states('CO').X[:, 0], self.s.t)
        CO_emission /= trapz(MW * self.sim.states.mdot_out, self.s.t)
        self.ui.svalueoutput.setText('CO emission (estimate):', CO_emission * 1.e6, 'ppm')
        return CO_emission

    def plot_CO2(self):
        MW = self.sim.states.mean_molecular_weight
        CO2_emission = trapz(MW * self.sim.states.mdot_out * self.sim.states('CO2').X[:, 0], self.s.t)
        CO2_emission /= trapz(MW * self.sim.states.mdot_out, self.s.t)
        self.ui.svalueoutput.setText('CO2 emission (estimate):', CO2_emission * 1.e6, 'ppm')
        return CO2_emission

class NewStudyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_newStudy()
        self.ui.setupUi(self)

        self.main = MainWindow

    def heat_release(self):
            Q = trapz(self.sim.states.heat_release_rate * self.sim.states.V, self.s.t)
            output_format = '{:45s}{:>4.1f} {}'
            self.ui.svalueoutput.setText(output_format.format('Heat Release per Cylinder (est.): ', Q / self.s.t[-1] / 1000., 'kW'))
            return Q / self.s.t[-1] / 1000

    def expansion_power(self):
        W = trapz(self.sim.states.dWv_dt, self.s.t)
        output_format = '{:45s}{:>4.1f} {}'
        self.ui.svalueoutput.setText(output_format.format('Expansion power per cylinder (est.)', W / self.s.t[-1] / 1000., 'kW'))
        return W / self.s.t[-1] / 1000

    def efficiency(self):
        W = trapz(self.sim.states.dWv_dt, self.s.t)
        Q = trapz(self.sim.states.heat_release_rate * self.sim.states.V, self.s.t)
        output_format = '{:45s}{:>4.1f} {}'
        self.ui.svalueoutput.setText(output_format.format('Efficiency (est.): ', W/Q * 100, '%'))
        return W/Q * 100

    def plot_CO(self):
        MW = self.sim.states.mean_molecular_weight
        CO_emission = trapz(MW * self.sim.states.mdot_out * self.sim.states('CO').X[:, 0], self.s.t)
        CO_emission /= trapz(MW * self.sim.states.mdot_out, self.s.t)
        self.ui.svalueoutput.setText('CO emission (estimate):', CO_emission * 1.e6, 'ppm')
        return CO_emission

    def plot_CO2(self):
        MW = self.sim.states.mean_molecular_weight
        CO2_emission = trapz(MW * self.sim.states.mdot_out * self.sim.states('CO2').X[:, 0], self.s.t)
        CO2_emission /= trapz(MW * self.sim.states.mdot_out, self.s.t)
        self.ui.svalueoutput.setText('CO2 emission (estimate):', CO2_emission * 1.e6, 'ppm')
        return CO2_emission

    def runStudy(self):
        print("Setting up Parameters...")

        self.propertyToVary = self.ui.propertyToVary.currentText()

        self.min = int(self.ui.minedit.text())
        self.max = int(self.ui.maxedit.text())
        self.step = int(self.ui.stepedit.text())

        self.values = []
        self.co_emissions = []
        self.co2_emissions = []
        self.efficiency_list = []
        self.expansion_power_list = []
        self.heat_release_list = []

        print("Parameters set!")
        print("Running Study...")

        self.mainui = self.main.ui

        for i in range(self.min, self.max, self.step):
            print("Creating Reactor for " + self.propertyToVary + " = " + str(i))
            self.main.make_components()
            self.main.engine = Engine(
                self.main.engine.bore,
                self.main.engine.stroke,
                float(i), 
                self.main.engine.cylinder_count
            )
            self.main.make_reactor()
            self.main.reactor.create_sim()
            self.simulator = self.main.reactor.simulator

            print("Running Simulation for  " + self.propertyToVary + " = " + str(i))
            self.main.reactor.run_sim()
            print("Simulation Successful! Appending Data")
            self.values.append(i)
            self.co_emissions.append(self.main.reactor.CO_emissions)
            self.co2_emissions.append(self.main.reactor.CO2_emissions)
            self.efficiency_list.append(self.main.reactor.eta)
            self.heat_release_list.append(self.main.reactor.Q)
            self.expansion_power_list.append(self.main.reactor.W)

        self.plot_all()

    def plot(self, x, y, xlabel, ylabel, title):
        fig, ax = plt.subplots()
        ax.plot(x,y)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        plt.show()

    def plot_all(self):
        self.plot(self.values, self.co_emissions, "Compression Ratio", "CO Emissions (ppm)", "CO Emissions vs Compression Ratio")
        self.plot(self.values, self.co2_emissions, "Compression Ratio", "CO2 Emissions (ppm)", "CO2 Emissions vs Compression Ratio")
        self.plot(self.values, self.efficiency_list, "Compression Ratio", "Efficiency (%)", "Efficiency vs Compression Ratio")
        self.plot(self.values, self.heat_release_list, "Compression Ratio", "Heat Release (kW)", "Heat Release vs Compression Ratio")
        self.plot(self.values, self.expansion_power_list, "Compression Ratio", "Expansion Power (kW) ", "Expansion Power vs Compression Ratio")

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Window()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()