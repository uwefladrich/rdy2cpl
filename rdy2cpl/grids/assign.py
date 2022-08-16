import logging
from collections import namedtuple

from rdy2cpl.grids.base.orca import OrcaTGrid, OrcaUGrid, OrcaVGrid
from rdy2cpl.grids.base.regular import EquidistantLatLonGrid
from rdy2cpl.grids.base.tco import Tco95
from rdy2cpl.grids.couple import CoupleGrid

_log = logging.getLogger(__name__)

_bgf = namedtuple(
    "BaseGridFactory",
    "type, args, kwargs, mask_mod",
    defaults=(
        [],
        {},
        [],
    ),
)

_map = {
    "IOCL": _bgf(Tco95),
    "ILCL": _bgf(Tco95),
    "RNFA": _bgf(EquidistantLatLonGrid, (360, 180)),
    "NOUM": _bgf(OrcaUGrid, ("examples/domain_cfg.nc",)),
    "NOVM": _bgf(OrcaVGrid, ("examples/domain_cfg.nc",)),
    "NOTM": _bgf(OrcaTGrid, ("examples/domain_cfg.nc",)),
}


def couple_grid(name):
    try:
        base_grid = _map[name].type(*_map[name].args, **_map[name].kwargs)
    except KeyError:
        _log.error(f'Grid id "{name}" not found in the assign map')
        raise
    for mm in _map[name].mask_mod or []:
        base_grid.mask = mm(base_grid.mask)
    return CoupleGrid(base_grid, name)
