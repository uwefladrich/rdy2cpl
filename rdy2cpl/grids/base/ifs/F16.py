from rdy2cpl.grids.base.regular import RegularLatLonGrid
from rdy2cpl.grids.base.utils import equidistant


class F16(RegularLatLonGrid):
    """Full (regular) Gaussian grid F16 (32 x 64), e.g. OpenIFS TL21"""

    def __init__(self, transposed=False):
        # Latitudes run north to south, as in ICMGG files
        super().__init__(
            _lats,
            equidistant(0, 360, 64, center_at_start=True),
            start_lat=90,
            transposed=transposed,
        )


_lats = (
    85.7605871204438, 80.26877907225, 74.7445403686358, 69.2129761693708, 63.6786355610969,
    58.1429540492033, 52.6065260343453, 47.0696420596877, 41.5324612466561, 35.9950784112716,
    30.4575539611521, 24.9199286299486, 19.3822313464344, 13.8444837343849, 8.3067028565188,
    2.768903007736, -2.768903007736, -8.3067028565188, -13.8444837343849, -19.3822313464344,
    -24.9199286299486, -30.4575539611521, -35.9950784112716, -41.5324612466561, -47.0696420596877,
    -52.6065260343453, -58.1429540492033, -63.6786355610969, -69.2129761693708, -74.7445403686358,
    -80.26877907225, -85.7605871204438,
)
