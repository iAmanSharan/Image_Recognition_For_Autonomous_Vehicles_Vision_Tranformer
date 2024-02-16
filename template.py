import logging
import os
from pathlib import Path

Project_name = "Image_Recognition_For_Autonomous_Vehicles"

list_of_files = [
    ".github/workflows/.gitkeep",
    "requirements.txt",
    "config.yaml",
    f"src/{Project_name}/__init__.py",
    f"src/{Project_name}/logging/logger.py",
    f"src/{Project_name}/Exception/exception.py",
    f"src/{Project_name}/components/__init__.py",
    f"src/{Project_name}/utils/__init__.py",
    f"src/{Project_name}/utils/common.py",
    f"src/{Project_name}/pipeline/__init__.py",
    "research/trials.ipynb",
    "setup.py",
    "params.yaml",
    "config/config.yaml"
]

for filepath in list_of_files:
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    Path(filepath).touch()
    logging.info(f"{filepath} created")

    