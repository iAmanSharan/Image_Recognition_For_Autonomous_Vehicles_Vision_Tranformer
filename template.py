import logging
import os
from pathlib import Path

Project_name = "Image Recognition For Autonomous Vehicles"

list_of_files = [
    "git/workflows/.gitingore",
    "requirements.txt",
    "config.yaml",
    f"src/{Project_name}/__init__.py",
    f"src/{Project_name}/logging/logger.py",
    f"src/{Project_name}/Exception/exception.py",
    f"src/{Project_name}/components/__init__.py"
]

for filepath in list_of_files:
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    Path(filepath).touch()
    logging.info(f"{filepath} created")

    