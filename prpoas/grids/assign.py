import logging
from collections import namedtuple

from prpoas.grids.base.orca import OrcaTGrid, OrcaUGrid, OrcaVGrid
from prpoas.grids.base.regular import EquidistantLatLonGrid
from prpoas.grids.base.tco import Tco159
from prpoas.grids.couple import CoupleGrid

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
    "IOCL": _bgf(Tco159),
    "ILCL": _bgf(Tco159),
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
