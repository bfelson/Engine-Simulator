import numpy as np
from Engine import *

class xLet():
    def __init__(self, type, valve_coefficient, open, close):
        self.type = type
        self.valve_coefficient = valve_coefficient
        self.open_timing = open / 180 * np.pi
        self.close_timing = close / 180 * np.pi

        self.delta = np.mod(self.close_timing - self.open_timing, 4 * np.pi)

    def isOpen(self, t):
        #Returns true if xLet is open at a given time t
        return np.mod(engine.get_crank_angle(t) - self.open_timing, 4 * np.pi) < self.delta


inlet = xLet('inlet', 1e-6, -18, 198)
outlet = xLet('outlet', 1e-6, 522, 18)

