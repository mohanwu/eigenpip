from setuptools import setup, find_packages
import os
import eigenpip

# path to eigen library
EIGEN_PATH = os.environ.get("EIGEN_PATH", None)

def package_files(directory):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths

if EIGEN_PATH is None:
    EIGEN_VER = "-3.3.7"
    EIGEN_PATH = eigenpip.get_include()+EIGEN_VER

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
