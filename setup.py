from setuptools import find_packages, setup

# it'll search for every __init__.py file in each folder then install that folder as local package
setup(
    name="signLanguages",
    version="0.0.0",
    author="MEmam",
    author_email="aurion1982@gmail.com",
    packages=find_packages(),
    install_requires=[]
)