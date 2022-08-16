import numpy as np

from .utils import EARTH_RADIUS, equidistant, interval_bounds


def _is_monotonic(array):
    """Checks for *strict* monotonicity"""
    diffs = np.diff(array)
    return all(diffs < 0) or all(diffs > 0)


class RegularLatLonGrid:
    def __init__(self, lats, lons, *, first_lat=-90):
        if not _is_monotonic((first_lat, *lats, -first_lat)):
            raise ValueError("Non-monotonic latitude values")
        if not _is_monotonic(lons):
            raise ValueError("Non-monotonic longitude values")
        self.first_lat = first_lat
        self.lats = np.array(lats)
        self.lons = np.array(lons)
        self.mask = np.zeros(self.shape)

    @property
    def nlats(self):
        return len(self.lats)

    @property
    def nlons(self):
        return len(self.lons)

    @property
    def shape(self):
        return (self.nlats, self.nlons)

    @property
    def size(self):
        return self.nlats * self.nlons

    @property
    def center_latitudes(self):
        return np.tile(self.lats, (self.nlons, 1)).T

    @property
    def center_longitudes(self):
        return np.tile(self.lons, (self.nlats, 1))

    @property
    def corner_latitudes(self):
        n_lats = interval_bounds(self.first_lat, self.lats, -self.first_lat, loc="u")
        s_lats = interval_bounds(self.first_lat, self.lats, -self.first_lat, loc="l")
        return np.transpose(
            [
                np.tile(n_lats, (self.nlons, 1)),  #  1 ---- 0
                np.tile(n_lats, (self.nlons, 1)),  #  |      |
                np.tile(s_lats, (self.nlons, 1)),  #  |      |
                np.tile(s_lats, (self.nlons, 1)),  #  2 ---- 3
            ]
        )

    @property
    def corner_longitudes(self):
        e_lons = interval_bounds(0, self.lons, 360, loc="r", wrap=True)
        w_lons = interval_bounds(0, self.lons, 360, loc="l")
        return np.transpose(
            [
                np.tile(e_lons, (self.nlats, 1)).T,  #  1 ---- 0
                np.tile(w_lons, (self.nlats, 1)).T,  #  |      |
                np.tile(w_lons, (self.nlats, 1)).T,  #  |      |
                np.tile(e_lons, (self.nlats, 1)).T,  #  2 ---- 3
            ]
        )

    @property
    def areas(self):
        n_lats = interval_bounds(self.first_lat, self.lats, -self.first_lat, loc="u")
        s_lats = interval_bounds(self.first_lat, self.lats, -self.first_lat, loc="l")
        return np.tile(
            2
            * np.pi
            * EARTH_RADIUS ** 2
            * np.abs(np.sin(np.radians(n_lats)) - np.sin(np.radians(s_lats)))
            / self.nlons,
            (self.nlons, 1),
        ).T


class EquidistantLatLonGrid(RegularLatLonGrid):
    def __init__(self, nlats, nlons, *, first_lat=-90):
        super().__init__(
            equidistant(first_lat, -first_lat, nlats),
            equidistant(0, 360, nlons, center_at_start=True),
            first_lat=first_lat,
        )
