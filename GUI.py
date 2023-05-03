import tkinter as tk
from main import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create a frame for the main content of the window
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        #Crank Angle, P
        self.ca_pressure_button = tk.Button(self, text="Plot CA Pressure", command=plot_ca_pressure)
        self.ca_pressure_button.pack()

        #Crank Angle, Temp
        self.ca_temperature_button = tk.Button(self, text="Plot CA Temperature", command = plot_ca_temp)
        self.ca_temperature_button.pack()

        #PV Diagram
        self.pv_diagram_button = tk.Button(self, text="Plot PV Diagram", command = plot_pv_diagram)
        self.pv_diagram_button.pack()

        #TS Diagram
        self.pv_diagram_button = tk.Button(self, text="Plot TS Diagram", command = plot_ts_diagram)
        self.pv_diagram_button.pack()

        #Heat of Reaction
        self.pv_diagram_button = tk.Button(self, text="Plot Reaction Heat, Expansion Work", command = plot_QW)
        self.pv_diagram_button.pack()

        #Gas Composition
        self.pv_diagram_button = tk.Button(self, text="Plot Gas Composition", command = plot_gas_composition)
        self.pv_diagram_button.pack()

        #CO Emissions
        self.pv_diagram_button = tk.Button(self, text="Print CO Emissions", command = plot_CO)
        self.pv_diagram_button.pack()

        #CO2 Emissions
        self.pv_diagram_button = tk.Button(self, text="Print CO2 Emissions", command = plot_CO2)
        self.pv_diagram_button.pack()

app = App()
app.title("Sample GUI")
app.mainloop()