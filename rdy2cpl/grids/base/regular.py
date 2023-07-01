import numpy as np

from .utils import EARTH_RADIUS, equidistant, interval_bounds


def _is_monotonic(array):
    """Checks for *strict* monotonicity"""
    diffs = np.diff(array)
    return all(diffs < 0) or all(diffs > 0)


class RegularLatLonGrid:
    def __init__(self, lats, lons, start_lat=-90, transposed=False) -> None:
        if not _is_monotonic((start_lat, *lats, -start_lat)):
            raise ValueError("Non-monotonic latitude values")
        if not _is_monotonic(lons):
            raise ValueError("Non-monotonic longitude values")
        self.lats = np.array(lats)
        self.lons = np.array(lons)
        self.start_lat = start_lat
        self.transposed = transposed
        self.t = np.transpose if transposed else lambda x: x
        self.mask = np.zeros(self.shape)

    @property
    def nlats(self):
        return len(self.lats)

    @property
    def nlons(self):
        return len(self.lons)

    @property
    def shape(self):
        return (
            (self.nlats, self.nlons)
            if not self.transposed
            else (self.nlons, self.nlats)
        )

    @property
    def size(self):
        return self.nlats * self.nlons

    @property
    def center_latitudes(self):
        return self.t(np.tile(self.lats, (self.nlons, 1)).T)

    @property
    def center_longitudes(self):
        return self.t(np.tile(self.lons, (self.nlats, 1)))

    @property
    def corner_latitudes(self):
        n_lats = interval_bounds(self.start_lat, self.lats, -self.start_lat, loc="u")
        s_lats = interval_bounds(self.start_lat, self.lats, -self.start_lat, loc="l")
        return np.transpose(
            [
                self.t(np.tile(n_lats, (self.nlons, 1)).T),  # 1 ---- 0
                self.t(np.tile(n_lats, (self.nlons, 1)).T),  # |      |
                self.t(np.tile(s_lats, (self.nlons, 1)).T),  # |      |
                self.t(np.tile(s_lats, (self.nlons, 1)).T),  # 2 ---- 3
            ],
            (1, 2, 0),
        )

    @property
    def corner_longitudes(self):
        e_lons = interval_bounds(0, self.lons, 360, loc="r", wrap=True)
        w_lons = interval_bounds(0, self.lons, 360, loc="l")
        return np.transpose(
            [
                self.t(np.tile(e_lons, (self.nlats, 1))),  # 1 ---- 0
                self.t(np.tile(w_lons, (self.nlats, 1))),  # |      |
                self.t(np.tile(w_lons, (self.nlats, 1))),  # |      |
                self.t(np.tile(e_lons, (self.nlats, 1))),  # 2 ---- 3
            ],
            (1, 2, 0),
        )

    @property
    def areas(self):
        n_lats = interval_bounds(self.start_lat, self.lats, -self.start_lat, loc="u")
        s_lats = interval_bounds(self.start_lat, self.lats, -self.start_lat, loc="l")
        return self.t(
            np.tile(
                2
                * np.pi
                * EARTH_RADIUS**2
                * np.abs(np.sin(np.radians(n_lats)) - np.sin(np.radians(s_lats)))
                / self.nlons,
                (self.nlons, 1),
            ).T
        )


class EquidistantLatLonGrid(RegularLatLonGrid):
    def __init__(self, nlats, nlons, *, start_lat=-90, transposed=False):
        super().__init__(
            equidistant(start_lat, -start_lat, nlats),
            equidistant(0, 360, nlons, center_at_start=True),
            start_lat=start_lat,
            transposed=transposed,
        )
