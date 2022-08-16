import logging

import pyoasis
from rdy2cpl.grids.assign import couple_grid

_log = logging.getLogger(__name__)


def work(id, link):
    _log.info(f"Started id {id} for link end point grid {link.source.grid.name}")

    oas_component = pyoasis.Component(f"worker{id:02}")

    cpl_grid = couple_grid(link.source.grid.name)
    cpl_grid.write()

    pyoasis.Var(f"VAR_{id:02}_S", cpl_grid.partition, pyoasis.OASIS.OUT)

    oas_component.enddef()
