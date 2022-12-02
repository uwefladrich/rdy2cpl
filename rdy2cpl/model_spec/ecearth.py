import logging
from collections import namedtuple

from rdy2cpl.grids.base.orca import OrcaTGrid, OrcaUGrid, OrcaVGrid
from rdy2cpl.grids.base.regular import EquidistantLatLonGrid
from rdy2cpl.grids.base.tco import Tco95, Tco159, Tco319
from rdy2cpl.grids.couple import CoupleGrid

_log = logging.getLogger(__name__)

# The _base_grid_factory returns a base grid as constructed by:
#   base_grid = type(*args, **kwargs)
# The base_grid's mask is then modified by applying the functions in
# 'mask_mod' by calling
#   for mm in mask_mod:
#       mm(base_grid)
# See function 'couple_grid()' below
_base_grid_factory = namedtuple(
    "BaseGridFactory",
    "type args kwargs mask_mod",
    defaults=(
        [],
        {},
        [],
    ),
)

_ece_grids = {
    "IOCL": _base_grid_factory(Tco95),
    "ILCL": _base_grid_factory(Tco95),
    "IOCM": _base_grid_factory(Tco159),
    "ILCM": _base_grid_factory(Tco159),
    "IOCH": _base_grid_factory(Tco319),
    "ILCH": _base_grid_factory(Tco319),
    "RNFA": _base_grid_factory(EquidistantLatLonGrid, (360, 180)),
    "NOUM": _base_grid_factory(OrcaUGrid, ("domain_cfg.nc",)),
    "NOVM": _base_grid_factory(OrcaVGrid, ("domain_cfg.nc",)),
    "NOTM": _base_grid_factory(OrcaTGrid, ("domain_cfg.nc",)),
}


def couple_grid(name):
    try:
        base_grid = _ece_grids[name].type(
            *_ece_grids[name].args, **_ece_grids[name].kwargs
        )
    except KeyError:
        _log.error(f'Grid id "{name}" not found in the assign map')
        raise
    for mm in _ece_grids[name].mask_mod or []:
        base_grid.mask = mm(base_grid.mask)
    return CoupleGrid(base_grid, name)
