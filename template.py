import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "text_summarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    ".gitattributes",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")



    else:
        logging.info(f"{filename} already exists")


gitattributes_content = """\
# Normalize line endings
* text=auto

# Force LF for specific files
*.py text eol=lf
*.ipynb text eol=lf
*.sh text eol=lf
*.yaml text eol=lf
*.yml text eol=lf
*.json text eol=lf
*.txt text eol=lf
*.md text eol=lf
*.csv text eol=lf
*.tsv text eol=lf
*.ini text eol=l
"""

if filepath.name == ".gitattributes" and filepath.stat().st_size == 0:
    filepath.write_text(gitattributes_content)
