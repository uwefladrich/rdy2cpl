from rdy2cpl.loader import _import_pyoasis

pyoasis = _import_pyoasis()


class CoupleGrid:
    def __init__(self, base, name):
        self.base = base
        self.name = name
        self.partition = pyoasis.SerialPartition(self.base.size)

    def write(self):
        oas_grid = pyoasis.Grid(
            self.name,
            *self.base.shape,
            self.base.center_longitudes,
            self.base.center_latitudes,
        )
        oas_grid.set_corners(self.base.corner_longitudes, self.base.corner_latitudes)
        oas_grid.set_area(self.base.areas)
        oas_grid.set_mask(self.base.mask)
        if hasattr(self.base, "fractions"):
            oas_grid.set_frac(self.base.fractions)
        if hasattr(self.base, "angles"):
            oas_grid.set_angle(self.base.angles)
        oas_grid.write()
