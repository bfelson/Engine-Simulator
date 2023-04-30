import cantera as ct

class Fuel():
    def __init__(self, rxn_mechanism, phase_name, composition_air, composition_fuel):
        self.rxn_mechanism = rxn_mechanism
        self.phase_name = phase_name
        self.composition_air = composition_air 
        self.composition_fuel = composition_fuel

fuel = Fuel('nDodecane_Reitz.yaml', 'nDodecane_IG', 'o2:1, n2:3.76', 'c12h26:1')