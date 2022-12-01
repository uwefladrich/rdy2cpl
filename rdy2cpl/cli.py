import argparse
import logging

import yaml
from mpi4py import MPI

from rdy2cpl.loader import import_pyoasis

pyoasis = import_pyoasis()

from rdy2cpl.namcouple import from_dict, reduce
from rdy2cpl.grids.assign import couple_grid

_log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def parse_cmdl_args():
    parser = argparse.ArgumentParser(
        description=(
            "Ready2couple: Automatic OASIS3-MCT coupling set up\n\n"
            "The r2c command creates the OASIS namcouple file, grid description\n"
            "files (grids.nc, masks.nc, areas.nc), and remapping weight files\n"
            "(rmp_*.nc) for a given coupling specification, given as a YAML file."
        ),
        epilog=(
            "If none of the options if given, everything is created: namcouple,\n"
            "grid description files, and remapping weights.\n\n"
            "IMPORTANT: r2c needs a working OASIS3-MCT installation, including\n"
            "the pyOASIS API. Two environment variables must to be set:\n\n"
            "  OASIS_BUILD_PATH: points to the OASIS *build* directory\n"
            "  LD_LIBRARY_PATH: needs to include ${OASIS_BUILD_PATH}/lib\n\n"
            "(c) 2022 Uwe Fladrich, see LICENSE file or https://github.com/uwefladrich/rdy2cpl"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    mgroup = parser.add_mutually_exclusive_group()
    mgroup.add_argument(
        "-l",
        "--num-links",
        help="print number of *distinc* coupling links",
        action="store_true",
        dest="print_num_links",
    )
    mgroup.add_argument(
        "-n",
        "--namcouple",
        help="create namcouple file",
        action="store_true",
    )
    mgroup.add_argument(
        "-r",
        "--reduced-namcouple",
        help="create the reduced namcouple file (distinct links only)",
        action="store_true",
    )
    mgroup.add_argument(
        "-g",
        "--grids",
        help="create namcouple and grid files (grids, masks, areas)",
        action="store_true",
    )
    parser.add_argument(
        "namcouple_spec",
        help="YAML file with namcouple specification",
    )
    return parser.parse_args()


def main(namcouple_spec, print_num_links=False, reduced_namcouple=False):

    with open(namcouple_spec) as f:
        namcouple = reduce(from_dict(yaml.load(f, Loader=yaml.FullLoader)))

    num_links = len(namcouple.links)

    if print_num_links:
        print(num_links)
        return

    rank = MPI.COMM_WORLD.Get_rank()
    size = MPI.COMM_WORLD.Get_size()

    if not reduced_namcouple and num_links > size:
        raise RuntimeError(
            f"Not enough MPI processes: {num_links} needed, {size} present"
        )

    if rank == 0:
        with open("namcouple", "w") as f:
            f.write(namcouple.out)
    MPI.COMM_WORLD.Barrier()

    if reduced_namcouple:
        return

    if rank < num_links:
        link = namcouple.links[rank]
        _log.info(
            f"MPI process {rank} processing link "
            f"{link.source.grid.name} --> {link.target.grid.name}"
        )
        oasis_component = pyoasis.Component(f"worker{rank:02}")

        cpl_grid_source = couple_grid(link.source.grid.name)
        cpl_grid_target = couple_grid(link.target.grid.name)

        cpl_grid_source.write()
        cpl_grid_target.write()

        pyoasis.Var(f"VAR_{rank:02}_S", cpl_grid_source.partition, pyoasis.OASIS.OUT)
        pyoasis.Var(f"VAR_{rank:02}_T", cpl_grid_target.partition, pyoasis.OASIS.IN)

        oasis_component.enddef()
        del oasis_component

    else:
        _log.warning(f"MPI process {rank}: no link to process for me")
        pyoasis.Component(f"noacct{rank:02}", coupled=False)


def main_cli():
    args = parse_cmdl_args()
    main(args.namcouple_spec, args.print_num_links, args.reduced_namcouple)


if __name__ == "__main__":
    main_cli()
