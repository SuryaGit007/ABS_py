import tkinter as tk
from PIL import Image, ImageTk

def create_visualization(root, simulator):
    # Load bus images
    top_view_img = Image.open("assets/bus_top_view.png").resize((400, 200))
    side_view_img = Image.open("assets/bus_side_view.png").resize((400, 150))

    top_view = ImageTk.PhotoImage(top_view_img)
    side_view = ImageTk.PhotoImage(side_view_img)

    # Display images
    top_view_label = tk.Label(root, image=top_view)
    top_view_label.image = top_view  # Reference to prevent garbage collection
    top_view_label.pack()

    side_view_label = tk.Label(root, image=side_view)
    side_view_label.image = side_view  # Reference to prevent garbage collection
    side_view_label.pack()

    # Add dynamic text display
    data_label = tk.Label(root, text="", font=("Arial", 14), justify="left")
    data_label.pack()

    def update_visualization():
        # Update dynamic text
        wheel_data = "\n".join(
            [
                f"Wheel {i + 1}: Speed: {simulator.wheel_speeds[i]:.2f} km/h, "
                f"Slip: {simulator.slip_ratios[i]:.2f}%, "
                f"Brake Force: {simulator.brake_forces[i]:.2f} N, "
                f"Brake Torque: {simulator.brake_torques[i]:.2f} Nm"
                for i in range(4)
            ]
        )
        vehicle_data = f"Vehicle Speed: {simulator.vehicle_speed:.2f} km/h\n"
        axle_data = f"Axle Loads: {simulator.calculate_axle_loads()}"
        data_label.config(text=f"{vehicle_data}\n{axle_data}\n{wheel_data}")

        root.after(100, update_visualization)

    update_visualization()
