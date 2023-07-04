import argparse
import logging

from mpi4py import MPI

from rdy2cpl.grids.couple_grid import from_model_spec
from rdy2cpl.loader import pyoasis
from rdy2cpl.namcouple.factory import from_yaml

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
        help="only create namcouple file",
        action="store_true",
        dest="namcouple_only",
    )
    mgroup.add_argument(
        "-r",
        "--reduced-namcouple",
        help="only create the reduced namcouple file (distinct links only)",
        action="store_true",
        dest="reduced_namcouple_only",
    )
    parser.add_argument(
        "spec_file",
        help="YAML file with namcouple specification",
    )
    return parser.parse_args()


def main(
    spec_file,
    *,
    print_number_of_links,
    namcouple_only,
    reduced_namcouple_only,
):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    try:
        with open(spec_file) as f:
            namcouple_spec = f.read()
    except OSError as e:
        _log.error(f"Could not open/read namcouple spec file: {e}")
        return
    namcouple = from_yaml(namcouple_spec)

    if namcouple_only:
        if rank == 0:
            _log.info("Writing namcouple file")
            try:
                namcouple.save()
            except OSError as e:
                _log.error(f"Could not write namcouple file: {e}")
        return

    reduced_namcouple = namcouple.reduced()

    if print_number_of_links:
        if rank == 0:
            print(reduced_namcouple.num_links)
        return

    if rank == 0:
        try:
            _log.info("Writing reduced namcouple file")
            namcouple.reduced().save()
        except OSError as e:
            _log.error(f"Could not write reduced namcouple file: {e}")
            return

    if reduced_namcouple_only:
        return

    if reduced_namcouple.num_links > size:
        raise RuntimeError(
            f"Not enough MPI processes: {reduced_namcouple.num_links} needed, {size} present"
        )
    comm.Barrier()

    if rank < reduced_namcouple.num_links:
        link = reduced_namcouple.links[rank]
        _log.info(
            f"MPI process {rank} processing link "
            f"{link.source.grid.name} --> {link.target.grid.name}"
        )
        oasis_component = pyoasis.Component(f"worker{rank:02}")

        cpl_grid_source = from_model_spec(link.source.grid.name)
        cpl_grid_target = from_model_spec(link.target.grid.name)

        cpl_grid_source.write()
        cpl_grid_target.write()

        pyoasis.Var(f"VAR_{rank:02}_S", cpl_grid_source.partition, pyoasis.OASIS.OUT)
        pyoasis.Var(f"VAR_{rank:02}_T", cpl_grid_target.partition, pyoasis.OASIS.IN)

        oasis_component.enddef()
        del oasis_component

        if rank == 0:
            _log.info("Writing final namcouple file")
            namcouple.save()

    else:
        _log.warning(f"MPI process {rank}: no link to process for me")
        pyoasis.Component(f"noacct{rank:02}", coupled=False)


def main_cli():
    args = parse_cmdl_args()
    main(**vars(args))


if __name__ == "__main__":
    main_cli()
