import numpy as np

from .utils import EARTH_RADIUS


def _equidistant_longitudes(n, loc="c"):
    if loc in ("c", "center"):
        return np.linspace(0, 360, n + 1)[:-1]
    bounds = np.linspace(0, 360, 2 * n + 1)[1::2]
    if loc in ("e", "east"):
        return bounds
    if loc in ("w", "west"):
        return np.roll(bounds, 1)


def _latitude_bounds(lats, loc):
    centers = 0.5 * (lats[:-1] + lats[1:])
    if loc in ("s", "south"):
        return np.array((*centers, -90))
    elif loc in ("n", "north"):
        return np.array((90, *centers))


class ReducedGaussianGrid:
    def __init__(self, nlons, lats):
        self.nlons = nlons
        self.lats = np.array(lats)
        self.mask = np.zeros(self.shape)

    def _repeat(self, values):
        return np.block([np.repeat(v, n) for v, n in zip(values, self.nlons)])

    def _tile(self, func, *args, **kwargs):
        return np.block([func(n, *args, **kwargs) for n in self.nlons])

    @property
    def shape(self):
        return (sum(self.nlons), 1)

    @property
    def size(self):
        return sum(self.nlons)

    @property
    def cell_longitudes(self):
        return self._tile(_equidistant_longitudes).reshape((-1, 1))

    @property
    def cell_latitudes(self):
        return self._repeat(self.lats).reshape((-1, 1))

    @property
    def corner_longitudes(self):
        return np.transpose(
            [
                [self._tile(_equidistant_longitudes, loc="e")],
                [self._tile(_equidistant_longitudes, loc="w")],
                [self._tile(_equidistant_longitudes, loc="w")],
                [self._tile(_equidistant_longitudes, loc="e")],
            ]
        )

    @property
    def corner_latitudes(self):
        return np.transpose(
            [
                [self._repeat(_latitude_bounds(self.lats, loc="n"))],
                [self._repeat(_latitude_bounds(self.lats, loc="n"))],
                [self._repeat(_latitude_bounds(self.lats, loc="s"))],
                [self._repeat(_latitude_bounds(self.lats, loc="s"))],
            ]
        )

    @property
    def areas(self):
        areas = (
            2
            * np.pi
            * EARTH_RADIUS ** 2
            * np.abs(
                np.sin(np.radians(_latitude_bounds(self.lats, loc="n")))
                - np.sin(np.radians(_latitude_bounds(self.lats, loc="s")))
            )
            / self.nlons
        )
        return self._repeat(areas).reshape((-1, 1))
