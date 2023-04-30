import cantera as ct
from Fuel import *
from Engine import *
from Turbocharger import *
from xLet import *
from Ambient import *
from Simulator import *
from Injector import *

#store thermodynamic state of fuel
gas = ct.Solution(fuel.rxn_mechanism, fuel.phase_name)

#Initial state for Inlet
gas.TPX = turbocharger.inlet_temp, turbocharger.inlet_pressure, turbocharger.inlet_composition
#make reactor
cylinder = ct.IdealGasReactor(gas)
cylinder.volume = engine.volume_combustion_dome

gas.TPX = turbocharger.inlet_temp, turbocharger.inlet_pressure, turbocharger.inlet_composition
inlet_reservoir = ct.Reservoir(gas)
#Create outlet valve
inlet_valve = ct.Valve(inlet_reservoir, cylinder)
inlet_valve.valve_coeff = inlet.valve_coefficient
inlet_valve.set_time_function(inlet.isOpen)

#Injector Stuff
gas.TPX = injector.temperature, injector.pressure, injector.composition
injector_reservoir = ct.Reservoir(gas)

injector_mfc = ct.MassFlowController(injector_reservoir, cylinder)
injector_mfc.mass_flow_coeff = injector.mass_flow_coefficient
injector_mfc.set_time_function(injector.isOpen)

#Next state for outlet
gas.TPX = ambient.temperature, turbocharger.outlet_pressure, ambient.composition
outlet_reservoir = ct.Reservoir(gas)

#Create Outlet Valve
outlet_valve = ct.Valve(cylinder, outlet_reservoir)
outlet_valve.valve_coeff = outlet.valve_coefficient
outlet_valve.set_time_function(outlet.isOpen)

#Ambient Stuff
gas.TPX = ambient.temperature, ambient.pressure, ambient.composition
ambient_reservoir = ct.Reservoir(gas)

#Setting Piston as moving wall
piston = ct.Wall(ambient_reservoir, cylinder)
piston.area = engine.area
piston.set_velocity(engine.get_piston_speed)

simulator = Simulator(8, 20, 1e-12, 1e-16, cylinder, 1, inlet_valve, outlet_valve, ambient_reservoir)
cylinder.set_advance_limit('temperature', simulator.max_delta_t)