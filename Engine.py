import numpy as np

class Engine():
    def __init__(self, bore, stroke, compression_ratio, cylinder_count):
        self.bore = bore #diameter, in m
        self.stroke = stroke
        self.cylinder_count = cylinder_count
        self.compression_ratio = compression_ratio

        self.area = (np.pi / 4) * bore ** 2
        self.volume_cylinder = self.area * self.stroke
        self.volume_combustion_dome = self.volume_cylinder / (self.compression_ratio - 1)



        self.engine_speed = 3000 / 60 #rpm

    def get_crank_angle(self, t):
        return np.remainder(2 * np.pi * self.engine_speed * t, 4 * np.pi)
    
    def get_piston_speed(self, t):
        return - self.stroke * np.pi * self.engine_speed * np.sin(self.get_crank_angle(t))
    
engine = Engine(0.083, 0.006, 50, 4)