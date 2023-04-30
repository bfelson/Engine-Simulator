import numpy as np
import matplotlib.pyplot as plt
from Ambient import *
from Fuel import *
from Turbocharger import *
from Reactor import *
from Engine import *

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

sim = simulator
sim.simulate()
t = sim.states.t

plot_pv_diagram()