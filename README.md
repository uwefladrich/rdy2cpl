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
