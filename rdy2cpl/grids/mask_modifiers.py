import logging

import numpy as np
from netCDF4 import Dataset

from rdy2cpl.grib import read as grib_read

_log = logging.getLogger(__name__)


def invert_mask(grid):
    grid.mask = np.where(grid.mask == 1, 0, 1)


def mask_box(grid, lats, lons):
    "Masks a box spanned by corners (lats[0], lons[0]) and (lats[1], lons[1])"
    grid.mask = np.where(
        (
            (grid.center_longitudes >= lons[0])
            & (grid.center_longitudes <= lons[1])
            & (grid.center_latitudes >= lats[0])
            & (grid.center_latitudes <= lats[1])
        ),
        1,
        grid.mask,
    )


def oifs_read_mask(oifs_grid, icmgginit_file="icmgginit"):
    """Reads 'lsm' and 'cl' from the icmgginit GRIB file and masks all points
    where either 'lsm' or 'cl' is greater than 0.5
    """
    try:
        oifs_masks = grib_read(icmgginit_file, ("lsm", "cl"))
    except (FileNotFoundError, PermissionError) as e:
        _log.error(f'Could not open OIFS mask file "{icmgginit_file}"')
        raise e from None
    oifs_grid.mask = np.where(
        np.logical_or(oifs_masks["lsm"] > 0.5, oifs_masks["cl"] > 0.5), 1, 0
    ).reshape(oifs_grid.shape)


def rnfm_read_mask(rnfm_grid, runoff_mapper_file="runoff_maps.nc"):
    """Reads runoff-mapper file and derives mask from drainage basin ids"""
    try:
        with Dataset(runoff_mapper_file) as nc:
            dbi = nc["drainage_basin_id"][...].T
    except OSError as e:
        _log.error(f"Could not open/read the runoff-mapper file: {e}")
        raise e from None
    except KeyError as e:
        _log.error(
            f"Could not find variable 'drainage_basin_id' in the runoff-mapper file"
        )
        raise e from None
    # convention is that ocean has id==-2
    rnfm_grid.mask = np.where(dbi == -2, 1, 0)
