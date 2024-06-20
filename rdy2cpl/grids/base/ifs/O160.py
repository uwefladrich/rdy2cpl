from rdy2cpl.grids.base.reduced_gaussian import ReducedGaussianGrid


class O160(ReducedGaussianGrid):
    def __init__(self):
        super().__init__(_lats, _nlons)


_lats = (
    89.5700895506067, 89.0131761310221, 88.4529738367131, 87.8920284453444, 87.3308011797376,
    86.7694375145276, 86.2079976214231, 85.6465108479529, 85.0849932009119, 84.5234541489144,
    83.9618996497181, 83.400333638737, 82.8387588197095, 82.2771771114338, 81.7155899132665,
    81.153998269713, 80.5924029761778, 80.0308046490315, 79.4692037732917, 78.907600735838,
    78.3459958490356, 77.7843893678487, 77.2227815024452, 76.6611724276205, 76.0995622899381,
    75.5379512132081, 74.9763393027375, 74.414726648662, 73.8531133285838, 73.2914994096763,
    72.7298849503795, 72.1682700017748, 71.6066546087076, 71.0450388107114, 70.4834226427713,
    69.9218061359605, 69.3601893179717, 68.7985722135654, 68.2369548449477, 67.6753372320917,
    67.1137193930114, 66.5521013439962, 65.9904830998128, 65.4288646738789, 64.8672460784143,
    64.3056273245713, 63.7440084225492, 63.1823893816941, 62.6207702105862, 62.0591509171168,
    61.4975315085565, 60.9359119916146, 60.374292372493, 59.8126726569328, 59.2510528502566,
    58.6894329574061, 58.1278129829758, 57.5661929312427, 57.0045728061936, 56.4429526115493,
    55.8813323507866, 55.3197120271579, 54.7580916437093, 54.1964712032966, 53.6348507086,
    53.0732301621377, 52.511609566278, 51.9499889232499, 51.388368235154, 50.826747503971,
    50.2651267315709, 49.7035059197201, 49.1418850700887, 48.5802641842574, 48.0186432637231,
    47.4570223099043, 46.895401324147, 46.3337803077286, 45.7721592618623, 45.2105381877018,
    44.6489170863444, 44.0872959588346, 43.5256748061674, 42.9640536292912, 42.4024324291106,
    41.840811206489, 41.2791899622509, 40.7175686971842, 40.1559474120422, 39.5943261075458,
    39.0327047843849, 38.4710834432206, 37.909462084686, 37.3478407093888, 36.7862193179118,
    36.2245979108143, 35.6629764886339, 35.1013550518869, 34.5397336010701, 33.9781121366611,
    33.41649065912, 32.8548691688896, 32.2932476663968, 31.731626152053, 31.1700046262551,
    30.6083830893862, 30.0467615418161, 29.4851399839021, 28.9235184159897, 28.3618968384128,
    27.8002752514945, 27.2386536555477, 26.6770320508755, 26.1154104377713, 25.55378881652,
    24.9921671873977, 24.4305455506724, 23.8689239066043, 23.3073022554465, 22.7456805974447,
    22.1840589328381, 21.6224372618593, 21.060815584735, 20.4991939016858, 19.9375722129269,
    19.3759505186683, 18.8143288191146, 18.2527071144659, 17.6910854049176, 17.1294636906605,
    16.5678419718816, 16.0062202487637, 15.4445985214858, 14.8829767902235, 14.3213550551488,
    13.7597333164304, 13.1981115742342, 12.636489828723, 12.0748680800568, 11.5132463283931,
    10.9516245738869, 10.390002816691, 9.82838105695562, 9.26675929482939, 8.70513753045879,
    8.14351576398857, 7.58189399556176, 7.02027222531986, 6.45865045340297, 5.89702867994982,
    5.33540690509797, 4.77378512898388, 4.21216335174302, 3.65054157351001, 3.08891979441866,
    2.52729801460214, 1.96567623419308, 1.40405445332362, 0.842432672125553, 0.280810890730402,
    -0.280810890730402, -0.842432672125553, -1.40405445332362, -1.96567623419308, -2.52729801460214,
    -3.08891979441866, -3.65054157351001, -4.21216335174302, -4.77378512898388, -5.33540690509797,
    -5.89702867994982, -6.45865045340297, -7.02027222531986, -7.58189399556176, -8.14351576398857,
    -8.70513753045879, -9.26675929482939, -9.82838105695562, -10.390002816691, -10.9516245738869,
    -11.5132463283931, -12.0748680800568, -12.636489828723, -13.1981115742342, -13.7597333164304,
    -14.3213550551488, -14.8829767902235, -15.4445985214858, -16.0062202487637, -16.5678419718816,
    -17.1294636906605, -17.6910854049176, -18.2527071144659, -18.8143288191146, -19.3759505186683,
    -19.9375722129269, -20.4991939016858, -21.060815584735, -21.6224372618593, -22.1840589328381,
    -22.7456805974447, -23.3073022554465, -23.8689239066043, -24.4305455506724, -24.9921671873977,
    -25.55378881652, -26.1154104377713, -26.6770320508755, -27.2386536555477, -27.8002752514945,
    -28.3618968384128, -28.9235184159897, -29.4851399839021, -30.0467615418161, -30.6083830893862,
    -31.1700046262551, -31.731626152053, -32.2932476663968, -32.8548691688896, -33.41649065912,
    -33.9781121366611, -34.5397336010701, -35.1013550518869, -35.6629764886339, -36.2245979108143,
    -36.7862193179118, -37.3478407093888, -37.909462084686, -38.4710834432206, -39.0327047843849,
    -39.5943261075458, -40.1559474120422, -40.7175686971842, -41.2791899622509, -41.840811206489,
    -42.4024324291106, -42.9640536292912, -43.5256748061674, -44.0872959588346, -44.6489170863444,
    -45.2105381877018, -45.7721592618623, -46.3337803077286, -46.895401324147, -47.4570223099043,
    -48.0186432637231, -48.5802641842574, -49.1418850700887, -49.7035059197201, -50.2651267315709,
    -50.826747503971, -51.388368235154, -51.9499889232499, -52.511609566278, -53.0732301621377,
    -53.6348507086, -54.1964712032966, -54.7580916437093, -55.3197120271579, -55.8813323507866,
    -56.4429526115493, -57.0045728061936, -57.5661929312427, -58.1278129829758, -58.6894329574061,
    -59.2510528502566, -59.8126726569328, -60.374292372493, -60.9359119916146, -61.4975315085565,
    -62.0591509171168, -62.6207702105862, -63.1823893816941, -63.7440084225492, -64.3056273245713,
    -64.8672460784143, -65.4288646738789, -65.9904830998128, -66.5521013439962, -67.1137193930114,
    -67.6753372320917, -68.2369548449477, -68.7985722135654, -69.3601893179717, -69.9218061359605,
    -70.4834226427713, -71.0450388107114, -71.6066546087076, -72.1682700017748, -72.7298849503795,
    -73.2914994096763, -73.8531133285838, -74.414726648662, -74.9763393027375, -75.5379512132081,
    -76.0995622899381, -76.6611724276205, -77.2227815024452, -77.7843893678487, -78.3459958490356,
    -78.907600735838, -79.4692037732917, -80.0308046490315, -80.5924029761778, -81.153998269713,
    -81.7155899132665, -82.2771771114338, -82.8387588197095, -83.400333638737, -83.9618996497181,
    -84.5234541489144, -85.0849932009119, -85.6465108479529, -86.2079976214231, -86.7694375145276,
    -87.3308011797376, -87.8920284453444, -88.4529738367131, -89.0131761310221, -89.5700895506067,
)

_nlons = (
    20, 24, 28, 32, 36, 40, 44, 48, 52, 56,
    60, 64, 68, 72, 76, 80, 84, 88, 92, 96,
    100, 104, 108, 112, 116, 120, 124, 128, 132, 136,
    140, 144, 148, 152, 156, 160, 164, 168, 172, 176,
    180, 184, 188, 192, 196, 200, 204, 208, 212, 216,
    220, 224, 228, 232, 236, 240, 244, 248, 252, 256,
    260, 264, 268, 272, 276, 280, 284, 288, 292, 296,
    300, 304, 308, 312, 316, 320, 324, 328, 332, 336,
    340, 344, 348, 352, 356, 360, 364, 368, 372, 376,
    380, 384, 388, 392, 396, 400, 404, 408, 412, 416,
    420, 424, 428, 432, 436, 440, 444, 448, 452, 456,
    460, 464, 468, 472, 476, 480, 484, 488, 492, 496,
    500, 504, 508, 512, 516, 520, 524, 528, 532, 536,
    540, 544, 548, 552, 556, 560, 564, 568, 572, 576,
    580, 584, 588, 592, 596, 600, 604, 608, 612, 616,
    620, 624, 628, 632, 636, 640, 644, 648, 652, 656,
    656, 652, 648, 644, 640, 636, 632, 628, 624, 620,
    616, 612, 608, 604, 600, 596, 592, 588, 584, 580,
    576, 572, 568, 564, 560, 556, 552, 548, 544, 540,
    536, 532, 528, 524, 520, 516, 512, 508, 504, 500,
    496, 492, 488, 484, 480, 476, 472, 468, 464, 460,
    456, 452, 448, 444, 440, 436, 432, 428, 424, 420,
    416, 412, 408, 404, 400, 396, 392, 388, 384, 380,
    376, 372, 368, 364, 360, 356, 352, 348, 344, 340,
    336, 332, 328, 324, 320, 316, 312, 308, 304, 300,
    296, 292, 288, 284, 280, 276, 272, 268, 264, 260,
    256, 252, 248, 244, 240, 236, 232, 228, 224, 220,
    216, 212, 208, 204, 200, 196, 192, 188, 184, 180,
    176, 172, 168, 164, 160, 156, 152, 148, 144, 140,
    136, 132, 128, 124, 120, 116, 112, 108, 104, 100,
    96, 92, 88, 84, 80, 76, 72, 68, 64, 60,
    56, 52, 48, 44, 40, 36, 32, 28, 24, 20,
)