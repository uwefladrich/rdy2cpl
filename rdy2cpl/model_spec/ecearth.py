import logging
from collections import namedtuple

import numpy as np

from rdy2cpl.grib import read as grib_read
from rdy2cpl.grids.base.orca import OrcaTGrid, OrcaUGrid, OrcaVGrid
from rdy2cpl.grids.base.regular import EquidistantLatLonGrid
from rdy2cpl.grids.base.tl import Tl159
from rdy2cpl.grids.base.tco import Tco95, Tco159, Tco319
from rdy2cpl.grids.couple import CoupleGrid

_log = logging.getLogger(__name__)


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
    except (FileNotFoundError, PermissionError):
        _log.error(f'Could not open OIFS mask file "{icmgginit_file}"')
        raise
    oifs_grid.mask = np.where(
        np.logical_or(oifs_masks["lsm"] > 0.5, oifs_masks["cl"] > 0.5), 1, 0
    ).reshape(oifs_grid.shape)


# _base_grid_factory is used below to define all known EC-Earth grids in _ece_grids
# The namedtuple handles the base grid type, together with arguments necessary
# construct, as well as information about the contruction of masks
_base_grid_factory = namedtuple(
    "BaseGridFactory",
    "type type_args type_kwargs mask_modifiers",
    defaults=(
        [],
        {},
        [],
    ),
)

# The _ece_grids dict contains all known EC-Earth grids, by their name as it is
# used in the namcouple file
# The information stored for each grid is:
#   - the base grid type
#   - optional args for the construction of the base grid
#   - optional kwargs for the construction of the base grid
#   - optional sequence of mask-modifying function calls, each item specifying:
#       + the name of the callable (called without arguments), or
#       + a 3-tuple of:
#           * name of the callable
#           * args for the callable
#           * kwargs for the callable
#
# Hence, each base grid is constructed as
#   base_grid = type(*type_args, **type_kwargs)
# and then the mask is constructed as
#   for mm in mask_modifiers:
#       mm(base_grid)
#         -- or --
#       mm[0](base_grid, *mm[1], **mm[2])
_ece_grids = {
    "IOCL": _base_grid_factory(
        Tco95,
        (),
        {},
        ((oifs_read_mask, ("icmgginit",)),),
    ),
    "ILCL": _base_grid_factory(Tco95),
    "IOLL": _base_grid_factory(
        Tl159,
        (),
        {},
        ((oifs_read_mask, ("icmgginit",)),),
    ),
    "ILLL": _base_grid_factory(Tl159),
    "IOCM": _base_grid_factory(Tco159),
    "ILCM": _base_grid_factory(Tco159),
    "IOCH": _base_grid_factory(Tco319),
    "ILCH": _base_grid_factory(Tco319),
    "RNFA": _base_grid_factory(EquidistantLatLonGrid, (512, 256)),
    "NOUM": _base_grid_factory(
        OrcaUGrid,
        ("domain_cfg.nc",),
        {},
        (
            (mask_box, ((36, 48), (46, 56))),  # Caspian sea
            (mask_box, ((41, 48), (27, 43))),  # Black sea
            (mask_box, ((41, 50), (-93, -76))),  # Great lakes
            (mask_box, ((-3, 1), (31.5, 35))),  # Lake Victoria
        ),
    ),
    "NOVM": _base_grid_factory(OrcaVGrid, ("domain_cfg.nc",)),
    "NOTM": _base_grid_factory(OrcaTGrid, ("domain_cfg.nc",)),
}


def couple_grid(name):
    try:
        base_grid = _ece_grids[name].type(
            *_ece_grids[name].type_args, **_ece_grids[name].type_kwargs
        )
    except KeyError:
        _log.error(f"Grid '{name}' is not a known EC-Earth grid")
        raise
    for mm in _ece_grids[name].mask_modifiers or []:
        if callable(mm):
            mm(base_grid)
        else:
            try:
                mm_func = mm[0]
            except TypeError:
                _log.error(
                    f"Wrong type of mask_modifier: '{type(mm)}', should be callable or a list/tuple"
                )
                raise
            mm_args = mm[1] if len(mm) > 1 else []
            mm_kwargs = mm[2] if len(mm) > 2 else {}
            mm_func(base_grid, *mm_args, **mm_kwargs)
    return CoupleGrid(base_grid, name)
