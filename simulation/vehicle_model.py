class VehicleModel:
    def __init__(self, mass):
        self.mass = mass

    def calculate_deceleration(self, brake_force):
        return brake_force / self.mass
