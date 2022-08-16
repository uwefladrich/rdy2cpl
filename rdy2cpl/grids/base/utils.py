import numpy as np

EARTH_RADIUS = 6371e3  # m


def equidistant(start, end, N, *, center_at_start=False):
    """Divides the interval [start, end]  into N subintervals of equal size and
    returns the midpoints of the subintervals. If 'first_at_start' is true, the
    first interval is centered around the start point."""
    if center_at_start:
        return np.linspace(start, end, N + 1)[:-1]
    else:
        return np.linspace(start, end, 2 * N + 1)[1::2]


def interval_bounds(start, centers, end, *, loc, wrap=False):
    """Returns the upper or lower bounds of [start, end] subintervals defined by
    their centers. It is checked if the first center coincides with 'start' and
    it is in that case assumed that the first interval is centered around the
    starting point. If 'wrap' is True, the first lower bound (last upper) is
    returned the same as the last upper (first lower)."""
    center_midpoints = 0.5 * (centers[:-1] + centers[1:])
    last_dx = 0.5 * (end - centers[-1]) if np.isclose(start, centers[0]) else 0
    if loc in ("l", "left", "lower"):
        return np.array((end - last_dx if wrap else start - last_dx, *center_midpoints))
    elif loc in ("r", "right", "u", "upper"):
        return np.array((*center_midpoints, start - last_dx if wrap else end - last_dx))
    raise ValueError(f"Invalid value for 'loc' argument: {loc}")
