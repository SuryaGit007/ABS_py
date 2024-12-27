import tkinter as tk
from gui.sliders import create_sliders
from simulation.abs_model import ABSSimulator

def run_app():
    # Initialize simulation and GUI
    simulator = ABSSimulator()
    
    root = tk.Tk()
    root.title("ABS Braking Simulator")
    root.geometry("800x600")

    # Create sliders for parameters
    sliders = create_sliders(root, simulator)

    # Create display for simulation output
    speed_display = tk.Label(root, text="Vehicle Speed: -- km/h\nTire Speed: -- km/h\nSlip Ratio: --%", font=("Arial", 14))
    speed_display.pack(pady=20)

    def update_simulation():
        simulator.update()
        speed_display.config(
            text=f"Vehicle Speed: {simulator.vehicle_speed:.2f} km/h\n"
                 f"Tire Speed: {simulator.tire_speed:.2f} km/h\n"
                 f"Slip Ratio: {simulator.slip_ratio:.2f}%"
        )
        root.after(100, update_simulation)

    # Start simulation update loop
    update_simulation()
    root.mainloop()
