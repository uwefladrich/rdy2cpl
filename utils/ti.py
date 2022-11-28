import sys

import numpy as np
import yaml

from rdy2cpl.loader import import_pyoasis

pyoasis = import_pyoasis()

from rdy2cpl.grids.assign import couple_grid
from rdy2cpl.namcouple import from_dict


def read_cpl_info(fname, write_namecouple=False):
    with open(fname) as f:
        namcouple = from_dict(yaml.load(f, yaml.SafeLoader))
    if write_namecouple:
        with open("namcouple", "w") as f:
            f.write(namcouple.out)
    return (
        namcouple.links[0].source.grid.name,
        namcouple.links[0].target.grid.name,
    )


def test_func_ones(lats, lons):
    return pyoasis.asarray(np.ones_like(lats))


def main(cpl_info_file):

    src_name, dst_name = read_cpl_info(cpl_info_file, write_namecouple=True)

    oasis_component = pyoasis.Component("INTERPOLTEST")
    src_grid = couple_grid(src_name)
    dst_grid = couple_grid(dst_name)

    src_var = pyoasis.Var("vsrc", src_grid.partition, pyoasis.OASIS.OUT)
    dst_var = pyoasis.Var("vdst", dst_grid.partition, pyoasis.OASIS.IN)
    oasis_component.enddef()

    print(
        f"Source: {src_name} "
        f"[type {type(src_grid.base).__name__}, "
        f"size {src_grid.base.size} {src_grid.base.shape}]"
    )
    print(
        f"Target: {dst_name} "
        f"[type {type(dst_grid.base).__name__}, "
        f"size {dst_grid.base.size} {dst_grid.base.shape}]"
    )

    test_func = test_func_ones

    f_src = test_func(src_grid.base.center_latitudes, src_grid.base.center_longitudes)
    f_dst = test_func(dst_grid.base.center_latitudes, dst_grid.base.center_longitudes)

    f_rcv = pyoasis.asarray(np.zeros(dst_grid.base.shape))
    src_var.put(0, f_src)
    dst_var.get(0, f_rcv)

    f_err = np.ma.array(
        f_rcv - f_dst,
        mask=dst_grid.base.mask == 1,
    )

    if np.isclose(f_err, 0.0).all():
        print("Remapping error is globally close to zero")
    else:
        print("Remapping error is NOT close to zero (at least not everywhere)")
    print(f"Error min:  {np.min(f_err):10.2e}")
    print(f"Error mean: {f_err.mean():10.2e}")
    print(f"Error max:  {np.max(f_err):10.2e}")

    del oasis_component


if __name__ == "__main__":
    main(sys.argv[1])
