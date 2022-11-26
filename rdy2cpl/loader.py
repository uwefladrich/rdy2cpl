import os
import sys


def import_pyoasis():
    """Imports and returns the pyoasis module, which is usually not available
    for a simple Python import command.
    Relies on environment variables:
    - OASIS_BUILD_PATH pointing to the OASIS build path, and
    - LD_LIBRARY_PATH containing ${OASIS_BUILD_PATH}/lib
    an ImportError is thrown if one of the above is missing
    """
    try:
        oasis_build_path = os.environ["OASIS_BUILD_PATH"]
    except KeyError:
        raise ImportError("OASIS_BUILD_PATH not set")

    if "LD_LIBRARY_PATH" not in os.environ:
        raise ImportError("LD_LIBRARY_PATH not set")

    if oasis_build_path + "/lib" not in os.environ["LD_LIBRARY_PATH"]:
        raise ImportError("OASIS build path not in LD_LIBRARY_PATH")

    sys.path.append(oasis_build_path + "/python")

    import pyoasis

    return pyoasis
