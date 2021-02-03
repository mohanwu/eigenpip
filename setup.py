from setuptools import setup, find_packages
import os
import eigenpip

# path to eigen library
EIGEN_PATH = None

if EIGEN_PATH is None:
    EIGEN_PATH = eigenpip.__eigen_dir__

def package_files(directory):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths

extra_files = package_files(EIGEN_PATH)

setup(
    name="eigenpip",
    version="0.1",
    author="Mohan Wu, Martin Lysy",
    author_email="mhwu@uwaterloo.ca",
    description="Eigen Library for Python Linking",
    url="http://github.com/mohanwu/eigenpip",
    packages = ["eigenpip", "eigenpip/eigen"],
    package_dir={"eigenpip/eigen": EIGEN_PATH},
    package_data={
        "eigenpip/eigen": extra_files
    },
)
