import os
import sys


def _import_pyoasis():
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
        raise ImportError(
            "Missing OASIS_BUILD_PATH: set this environmane variable "
            "to point to the OASIS *build* directory!"
        ) from None

    if "LD_LIBRARY_PATH" not in os.environ:
        raise ImportError(
            "Missing LD_LIBRARY_PATH: Make sure it is set and includes ${OASIS_BUILD_PATH}/lib!"
        )

    if oasis_build_path + "/lib" not in os.environ["LD_LIBRARY_PATH"]:
        raise ImportError(
            "Incomplete LD_LIBRARY_PATH: Make sure it includes ${OASIS_BUILD_PATH}/lib!"
        )

    sys.path.append(oasis_build_path + "/python")

    try:
        import pyoasis
    except ModuleNotFoundError:
        raise ModuleNotFoundError(
            "Module 'pyoasis' not found. Maybe OASIS is not build with support for "
            "pyOASIS or the OASIS_BUILD_PATH does not point to the correct OASIS "
            "*build* directory?"
        ) from None

    return pyoasis


pyoasis = _import_pyoasis()


class _noStdout:
    """A context manager that swallows stdout"""

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self

    def __exit__(self, type, value, traceback):
        sys.stdout = self.stdout
        if type is not None:
            raise

    def write(self, x):
        pass

    def flush(self):
        pass


def _import_eccodes():
    """Prevent eccodes from writing directly to stdout during import"""
    with _noStdout():
        import eccodes

    return eccodes


eccodes = _import_eccodes()
