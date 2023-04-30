import numpy as np
import matplotlib.pyplot as plt
from Ambient import *
from Fuel import *
from Turbocharger import *
from Reactor import *
from Engine import *
from GUI import *

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


sim = simulator
sim.simulate()
t = sim.states.t
