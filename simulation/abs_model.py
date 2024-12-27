class ABSSimulator:
    def __init__(self):
        # Vehicle parameters
        self.vehicle_mass = 12000.0  # kg
        self.static_mass_distribution = [0.6, 0.4]  # Front vs Rear
        self.track_width = 2.5  # meters
        self.wheel_base = 6.0  # meters
        self.tire_radius = 0.6  # meters
        self.tire_width = 0.35  # meters

        # Road and tire parameters
        self.road_friction = [0.8, 0.8, 0.8, 0.8]  # Per wheel
        self.global_friction = 0.8  # Overall road friction

        # Dynamic parameters
        self.vehicle_speed = 80.0  # km/h
        self.wheel_speeds = [80.0, 80.0, 80.0, 80.0]  # km/h (FL, FR, RL, RR)
        self.brake_torques = [0.0, 0.0, 0.0, 0.0]  # Nm (FL, FR, RL, RR)
        self.brake_forces = [0.0, 0.0, 0.0, 0.0]  # N
        self.slip_ratios = [0.0, 0.0, 0.0, 0.0]  # %

        # Input controls
        self.brake_pedal_input = 0.0  # 0 to 1 scale

    def update(self):
        # Calculate brake force and torque
        max_brake_force = self.brake_pedal_input * self.vehicle_mass * 9.81
        axle_loads = self.calculate_axle_loads()

        for i, load in enumerate(axle_loads):
            available_friction = self.road_friction[i] * load
            self.brake_forces[i] = min(max_brake_force / 4, available_friction)
            self.brake_torques[i] = self.brake_forces[i] * self.tire_radius

        # Update speeds and slip ratios
        deceleration = sum(self.brake_forces) / self.vehicle_mass
        self.vehicle_speed = max(0, self.vehicle_speed - deceleration * 0.1)

        for i in range(4):
            wheel_deceleration = self.brake_forces[i] / (self.vehicle_mass / 4)
            self.wheel_speeds[i] = max(0, self.wheel_speeds[i] - wheel_deceleration * 0.1)
            self.slip_ratios[i] = (
                (self.vehicle_speed - self.wheel_speeds[i]) / max(self.vehicle_speed, 0.1)
            ) * 100

    def calculate_axle_loads(self):
        rear_load = self.vehicle_mass * self.static_mass_distribution[1] * 9.81
        front_load = self.vehicle_mass * self.static_mass_distribution[0] * 9.81
        return [front_load / 2, front_load / 2, rear_load / 2, rear_load / 2]
