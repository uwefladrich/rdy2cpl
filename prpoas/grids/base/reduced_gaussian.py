import numpy as np

from .utils import EARTH_RADIUS, equidistant, interval_bounds


def _equidistant_longitudes(n, loc="c"):
    lons = equidistant(0, 360, n, center_at_start=True)
    if loc in ("c", "center"):
        return lons
    elif loc in ("w", "west"):
        return interval_bounds(0, lons, 360, loc="l", wrap=True)
    elif loc in ("e", "east"):
        return interval_bounds(0, lons, 360, loc="r")
    raise ValueError(f'Invalid value for loc argument: "{loc}"')


def _latitude_bounds(lats, loc):
    if loc in ("n", "north"):
        return interval_bounds(90, lats, -90, loc="l")
    elif loc in ("s", "south"):
        return interval_bounds(90, lats, -90, loc="r")
    raise ValueError(f'Invalid value for loc argument: "{loc}"')


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
