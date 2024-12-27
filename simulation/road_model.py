class RoadModel:
    def __init__(self, friction):
        self.friction = friction

    def max_deceleration(self):
        return self.friction * 9.81
