from typing import List, Tuple


def generate_lane_trajectory(
    start_x: float = 0.0,
    start_y: float = 0.0,
    target_x: float = 120.0,
    target_y: float = 0.0,
    step: float = 0.5,
) -> List[Tuple[float, float]]:
    points: List[Tuple[float, float]] = []
    x = start_x
    y = start_y

    while x <= target_x:
        points.append((x, y))
        x += step
        y += 0.02 * (x / 10.0)

    return points
