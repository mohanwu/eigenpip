import os.path

def get_include():
    """
    Returns the path to the Eigen directory.
    """
    try:
        import eigenpip
        return os.path.join(eigenpip.__path__[0], "eigen")
    except ImportError as e:
        msg = """The get_include() path will not be correct if you import eigenpip
        from its source directory; please exit the eigenpip source tree, and relaunch
        your python interpreter if you need to use eigenpip.get_include()."""
        raise ImportError(msg) from e