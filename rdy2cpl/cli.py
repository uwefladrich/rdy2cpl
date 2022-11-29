import argparse
import logging

import yaml
from mpi4py import MPI

from rdy2cpl.loader import import_pyoasis

pyoasis = import_pyoasis()

from rdy2cpl.namcouple import from_dict, reduce
from rdy2cpl.worker import work

_log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def do_nothing(rank):
    _log.warning(f"Rank {rank} not needed")
    pyoasis.Component(f"noacct{rank:02}", coupled=False)


def parse_cmdl_args():
    parser = argparse.ArgumentParser(
        description="Ready2couple: A tool to set up OASIS3-MCT coupling",
        epilog="(c) 2022 Uwe Fladrich, see LICENSE file or https://github.com/uwefladrich/rdy2cpl",
    )
    parser.add_argument(
        "-l",
        "--num-links",
        help="print number of *distinc* coupling links",
        action="store_true",
    )
    mutual_exclusive = parser.add_mutually_exclusive_group()
    mutual_exclusive.add_argument(
        "-n",
        "--namcouple",
        help="create namcouple file",
        action="store_true",
    )
    mutual_exclusive.add_argument(
        "-r",
        "--reduced-namcouple",
        help="create the reduced namcouple file (distinct links only)",
        action="store_true",
    )
    parser.add_argument(
        "-g",
        "--grids",
        help="create OASIS grid files (grids, masks, areas)",
        action="store_true",
    )
    parser.add_argument(
        "-w",
        "--weights",
        help=(
            "create remapping weight files for all distinct links "
            "(implies --grids)"
        ),
        action="store_true",
    )
    parser.add_argument(
        "namcouple_spec",
        help="YAML file with namcouple specification",
    )
    return parser.parse_args()


def main(namcouple_spec):

    with open(namcouple_spec) as f:
        namcouple = reduce(from_dict(yaml.load(f, Loader=yaml.FullLoader)))

    global_rank = MPI.COMM_WORLD.Get_rank()
    global_size = MPI.COMM_WORLD.Get_size()

    i_am_worker = 0 <= global_rank < len(namcouple.links)

    if global_size < len(namcouple.links):
        _log.error(
            f"Not enough workers ({len(namcouple.links)} needed, {global_size} present)"
        )
        raise RuntimeError("Not enough workers")

    with open("namcouple", "w") as f:
        f.write(namcouple.out)

    MPI.COMM_WORLD.Barrier()

    if i_am_worker:
        work(global_rank, namcouple.links[global_rank])

    else:
        do_nothing(global_rank)


def main_cli():
    main_cli(**parse_cmdl_args())


if __name__ == "__main__":
    main_cli()
