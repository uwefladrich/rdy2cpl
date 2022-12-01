import argparse
import logging

from mpi4py import MPI

from rdy2cpl.loader import import_pyoasis

pyoasis = import_pyoasis()

from rdy2cpl.grids.assign import couple_grid
from rdy2cpl.namcouple import (
    number_of_links,
    read_namcouple_spec,
    reduce,
    write_namcouple,
)

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
        dest="print_number_of_links",
    )
    mgroup.add_argument(
        "-n",
        "--namcouple",
        help="create namcouple file",
        action="store_true",
        dest="namcouple_only",
    )
    mgroup.add_argument(
        "-r",
        "--reduced-namcouple",
        help="create the reduced namcouple file (distinct links only)",
        action="store_true",
        dest="reduced_namcouple_only",
    )
    #   mgroup.add_argument(
    #       "-g",
    #       "--grids",
    #       help="create namcouple and grid files (grids, masks, areas)",
    #       action="store_true",
    #       dest="grids_only",
    #   )
    parser.add_argument(
        "namcouple_spec",
        help="YAML file with namcouple specification",
    )
    return parser.parse_args()


def main(
    namcouple_spec,
    *,
    print_number_of_links,
    namcouple_only,
    reduced_namcouple_only,
    #   grids_only,
):

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if namcouple_only:
        if rank == 0:
            write_namcouple(read_namcouple_spec(namcouple_spec))
        return

    reduced_namcouple = reduce(read_namcouple_spec(namcouple_spec))
    num_links = number_of_links(reduced_namcouple)

    if print_number_of_links:
        if rank == 0:
            print(num_links)
        return

    if rank == 0:
        write_namcouple(reduced_namcouple)

    if reduced_namcouple_only:
        return

    if num_links > size:
        raise RuntimeError(
            f"Not enough MPI processes: {num_links} needed, {size} present"
        )
    comm.Barrier()

    if rank < num_links:
        link = reduced_namcouple.links[rank]
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
    main(**vars(args))


if __name__ == "__main__":
    main_cli()
