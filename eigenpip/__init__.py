from pkg_resources import resource_filename
import numpy as np
import os.path

__eigen_dir__ = resource_filename(__name__, "eigen-3.3.9")

def get_include():
    """
    Returns the path to the Eigen directory.
    """
    try:
        import eigenpip
        return eigenpip.__path__[0]
    except ImportError as e:
        msg = """The get_include() path will not be correct if you import eigenpip
        from its source directory; please exit the eigenpip source tree, and relaunch
        your python interpreter if you need to use eigenpip.get_include()."""
        raise ImportError(msg) from e