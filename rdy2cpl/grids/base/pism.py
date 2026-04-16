import numpy as np
from netCDF4 import Dataset


class PismGrid:
    """PISM rectilinear grid read from a reference NetCDF file.

    Reads 2D lon/lat fields and their corner bounds directly from
    the file, and computes uniform cell areas from the projected
    grid spacing (stereographic x/y coordinates).
    """

    def __init__(self, ref_file, mask_var="land_ice_area_fraction_retreat"):
        with Dataset(ref_file) as nc:
            # Transpose from NetCDF (y,x) to Fortran/OASIS (x,y) order
            self.center_longitudes = nc["lon"][...].data.copy().T
            self.center_latitudes = nc["lat"][...].data.copy().T
            self.corner_longitudes = np.transpose(
                nc["lon_bnds"][...].data.copy(), (1, 0, 2)
            )
            self.corner_latitudes = np.transpose(
                nc["lat_bnds"][...].data.copy(), (1, 0, 2)
            )
            x = nc["x"][...].data
            y = nc["y"][...].data
            if mask_var and mask_var in nc.variables:
                self._mask_data = nc[mask_var][...].data.copy().T
            else:
                self._mask_data = None

        dx = float(np.abs(np.diff(x)).mean())
        dy = float(np.abs(np.diff(y)).mean())
        nx, ny = self.center_longitudes.shape
        self.shape = (nx, ny)
        self.size = nx * ny
        self.areas = np.full((nx, ny), dx * dy)
        self.mask = np.zeros((nx, ny), dtype="int32")
