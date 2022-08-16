import logging
import sys

import yaml
from mpi4py import MPI

import pyoasis
from rdy2cpl.leader import lead
from rdy2cpl.namcouple import from_dict, reduce
from rdy2cpl.worker import work

_log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def do_nothing(rank):
    _log.warning(f"Rank {rank} not needed")
    pyoasis.Component(f"noacct{rank:02}", coupled=False)


def main():

    with open(sys.argv[1]) as f:
        namcouple = reduce(from_dict(yaml.load(f, Loader=yaml.FullLoader)))

    global_rank = MPI.COMM_WORLD.Get_rank()
    global_size = MPI.COMM_WORLD.Get_size()

    i_am_leader = global_rank == 0
    i_am_worker = 0 < global_rank <= len(namcouple.links)

    if i_am_leader:
        if global_size <= len(namcouple.links):
            _log.error(
                f"Not enough workers ({len(namcouple.links)} needed, {global_size-1} present)"
            )
            raise RuntimeError("Not enough workers")
        with open("namcouple", "w") as f:
            f.write(namcouple.out)

    MPI.COMM_WORLD.Barrier()

    if i_am_leader:
        lead(namcouple.links)

    elif i_am_worker:
        work(global_rank - 1, namcouple.links[global_rank - 1])

    else:
        do_nothing(global_rank)


if __name__ == "__main__":
    main()
