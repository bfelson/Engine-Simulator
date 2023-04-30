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

app = App()
app.title("Sample GUI")
app.mainloop()