import numpy as np

import pyoasis


def eqdist_center_longitudes(nx, ny, dx, first_lon=0, offset=0):
    lons = np.array(
        [first_lon + (offset * nx + i + 0.5) * dx for i in range(nx)],
        dtype=np.float64,
    )
    return np.tile(lons, (ny, 1)).T


def eqdist_center_latitudes(nx, ny, dy):
    lats = np.array([-90.0 + (j + 0.5) * dy for j in range(ny)], dtype=np.float64)
    return np.tile(lats, (nx, 1))


def eqdist_corner_longitudes(lons, dx):
    clons = pyoasis.asarray(np.zeros((*lons.shape, 4), dtype=np.float64))
    clons[:, :, 0] = lons[:, :] - 0.5 * dx
    clons[:, :, 1] = lons[:, :] + 0.5 * dx
    clons[:, :, 2] = clons[:, :, 1]
    clons[:, :, 3] = clons[:, :, 0]
    return clons


def eqdist_corner_latitudes(lats, dy):
    clats = pyoasis.asarray(np.zeros((*lats.shape, 4), dtype=np.float64))
    clats[:, :, 0] = lats[:, :] - 0.5 * dy
    clats[:, :, 1] = clats[:, :, 0]
    clats[:, :, 2] = lats[:, :] + 0.5 * dy
    clats[:, :, 3] = clats[:, :, 2]
    return clats


def rect_cell_areas(clons, clats):
    pi_180 = np.pi / 180.0
    return (
        pi_180
        * np.abs(np.sin(clats[:, :, 2] * pi_180) - np.sin(clats[:, :, 0] * pi_180))
        * np.abs(clons[:, :, 1] - clons[:, :, 0])
    )


def grid_a_mask(nx, ny, rank):
    mask = np.zeros((nx, ny), dtype=np.int32)
    if rank == 0:
        mask[4:6, 2:16] = 1
        mask[6:11, (8, 9, 14, 15)] = 1
        mask[11, (8, 9, 10, 13, 14, 15)] = 1
        mask[12, 9:15] = 1
        mask[13, 10:14] = 1
    elif rank == 1:
        mask[(3, 14), 14:16] = 1
        mask[(4, 13), 12:16] = 1
        mask[(5, 12), 11:15] = 1
        mask[(6, 11), 10:13] = 1
        mask[(7, 10), 9:12] = 1
        mask[8:10, 2:11] = 1
    elif rank == 2:
        mask[(4, 13), 4:14] = 1
        mask[(5, 12), 3:15] = 1
        mask[(6, 11), 2:5] = 1
        mask[(6, 11), 13:16] = 1
        mask[7:11, 2:4] = 1
        mask[7:11, 14:16] = 1
    return mask


def grid_b_mask(lons, lats):
    return np.where(
        np.power(lons[:, :] - 180.0, 2) + np.power(lats[:, :], 2) < 30 * 30, 1, 0
    )


class Grid:
    def __init__(self, nx, ny):
        self.nx = nx
        self.ny = ny
        self.dx = 360.0 / self.nx
        self.dy = 180.0 / self.ny
        self.partition = pyoasis.SerialPartition(nx * ny)

        self.mask = np.zeros((self.nx, self.ny), dtype=np.int32)
        self.fractions = np.ones((self.nx, self.ny), dtype=np.float64)
        self.angles = np.zeros((self.nx, self.ny), dtype=np.float64)

    @property
    def shape(self):
        return (self.nx, self.ny)

    @property
    def size(self):
        return self.nx * self.ny

    @property
    def center_longitudes(self):
        return eqdist_center_longitudes(self.nx, self.ny, self.dx)

    @property
    def center_latitudes(self):
        return eqdist_center_latitudes(self.nx, self.ny, self.dy)

    @property
    def corner_longitudes(self):
        return eqdist_corner_longitudes(self.center_longitudes, self.dx)

    @property
    def corner_latitudes(self):
        return eqdist_corner_latitudes(self.center_latitudes, self.dy)

    @property
    def areas(self):
        return rect_cell_areas(self.corner_longitudes, self.corner_latitudes)

    def oasis_grid(self, name):
        g = pyoasis.Grid(
            name,
            self.nx,
            self.ny,
            self.center_longitudes,
            self.center_latitudes,
            partition=self.partition,
        )
        g.set_corners(self.corner_longitudes, self.corner_latitudes)
        g.set_area(self.areas)
        g.set_mask(self.mask)
        if self.fractions is not None:
            g.set_frac(self.fractions)
        if self.angles is not None:
            g.set_angle(self.angles)
        return g


class GridA(Grid):
    @property
    def center_longitudes(self):
        return eqdist_center_longitudes(self.nx, self.ny, self.dx, first_lon=-180)


class GridB(Grid):
    pass
