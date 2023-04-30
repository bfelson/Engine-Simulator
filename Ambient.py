class Ambient():
    def __init__(self, temperature, pressure, composition):
        self.temperature = temperature
        self.pressure = pressure
        self.composition = composition

ambient = Ambient(600, 1e5, 'o2:1, n2:3.76')