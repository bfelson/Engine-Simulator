import cantera as ct

from Engine import *
from Ambient import *
from Reactor import *

class Simulator():
    def __init__(self, number_revolutions, max_delta_t, rtol, atol, cylinder, 
                 max_resolution, inlet_valve, outlet_valve, ambient_reservoir):
        self.number_revolutions = number_revolutions
        self.max_delta_t = max_delta_t
        self.rtol = rtol
        self.atol = atol

        self.cylinder = cylinder
        self.reactorNet = ct.ReactorNet([cylinder])
        self.reactorNet.rtol = self.rtol
        self.reactorNet.atol = self.atol

        self.max_resolution = max_resolution

        self.inlet_valve = inlet_valve
        self.outlet_valve = outlet_valve

        self.ambient_reservoir = ambient_reservoir

    def simulate(self):
        self.states = ct.SolutionArray(
            self.cylinder.thermo,
            extra=('t', 'ca', 'V', 'm', 'mdot_in', 'mdot_out', 'dWv_dt')
        )

        dt = self.max_resolution / (360 * engine.engine_speed)
        time_stop = self.number_revolutions / engine.engine_speed

        while self.reactorNet.time < time_stop:
            self.reactorNet.advance(self.reactorNet.time + dt)

            dWv_dt = - (self.cylinder.thermo.P - self.ambient_reservoir.thermo.P) * engine.area * engine.get_piston_speed(self.reactorNet.time)

            self.states.append( self.cylinder.thermo.state,
                                t = self.reactorNet.time,
                                ca = engine.get_crank_angle(self.reactorNet.time),
                                V = self.cylinder.volume,
                                m = self.cylinder.mass,
                                mdot_in = self.inlet_valve.mass_flow_rate,
                                mdot_out = self.outlet_valve.mass_flow_rate,
                                dWv_dt = dWv_dt
            )