import logging

import pyoasis
from rdy2cpl.grids.assign import couple_grid

_log = logging.getLogger(__name__)


def lead(links):
    _log.info("Started")

    oas_comp = pyoasis.Component("leader")
    for n, l in enumerate(links):
        _log.info(f"Processing link number {n} for grid {l.target.grid.name}")
        cpl_grid = couple_grid(l.target.grid.name)
        cpl_grid.write()
        pyoasis.Var(f"VAR_{n:02}_T", cpl_grid.partition, pyoasis.OASIS.IN)
    oas_comp.enddef()
