from setuptools import setup, find_packages
import os

# Read README.md safely
try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except:
    long_description = "A text summarization project"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "Santanu"
SRC_REPO = "text_summarizer"
AUTHOR_EMAIL = "dassantanubnk@gmail.com"

setup(
    name=SRC_REPO,
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "transformers",
        "datasets",
        "sacrebleu",
        "rouge-score",
        "py7zr",
        "pandas",
        "nltk",
        "tqdm",
        "PyYAML",
        "matplotlib",
        "torch",
        "notebook",
        "boto3",
        "mypy-boto3-s3",
        "python-box",
        "ensure",
        "fastapi",
        "uvicorn",
        "Jinja2"
    ],
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text summarization project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    python_requires=">=3.8,<3.14",  # Updated to allow Python 3.13
)
