import numpy as np
from Fuel import *
from Engine import *

class Injector():
    def __init__(self, temperature, pressure, composition, open, close, m):
        self.temperature = temperature
        self.pressure = pressure
        self.composition = composition
        self.open_timing = open / 180 * np.pi
        self.close_timing = close / 180 * np.pi
        self.mass = m

        self.delta = np.mod(self.close_timing - self.open_timing, 4 * np.pi)
        self.time_open = (self.close_timing - self.open_timing) / 2 / np.pi / engine.engine_speed

        self.mass_flow_coefficient = self.mass / self.time_open

    def isOpen(self, t):
        #Returns true if xLet is open at a given time t
        return np.mod(engine.get_crank_angle(t) - self.open_timing, 4 * np.pi) < self.delta