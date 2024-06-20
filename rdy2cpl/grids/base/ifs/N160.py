from rdy2cpl.grids.base.reduced_gaussian import ReducedGaussianGrid


class N160(ReducedGaussianGrid):
    def __init__(self):
        super().__init__(_lats, _nlons)


_lats = (
    89.5700895506083, 89.0131761310228, 88.4529738367133, 87.8920284453448, 87.3308011797378,
    86.7694375145277, 86.2079976214232, 85.6465108479529, 85.0849932009118, 84.5234541489143,
    83.961899649718, 83.4003336387369, 82.8387588197095, 82.2771771114338, 81.7155899132664,
    81.153998269713, 80.5924029761778, 80.0308046490315, 79.4692037732917, 78.907600735838,
    78.3459958490356, 77.7843893678487, 77.2227815024452, 76.6611724276205, 76.0995622899381,
    75.5379512132081, 74.9763393027375, 74.4147266486621, 73.8531133285838, 73.2914994096763,
    72.7298849503796, 72.1682700017748, 71.6066546087076, 71.0450388107113, 70.4834226427713,
    69.9218061359605, 69.3601893179717, 68.7985722135654, 68.2369548449477, 67.6753372320917,
    67.1137193930113, 66.5521013439961, 65.9904830998127, 65.4288646738789, 64.8672460784143,
    64.3056273245713, 63.7440084225492, 63.1823893816941, 62.6207702105861, 62.0591509171168,
    61.4975315085564, 60.9359119916146, 60.374292372493, 59.8126726569328, 59.2510528502566,
    58.6894329574061, 58.1278129829758, 57.5661929312427, 57.0045728061936, 56.4429526115493,
    55.8813323507866, 55.3197120271579, 54.7580916437093, 54.1964712032966, 53.6348507086,
    53.0732301621378, 52.511609566278, 51.9499889232499, 51.388368235154, 50.826747503971,
    50.265126731571, 49.7035059197201, 49.1418850700887, 48.5802641842574, 48.0186432637231,
    47.4570223099044, 46.8954013241471, 46.3337803077286, 45.7721592618623, 45.2105381877019,
    44.6489170863444, 44.0872959588346, 43.5256748061674, 42.9640536292912, 42.4024324291106,
    41.840811206489, 41.2791899622509, 40.7175686971842, 40.1559474120422, 39.5943261075458,
    39.0327047843849, 38.4710834432206, 37.909462084686, 37.3478407093888, 36.7862193179118,
    36.2245979108143, 35.6629764886339, 35.1013550518869, 34.5397336010701, 33.9781121366611,
    33.41649065912, 32.8548691688896, 32.2932476663968, 31.731626152053, 31.1700046262551,
    30.6083830893862, 30.0467615418161, 29.4851399839021, 28.9235184159897, 28.3618968384128,
    27.8002752514945, 27.2386536555477, 26.6770320508755, 26.1154104377713, 25.55378881652,
    24.9921671873977, 24.4305455506724, 23.8689239066043, 23.3073022554465, 22.7456805974447,
    22.1840589328381, 21.6224372618593, 21.060815584735, 20.4991939016858, 19.9375722129269,
    19.3759505186683, 18.8143288191146, 18.2527071144659, 17.6910854049175, 17.1294636906605,
    16.5678419718816, 16.0062202487637, 15.4445985214858, 14.8829767902235, 14.3213550551488,
    13.7597333164304, 13.1981115742342, 12.636489828723, 12.0748680800568, 11.5132463283931,
    10.9516245738869, 10.3900028166909, 9.82838105695562, 9.26675929482939, 8.70513753045879,
    8.14351576398857, 7.58189399556176, 7.02027222531986, 6.45865045340297, 5.89702867994982,
    5.33540690509797, 4.77378512898388, 4.21216335174302, 3.65054157351001, 3.08891979441866,
    2.52729801460214, 1.96567623419308, 1.40405445332362, 0.842432672125553, 0.280810890730402,
    -0.280810890730402, -0.842432672125553, -1.40405445332362, -1.96567623419308, -2.52729801460214,
    -3.08891979441866, -3.65054157351001, -4.21216335174302, -4.77378512898388, -5.33540690509797,
    -5.89702867994982, -6.45865045340297, -7.02027222531986, -7.58189399556176, -8.14351576398857,
    -8.70513753045879, -9.26675929482939, -9.82838105695562, -10.3900028166909, -10.9516245738869,
    -11.5132463283931, -12.0748680800568, -12.636489828723, -13.1981115742342, -13.7597333164304,
    -14.3213550551488, -14.8829767902235, -15.4445985214858, -16.0062202487637, -16.5678419718816,
    -17.1294636906605, -17.6910854049175, -18.2527071144659, -18.8143288191146, -19.3759505186683,
    -19.9375722129269, -20.4991939016858, -21.060815584735, -21.6224372618593, -22.1840589328381,
    -22.7456805974447, -23.3073022554465, -23.8689239066043, -24.4305455506724, -24.9921671873977,
    -25.55378881652, -26.1154104377713, -26.6770320508755, -27.2386536555477, -27.8002752514945,
    -28.3618968384128, -28.9235184159897, -29.4851399839021, -30.0467615418161, -30.6083830893862,
    -31.1700046262551, -31.731626152053, -32.2932476663968, -32.8548691688896, -33.41649065912,
    -33.9781121366611, -34.5397336010701, -35.1013550518869, -35.6629764886339, -36.2245979108143,
    -36.7862193179118, -37.3478407093888, -37.909462084686, -38.4710834432206, -39.0327047843849,
    -39.5943261075458, -40.1559474120422, -40.7175686971842, -41.2791899622509, -41.840811206489,
    -42.4024324291106, -42.9640536292912, -43.5256748061674, -44.0872959588346, -44.6489170863444,
    -45.2105381877019, -45.7721592618623, -46.3337803077286, -46.8954013241471, -47.4570223099044,
    -48.0186432637231, -48.5802641842574, -49.1418850700887, -49.7035059197201, -50.265126731571,
    -50.826747503971, -51.388368235154, -51.9499889232499, -52.511609566278, -53.0732301621378,
    -53.6348507086, -54.1964712032966, -54.7580916437093, -55.3197120271579, -55.8813323507866,
    -56.4429526115493, -57.0045728061936, -57.5661929312427, -58.1278129829758, -58.6894329574061,
    -59.2510528502566, -59.8126726569328, -60.374292372493, -60.9359119916146, -61.4975315085564,
    -62.0591509171168, -62.6207702105861, -63.1823893816941, -63.7440084225492, -64.3056273245713,
    -64.8672460784143, -65.4288646738789, -65.9904830998127, -66.5521013439961, -67.1137193930113,
    -67.6753372320917, -68.2369548449477, -68.7985722135654, -69.3601893179717, -69.9218061359605,
    -70.4834226427713, -71.0450388107113, -71.6066546087076, -72.1682700017748, -72.7298849503796,
    -73.2914994096763, -73.8531133285838, -74.4147266486621, -74.9763393027375, -75.5379512132081,
    -76.0995622899381, -76.6611724276205, -77.2227815024452, -77.7843893678487, -78.3459958490356,
    -78.907600735838, -79.4692037732917, -80.0308046490315, -80.5924029761778, -81.153998269713,
    -81.7155899132664, -82.2771771114338, -82.8387588197095, -83.4003336387369, -83.961899649718,
    -84.5234541489143, -85.0849932009118, -85.6465108479529, -86.2079976214232, -86.7694375145277,
    -87.3308011797378, -87.8920284453448, -88.4529738367133, -89.0131761310228, -89.5700895506083,
)

_nlons = (
    18, 25, 36, 40, 45, 50, 60, 64, 72, 72,
    80, 90, 90, 96, 108, 120, 120, 125, 128, 135,
    144, 150, 160, 160, 180, 180, 180, 192, 192, 200,
    216, 216, 225, 225, 240, 240, 243, 250, 256, 270,
    270, 288, 288, 288, 300, 300, 320, 320, 320, 320,
    324, 360, 360, 360, 360, 360, 360, 375, 375, 375,
    384, 384, 400, 400, 400, 405, 432, 432, 432, 432,
    432, 450, 450, 450, 450, 480, 480, 480, 480, 480,
    480, 480, 500, 500, 500, 500, 500, 512, 512, 540,
    540, 540, 540, 540, 540, 540, 540, 576, 576, 576,
    576, 576, 576, 576, 576, 576, 576, 600, 600, 600,
    600, 600, 600, 600, 600, 600, 640, 640, 640, 640,
    640, 640, 640, 640, 640, 640, 640, 640, 640, 640,
    640, 640, 640, 640, 640, 640, 640, 640, 640, 640,
    640, 640, 640, 640, 640, 640, 640, 640, 640, 640,
    640, 640, 640, 640, 640, 640, 640, 640, 640, 640,
    640, 640, 640, 640, 640, 640, 640, 640, 640, 640,
    640, 640, 640, 640, 640, 640, 640, 640, 640, 640,
    640, 640, 640, 640, 640, 640, 640, 640, 640, 640,
    640, 640, 640, 640, 640, 640, 640, 640, 640, 640,
    640, 640, 640, 640, 600, 600, 600, 600, 600, 600,
    600, 600, 600, 576, 576, 576, 576, 576, 576, 576,
    576, 576, 576, 540, 540, 540, 540, 540, 540, 540,
    540, 512, 512, 500, 500, 500, 500, 500, 480, 480,
    480, 480, 480, 480, 480, 450, 450, 450, 450, 432,
    432, 432, 432, 432, 405, 400, 400, 400, 384, 384,
    375, 375, 375, 360, 360, 360, 360, 360, 360, 324,
    320, 320, 320, 320, 300, 300, 288, 288, 288, 270,
    270, 256, 250, 243, 240, 240, 225, 225, 216, 216,
    200, 192, 192, 180, 180, 180, 160, 160, 150, 144,
    135, 128, 125, 120, 120, 108, 96, 90, 90, 80,
    72, 72, 64, 60, 50, 45, 40, 36, 25, 18,
)