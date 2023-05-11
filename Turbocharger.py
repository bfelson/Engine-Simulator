import numpy as np
from Fuel import *

class Turbocharger():
    def __init__(self, inlet_temp, inlet_pressure, outlet_pressure, inlet_composition):
        self.inlet_temp = inlet_temp #Kelvin
        self.inlet_pressure = inlet_pressure
        self.outlet_pressure = outlet_pressure
        self.inlet_composition = inlet_composition

