import tkinter as tk

def create_sliders(root, simulator):
    sliders = []
    params = [
        ("Road Friction", "road_friction", 0.1, 1.0, 0.1),
        ("Brake Force", "brake_force", 0, 1000, 50),
        ("Vehicle Mass", "vehicle_mass", 500, 5000, 100),
    ]

    for param_name, param_key, min_val, max_val, step in params:
        frame = tk.Frame(root)
        frame.pack(pady=10)

        label = tk.Label(frame, text=param_name)
        label.pack(side="left")

        slider = tk.Scale(frame, from_=min_val, to=max_val, resolution=step, orient="horizontal")
        slider.set(getattr(simulator, param_key))
        slider.pack(side="left")

        def update_parameter(value, key=param_key):
            setattr(simulator, key, float(value))

        slider.config(command=update_parameter)
        sliders.append(slider)

    return sliders
