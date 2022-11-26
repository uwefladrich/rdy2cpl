import logging

from rdy2cpl.loader import import_pyoasis

pyoasis = import_pyoasis()

from rdy2cpl.grids.assign import couple_grid

_log = logging.getLogger(__name__)


def work(id, link):
    _log.info(f"Started id {id} for link end point grid {link.source.grid.name}")

    oas_component = pyoasis.Component(f"worker{id:02}")

    cpl_grid_source = couple_grid(link.source.grid.name)
    cpl_grid_source.write()
    pyoasis.Var(f"VAR_{id:02}_S", cpl_grid_source.partition, pyoasis.OASIS.OUT)

    cpl_grid_target = couple_grid(link.target.grid.name)
    cpl_grid_target.write()
    pyoasis.Var(f"VAR_{id:02}_T", cpl_grid_target.partition, pyoasis.OASIS.IN)

    oas_component.enddef()
