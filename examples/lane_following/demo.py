import matplotlib.pyplot as plt

from packages.common.logger import setup_logger
from packages.common.utils import ensure_dir, project_root
from packages.planning.planner import Planner

logger = setup_logger("AutoDriveStack")


def main():
    logger.info("Starting AutoDriveStack demo...")

    planner = Planner(start_x=0.0, start_y=0.0, target_x=120.0, target_y=0.0, step=0.5)
    path = planner.generate_path()

    if not path:
        logger.error("No trajectory generated.")
        return

    xs = [p[0] for p in path]
    ys = [p[1] for p in path]

    root = project_root()
    output_dir = root / "data" / "samples"
    ensure_dir(str(output_dir))

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(xs, ys, label="Reference path", color="tab:blue", linewidth=2)
    ax.scatter(xs[0], ys[0], color="green", s=50, label="Start")
    ax.scatter(xs[-1], ys[-1], color="red", s=50, label="Target")
    ax.set_title("AutoDriveStack - Lane Following Demo")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()

    output_path = output_dir / "demo_path.png"
    plt.savefig(output_path)
    logger.info(f"Saved demo plot to: {output_path}")

    print(f"Demo path points: {len(path)}")
    print(f"Plot saved to: {output_path}")


if __name__ == "__main__":
    main()
