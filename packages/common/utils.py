from pathlib import Path


def ensure_dir(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)


def project_root():
    return Path(__file__).resolve().parents[2]
