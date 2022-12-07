# Ready2couple (`rdy2cpl`)

A Python tool to automatically and efficiently create auxiliary files and
remapping weights for the OASIS coupler.


## Installation

### Prerequisites

* C and Fortran compilers
* MPI installation, libraries and headers
* NetCDF libraries, headers and Fortran modules
* Python>=3.7
* OASIS3-MCT>=5.0 (build with shared libraries and pyOASIS support, see below)
* Python modules as required in `condaenv*.yml` files (will be installed with conda)


### Install OASIS3-MCT

Head over to the [OASIS home page](https://oasis.cerfacs.fr/en/) and find out
how to download and install OASIS3-MCT 5.0 or later. Make note of the build
directory in the installation process, it is needed below. Make also sure to
build with pyOASIS support by running both
```
> make -f TopMakefileOasis3
> make -f TopMakefileOasis3 pyoasis
```


### Prepare a conda environment

Create and activate a conda environment with dependencies (installed via the
conda-forge channel):
```
> conda env create --name=MY_ENV --file=condaenv.yml
> conda activate MY_ENV
```

Install `rdy2cpl` in this environment:
```
> pip install .
```
If you want to modify the `rdy2cpl` source code, install instead in editable
mode (`pip install -e .`).

For using the interpolation tests and allow them to plot results, install the
plotting dependencies:
```
> conda env update --name=MY_ENV --file=condaenv-plot.yml
```


### Environment variables

Make sure that `rdy2cpl` finds your OASIS installation by setting/modifying the following two environment variables:

* `OASIS_BUILD_PATH` must point to the OASIS **build** directory
* the `LD_LIBRARY_PATH` variable must include `$OASIS_BUILD_DIRECTORY/lib`

Note that the OASIS installation process for pyOASIS suggests setting further
environment variables. These variables are not needed for `rdy2cpl`.


## Running the `r2c` tool

The main Ready2couple command line tool is `r2c`, which should be in the `PATH`
once the installation is completed as described above:
```
> r2c --help
usage: r2c [-h] [-l | -n | -r] namcouple_spec

Ready2couple: Automatic OASIS3-MCT coupling set up

The r2c command creates the OASIS namcouple file, grid description
files (grids.nc, masks.nc, areas.nc), and remapping weight files
(rmp_*.nc) for a given coupling specification, given as a YAML file.

positional arguments:
  namcouple_spec        YAML file with namcouple specification

options:
  -h, --help            show this help message and exit
  -l, --num-links       print number of *distinc* coupling links
  -n, --namcouple       only create namcouple file
  -r, --reduced-namcouple
                        only create the reduced namcouple file (distinct links only)

If none of the options if given, everything is created: namcouple,
grid description files, and remapping weights.

IMPORTANT: r2c needs a working OASIS3-MCT installation, including
the pyOASIS API. Two environment variables must to be set:

  OASIS_BUILD_PATH: points to the OASIS *build* directory
  LD_LIBRARY_PATH: needs to include ${OASIS_BUILD_PATH}/lib
```

For convenience, a `Makefile` is provided that will take care of copying
necessary files to a `work` subdirectory and starting `r2c` with the appropriate
number of processes via `mpirun`. The example run can be started with `make
run`. However, keep in mind that coupling configuration is quite specific to the
use case and that some adjustments might be needed. Do not expect the `Makefile`
to work robustly without changes in all user environments.

Examples for namcouple specification files are provided in the `examples/`
subdirectory. Please refer to these examples for the YAML form of the coupling
information that is needed for `r2c`.


## Possible issues

### MPI for Python (`mpi4py`)

It is important that the `mpi4py` Python module interacts correctly with your
system MPI! The `mpi4py` module is therefore installed from a PyPI **source**
package and automatically build during the installation process (this is
controlled via the `condaenv.yml` file). This is why it is a prerequisite to
have working compilers and MPI installation, including headers and libraries.
See the [`mpi4py` installation
documentation](https://mpi4py.readthedocs.io/en/stable/install.html) in case of
problems.


### ecCodes (`eccodes`)

The [ecCodes](https://confluence.ecmwf.int/display/ECC) library is needed to
read some model-specific data from GRIB files. In order to make ecCodes available in Python, two components have to be installed:
* the binary ecCodes package, including libraries, definitions, and tables
* the Python API

There are, confusingly, two[^1] `eccodes` packages available, which provide the
corresponding components:
* `eccodes` on [conda-forge](https://anaconda.org/conda-forge/eccodes) for the
  binary package
* `eccodes` on [PyPI](https://pypi.org/project/eccodes) for the Python API

The `condaenv.yml` file will install both parts.

However, it is important to make sure that the installation does not interfere
with any system-wide installation of ecCodes.

[^1]: There are, in fact, further ecCodes related packages. Conda-forge has also
the [`python-eccodes`](https://anaconda.org/conda-forge/python-eccodes) package,
which presumably provides the Python API. However, at the time of writing this
package is at an older version than `eccodes` from PyPI, which is why we rely on
the latter.
