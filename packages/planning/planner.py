from packages.planning.trajectory import generate_lane_trajectory


class Planner:
    def __init__(self, start_x=0.0, start_y=0.0, target_x=120.0, target_y=0.0, step=0.5):
        self.start_x = start_x
        self.start_y = start_y
        self.target_x = target_x
        self.target_y = target_y
        self.step = step

    def generate_path(self):
        return generate_lane_trajectory(
            start_x=self.start_x,
            start_y=self.start_y,
            target_x=self.target_x,
            target_y=self.target_y,
            step=self.step,
        )
