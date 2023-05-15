import cantera as ct
from Fuel import *
from Engine import *
from Turbocharger import *
from xLet import *
from Ambient import *
from Simulator import *
from Injector import *
from scipy.integrate import trapz

# fuel = Fuel('nDodecane_Reitz.yaml', 'nDodecane_IG', 'o2:1, n2:3.76', 'c12h26:1')
# injector = Injector(600, 1600e5, fuel.composition_fuel, 350, 365, 3.2e-5)
# turbocharger = Turbocharger(600, 1.3e5, 1.2e5, fuel.composition_air)

class Reactor():
    def __init__(self, fuel, turbocharger, engine, injector):
        self.engine = engine
        self.fuel = fuel
        self.turbocharger = turbocharger
        self.injector = injector

        self.runSimulation = False
        #store thermodynamic state of fuel
        self.gas = ct.Solution(fuel.rxn_mechanism, fuel.phase_name)

        #Initial state for Inlet
        self.gas.TPX = turbocharger.inlet_temp, turbocharger.inlet_pressure, turbocharger.inlet_composition
        #make reactor
        self.cylinder = ct.IdealGasReactor(self.gas)
        self.cylinder.volume = self.engine.volume_combustion_dome

        self.gas.TPX = turbocharger.inlet_temp, turbocharger.inlet_pressure, turbocharger.inlet_composition
        self.inlet_reservoir = ct.Reservoir(self.gas)
        #Create outlet valve
        self.inlet_valve = ct.Valve(self.inlet_reservoir, self.cylinder)
        self.inlet_valve.valve_coeff = inlet.valve_coefficient
        self.inlet_valve.set_time_function(inlet.isOpen)

        #Injector Stuff
        self.gas.TPX = self.injector.temperature, self.injector.pressure, self.injector.composition
        self.injector_reservoir = ct.Reservoir(self.gas)

        self.injector_mfc = ct.MassFlowController(self.injector_reservoir, self.cylinder)
        self.injector_mfc.mass_flow_coeff = self.injector.mass_flow_coefficient
        self.injector_mfc.set_time_function(self.injector.isOpen)

        #Next state for outlet
        self.gas.TPX = ambient.temperature, turbocharger.outlet_pressure, ambient.composition
        self.outlet_reservoir = ct.Reservoir(self.gas)

        #Create Outlet Valve
        self.outlet_valve = ct.Valve(self.cylinder, self.outlet_reservoir)
        self.outlet_valve.valve_coeff = outlet.valve_coefficient
        self.outlet_valve.set_time_function(outlet.isOpen)

        #Ambient Stuff
        self.gas.TPX = ambient.temperature, ambient.pressure, ambient.composition
        self.ambient_reservoir = ct.Reservoir(self.gas)

        #Setting Piston as moving wall
        piston = ct.Wall(self.ambient_reservoir, self.cylinder)
        piston.area = self.engine.area
        piston.set_velocity(self.engine.get_piston_speed)

    def create_sim(self):
        self.simulator = Simulator(8, 20, 1e-12, 1e-16, self.cylinder, 1, self.inlet_valve, self.outlet_valve, self.ambient_reservoir)
        self.cylinder.set_advance_limit('temperature', self.simulator.max_delta_t)

    def run_sim(self):
        self.simulator.simulate()
        self.t = self.simulator.states.t
        #Assigning a bunch of things for plotting later

        #s is for ease of use
        self.s = self.simulator.states

        #Pressure
        self.P = self.s.P
        #Temperature
        self.T = self.s.T
        #Volume
        self.V = self.s.m * self.s.s
        #Heat of Reaction
        self.heat_rxn = self.s.heat_release_rate * self.V
        #Expansion Work
        self.dWv_dt = self.s.dWv_dt
        #Gas Composition -----------
        self.o2_comp = self.s('o2').X
        self.co2_comp = self.s('co2').X
        self.co_comp = self.s('co').X
        self.fuel_comp = self.s(self.fuel.composition_fuel[:-2])
        #Heat Release Rate per Cylinder
        self.Q = trapz(self.s.heat_release_rate * self.V, self.t) / self.t[-1] * 1000 #kW
        #Expansion Power
        self.W = trapz(self.dWv_dt, self.t) / self.t[-1] * 1000 #kW
        #Efficiency
        self.eta = (self.W / self.Q) * 100 #%
        #Molecular Weight
        self.MW = self.s.mean_molecular_weight
        #Emissions (ppm)
        self.CO_emissions = trapz(self.MW * self.s.mdot_out * self.s('CO').X[:, 0], self.t) / trapz(self.MW * self.s.mdot_out, self.t) * 1e6
        self.CO2_emissions = trapz(self.MW * self.s.mdot_out * self.s('CO2').X[:, 0], self.t) / trapz(self.MW * self.s.mdot_out, self.t) * 1e6

        self.runSimulation = True

# r = Reactor(fuel, turbocharger)
# r.create_sim()
# r.run_sim()