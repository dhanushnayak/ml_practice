import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "mlProject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utlis/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    f"config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html",
]

for files in list_of_files:
    filepth =  Path(files)
    filedir, filename =  os.path.split(filepth)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory; {filedir} for the files: {filename}")

    if (not os.path.exists(filepth)) or (os.path.getsize(filepth)==0):
        with open(filepth,"w") as f: pass
        logging.info(f"Creating empty file: {filepth}")
    else: 
        logging.info(f"{filename} already exists")