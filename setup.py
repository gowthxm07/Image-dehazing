from setuptools import setup, find_packages

setup(
    name="image_dehazing_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pillow",
        "matplotlib",
    ],
)
