import os
from pathlib import Path


DATA_ROOT = Path(os.environ.get("BAXMAXX_DATA", "/data/BAXMAXX"))
MODELS_ROOT = Path(os.environ.get("BAXMAXX_MODELS", "/data/BAXMAXX_models"))

PROJECT_ROOT = Path(__file__).resolve().parent
FIGURES_DIR = PROJECT_ROOT / "figures"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"


def ensure_dirs() -> None:
    for path in [FIGURES_DIR, NOTEBOOKS_DIR, SCRIPTS_DIR]:
        path.mkdir(parents=True, exist_ok=True)


ensure_dirs()
