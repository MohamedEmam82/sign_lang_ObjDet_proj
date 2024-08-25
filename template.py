
import os
from pathlib import Path
import logging


'''
# why use __init__.py file?
https://sarangsurve.medium.com/python-basics-why-use-init-py-c88589e44c91#:~:text=__init__.py%20allows,foundation%20for%20your%20packages'%20functionality.

# why use .gitignore folder?
https://www.w3schools.com/git/git_ignore.asp?remote=github#:~:text=Git%20can%20specify%20which%20files,and%20folders%20specified%20in%20.gitignore%20.

# why use .gitkeep folder?
https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/gitkeep-push-empty-folders-git-commit#:~:text=The%20purpose%20of%20the%20.,gitkeep%20in%20it.
'''

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

project_name = "sign_language"

list_of_files = [

    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    "docs/.gitkeep"
    "template/index.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",

    f"{project_name}/__init__.py",

    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",

    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",

    f"{project_name}/constant/__init__py",
    f"{project_name}/constant/training_pipeline/__init__py",
    f"{project_name}/constant/application.py",

    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/entity/config_entity.py",

    f"{project_name}/exception/__init__.py",

    f"{project_name}/logger/__init__.py",

    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",

    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
]


for filepath in list_of_files:

    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file {filename}")
