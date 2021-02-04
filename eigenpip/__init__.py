import os.path

def get_include():
    """
    Returns the path to the Eigen directory.
    """
    import eigenpip
    return os.path.join(eigenpip.__path__[0], "eigen")
    