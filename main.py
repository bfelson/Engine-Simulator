
'''
def plot_ca_pressure():
    fig, ax = plt.subplots()
    ax.plot(t, sim.states.P)
    ax.set_xlabel(r'$\phi$ (deg)')
    ax.set_ylabel("Pressure (Pa)")
    plt.show()

def plot_ca_temp():
    fig, ax = plt.subplots()
    ax.plot(t, sim.states.T)
    ax.set_xlabel(r'$\phi$ (deg)')
    ax.set_ylabel('$T$ (K)')
    plt.show()

def plot_pv_diagram():
    fig, ax = plt.subplots()
    ax.plot(sim.states.V[t > 0.04] * 1000,  sim.states.P[t > 0.04])
    ax.set_xlabel('$V$ (L)')
    ax.set_ylabel('$P$ (Pa)')
    plt.show()

def plot_ts_diagram():
    fig, ax = plt.subplots()
    ax.plot(sim.states.m[t > 0.04] * sim.states.s[t > 0.04], sim.states.T[t > 0.04])
    ax.set_xlabel("$S$ (J/K)")
    ax.set_ylabel("$T$ (K)")
    plt.show()

def plot_QW():
    fig, ax = plt.subplots()
    ax.plot(t, 1e-3 * sim.states.heat_release_rate * sim.states.V, label=r'$\dot{Q}$')
    ax.plot(t, 1e-3 * sim.states.dWv_dt, label=r'\dot{W}_v')
    ax.set_xlabel(r'$\phi$ (deg)')
    ax.set_ylabel("kW")
    plt.show()

def plot_gas_composition():
    fig, ax = plt.subplots()
    ax.plot(t, sim.states('o2').X, label='O2')
    ax.plot(t, sim.states('co2').X, label='CO2')
    ax.plot(t, sim.states('co').X, label='CO')
    ax.plot(t, sim.states('c12h26').X, label='n-Dodecane x10')

    ax.set_xlabel(r'$\phi$ (deg)')
    ax.set_ylabel('Mass Fraction $X_i$ (%)')
    plt.show()

def heat_release():
    Q = trapz(sim.states.heat_release_rate * sim.states.V, t)
    output_format = '{:45s}{:>4.1f} {}'
    print(output_format.format('Heat Release per Cylinder (est.): ', Q / t[-1] / 1000., 'kW'))

def expansion_power():
    W = trapz(sim.states.dWv_dt, t)
    output_format = '{:45s}{:>4.1f} {}'
    print(output_format.format('Expansion power per cylinder (est.)', W / t[-1] / 1000., 'kW'))

def efficiency():
    W = trapz(sim.states.dWv_dt, t)
    Q = trapz(sim.states.heat_release_rate * sim.states.V, t)
    output_format = '{:45s}{:>4.1f} {}'
    print(output_format.format('Efficiency (est.): ', W/Q * 100, '%'))

def plot_CO():
    MW = sim.states.mean_molecular_weight
    CO_emission = trapz(MW * sim.states.mdot_out * sim.states('CO').X[:, 0], t)
    CO_emission /= trapz(MW * sim.states.mdot_out, t)
    print('CO emission (estimate):', CO_emission * 1.e6, 'ppm')

def plot_CO2():
    MW = sim.states.mean_molecular_weight
    CO2_emission = trapz(MW * sim.states.mdot_out * sim.states('CO2').X[:, 0], t)
    CO2_emission /= trapz(MW * sim.states.mdot_out, t)
    print('CO2 emission (estimate):', CO2_emission * 1.e6, 'ppm')
'''

import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "EngineSimGUI.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec())