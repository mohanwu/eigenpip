# eigenpip: Recent Version of Eigen Library for Python

*Mohan Wu, Martin Lysy*

---

## Description

**eigenpip** is a recent distribution of the [C++ Eigen library](http://eigen.tuxfamily.org/) for Python linking. Some applications of the library can be found in our [Kalman package](https://github.com/mlysy/kalmantv). There are two main functions to **eigenpip**. The first is installing the Eigen library to give access to other Python packages. The second is give the user access to the path of the Eigen library.

## Installation

For a normal installation: 

```bash
git clone https://github.com/mohanwu/eigenpip
cd eigenpip
pip install .
```

If you would like to your own version of the Eigen library then set the environment variable `EIGEN_PATH` to the path of your library. 

On Linux:

```bash
EIGEN_PATH="/ABSOLUTE/PATH/TO/EIGEN/LIBRARY" pip install .
```

On Windows Powershell:

```bash
$env:EIGEN_PATH = "C:\Users\mohan\Documents\kalmantv"; pip install .
```

## Usage

To get the path of the Eigen library:

```Python
import eigenpip

EIGEN_PATH = eigenpip.get_include()
```

