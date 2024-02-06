from rdy2cpl.grids.base.reduced_gaussian import ReducedGaussianGrid


class Tco399(ReducedGaussianGrid):
    def __init__(self):
        super().__init__(_lats, _nlons)


_lats = (
89.8278746458936, 89.6049004900231, 89.3806095512502, 89.1560210950552, 88.9313197834772, 
88.706563860905, 88.4817774185774, 88.2569722065048, 88.0321546334029, 87.8073284902638, 
87.5824961624204, 87.3576592255104, 87.1328187620395, 86.9079755402427, 86.6831301203839, 
86.4582829206533, 86.2334342595074, 86.0085843837221, 85.7837334874826, 85.5588817256825, 
85.3340292233812, 85.1091760826566, 84.884322387651, 84.6594682083445, 84.4346136034139, 
84.2097586224261, 83.9849033075396, 83.760047694839, 83.5351918153906, 83.3103356960851, 
83.0854793603169, 82.8606228285338, 82.6357661186873, 82.4109092466016, 82.1860522262803, 
81.9611950701603, 81.7363377893254, 81.5114803936852, 81.2866228921265, 81.0617652926422, 
80.8369076024407, 80.6120498280398, 80.3871919753479, 80.1623340497331, 79.9374760560837, 
79.7126179988608, 79.4877598821437, 79.2629017096704, 79.0380434848719, 78.8131852109035, 
78.5883268906718, 78.3634685268588, 78.1386101219434, 77.9137516782196, 77.6888931978141, 
77.464034682701, 77.2391761347153, 77.0143175555649, 76.7894589468414, 76.5646003100298, 
76.3397416465176, 76.1148829576022, 75.8900242444982, 75.6651655083445, 75.4403067502091, 
75.2154479710953, 74.9905891719463, 74.7657303536496, 74.5408715170409, 74.3160126629084, 
74.0911537919953, 73.8662949050035, 73.6414360025965, 73.4165770854017, 73.1917181540129, 
72.9668592089926, 72.7420002508738, 72.5171412801625, 72.2922822973387, 72.0674233028583, 
71.8425642971547, 71.6177052806403, 71.3928462537072, 71.1679872167291, 70.9431281700618, 
70.7182691140447, 70.4934100490016, 70.2685509752413, 70.0436918930588, 69.8188328027362, 
69.5939737045428, 69.3691145987363, 69.1442554855634, 68.9193963652602, 68.6945372380528, 
68.4696781041579, 68.2448189637832, 68.019959817128, 67.7951006643835, 67.5702415057331, 
67.3453823413531, 67.1205231714128, 66.8956639960749, 66.6708048154959, 66.4459456298263, 
66.2210864392109, 65.996227243789, 65.7713680436948, 65.5465088390577, 65.3216496300021, 
65.0967904166482, 64.8719311991118, 64.6470719775044, 64.422212751934, 64.1973535225043, 
63.972494289316, 63.7476350524659, 63.5227758120477, 63.297916568152, 63.0730573208663, 
62.8481980702752, 62.6233388164605, 62.3984795595014, 62.1736202994746, 61.9487610364542, 
61.723901770512, 61.4990425017176, 61.2741832301384, 61.0493239558396, 60.8244646788845, 
60.5996053993346, 60.3747461172492, 60.149886832686, 59.9250275457011, 59.7001682563488, 
59.4753089646818, 59.2504496707513, 59.025590374607, 58.8007310762971, 58.5758717758686, 
58.351012473367, 58.1261531688367, 57.9012938623206, 57.6764345538606, 57.4515752434975, 
57.2267159312708, 57.001856617219, 56.7769973013796, 56.5521379837891, 56.327278664483, 
56.1024193434958, 55.8775600208612, 55.652700696612, 55.4278413707801, 55.2029820433965, 
54.9781227144917, 54.7532633840952, 54.5284040522357, 54.3035447189414, 54.0786853842395, 
53.8538260481569, 53.6289667107195, 53.4041073719528, 53.1792480318815, 52.9543886905298, 
52.7295293479214, 52.5046700040793, 52.279810659026, 52.0549513127834, 51.8300919653731, 
51.605232616816, 51.3803732671325, 51.1555139163426, 50.930654564466, 50.7057952115217, 
50.4809358575284, 50.2560765025044, 50.0312171464674, 49.806357789435, 49.5814984314242, 
49.3566390724517, 49.1317797125338, 48.9069203516865, 48.6820609899255, 48.457201627266, 
48.232342263723, 48.0074828993112, 47.7826235340449, 47.5577641679382, 47.3329048010047, 
47.1080454332581, 46.8831860647114, 46.6583266953776, 46.4334673252694, 46.2086079543992, 
45.983748582779, 45.7588892104209, 45.5340298373364, 45.3091704635371, 45.0843110890342, 
44.8594517138386, 44.6345923379612, 44.4097329614124, 44.1848735842028, 43.9600142063424, 
43.7351548278412, 43.510295448709, 43.2854360689555, 43.06057668859, 42.8357173076218, 
42.61085792606, 42.3859985439135, 42.161139161191, 41.9362797779011, 41.7114203940523, 
41.4865610096528, 41.2617016247108, 41.0368422392342, 40.8119828532309, 40.5871234667086, 
40.3622640796748, 40.137404692137, 39.9125453041025, 39.6876859155785, 39.4628265265721, 
39.2379671370901, 39.0131077471394, 38.7882483567267, 38.5633889658586, 38.3385295745415, 
38.1136701827818, 37.8888107905859, 37.6639513979598, 37.4390920049096, 37.2142326114413, 
36.9893732175608, 36.7645138232737, 36.5396544285858, 36.3147950335027, 36.0899356380299, 
35.8650762421728, 35.6402168459366, 35.4153574493267, 35.1904980523482, 34.9656386550062, 
34.7407792573057, 34.5159198592516, 34.2910604608488, 34.066201062102, 33.841341663016, 
33.6164822635954, 33.3916228638447, 33.1667634637684, 32.941904063371, 32.7170446626569, 
32.4921852616304, 32.2673258602956, 32.0424664586568, 31.8176070567181, 31.5927476544835, 
31.3678882519571, 31.1430288491428, 30.9181694460445, 30.693310042666, 30.4684506390112, 
30.2435912350837, 30.0187318308872, 29.7938724264254, 29.5690130217019, 29.3441536167201, 
29.1192942114836, 28.8944348059959, 28.6695754002602, 28.44471599428, 28.2198565880586, 
27.9949971815992, 27.770137774905, 27.5452783679793, 27.3204189608252, 27.0955595534457, 
26.870700145844, 26.6458407380231, 26.4209813299859, 26.1961219217355, 25.9712625132746, 
25.7464031046063, 25.5215436957333, 25.2966842866584, 25.0718248773845, 24.8469654679143, 
24.6221060582504, 24.3972466483957, 24.1723872383526, 23.9475278281239, 23.7226684177121, 
23.4978090071198, 23.2729495963495, 23.0480901854038, 22.823230774285, 22.5983713629957, 
22.3735119515383, 22.1486525399151, 21.9237931281286, 21.6989337161811, 21.4740743040749, 
21.2492148918122, 21.0243554793955, 20.7994960668269, 20.5746366541086, 20.3497772412429, 
20.1249178282319, 19.9000584150778, 19.6751990017828, 19.4503395883489, 19.2254801747782, 
19.0006207610729, 18.775761347235, 18.5509019332666, 18.3260425191695, 18.101183104946, 
17.8763236905978, 17.6514642761271, 17.4266048615357, 17.2017454468256, 16.9768860319987, 
16.7520266170569, 16.5271672020021, 16.3023077868361, 16.0774483715609, 15.8525889561781, 
15.6277295406897, 15.4028701250975, 15.1780107094032, 14.9531512936086, 14.7282918777155, 
14.5034324617257, 14.2785730456409, 14.0537136294627, 13.828854213193, 13.6039947968334, 
13.3791353803856, 13.1542759638513, 12.9294165472321, 12.7045571305297, 12.4796977137457, 
12.2548382968819, 12.0299788799397, 11.8051194629208, 11.5802600458268, 11.3554006286593, 
11.1305412114198, 10.90568179411, 10.6808223767315, 10.4559629592856, 10.2311035417741, 
10.0062441241984, 9.78138470656006, 9.55652528886062, 9.33166587110158, 9.1068064532844, 
8.88194703541063, 8.65708761748175, 8.43222819949924, 8.20736878146456, 7.9825093633792, 
7.75764994524461, 7.53279052706224, 7.30793110883355, 7.08307169055999, 6.85821227224297, 
6.63335285388396, 6.40849343548435, 6.18363401704559, 5.95877459856911, 5.7339151800563, 
5.50905576150856, 5.2841963429273, 5.05933692431394, 4.83447750566982, 4.60961808699641, 
4.38475866829507, 4.15989924956715, 3.93503983081408, 3.7101804120372, 3.48532099323791, 
3.26046157441757, 3.03560215557754, 2.81074273671922, 2.58588331784392, 2.36102389895308, 
2.13616448004801, 1.91130506113008, 1.68644564220064, 1.46158622326105, 1.23672680431268, 
1.01186738535687, 0.787007966395004, 0.562148547428371, 0.33728912845838, 
0.112429709486354, -0.112429709486354, -0.33728912845838, -0.562148547428371, 
-0.787007966395004, -1.01186738535687, -1.23672680431268, -1.46158622326105, 
-1.68644564220064, -1.91130506113008, -2.13616448004801, -2.36102389895308, 
-2.58588331784392, -2.81074273671922, -3.03560215557754, -3.26046157441757, 
-3.48532099323791, -3.7101804120372, -3.93503983081408, -4.15989924956715, 
-4.38475866829507, -4.60961808699641, -4.83447750566982, -5.05933692431394, 
-5.2841963429273, -5.50905576150856, -5.7339151800563, -5.95877459856911, 
-6.18363401704559, -6.40849343548435, -6.63335285388396, -6.85821227224297, 
-7.08307169055999, -7.30793110883355, -7.53279052706224, -7.75764994524461, 
-7.9825093633792, -8.20736878146456, -8.43222819949924, -8.65708761748175, 
-8.88194703541063, -9.1068064532844, -9.33166587110158, -9.55652528886062, 
-9.78138470656006, -10.0062441241984, -10.2311035417741, -10.4559629592856, 
-10.6808223767315, -10.90568179411, -11.1305412114198, -11.3554006286593, 
-11.5802600458268, -11.8051194629208, -12.0299788799397, -12.2548382968819, 
-12.4796977137457, -12.7045571305297, -12.9294165472321, -13.1542759638513, 
-13.3791353803856, -13.6039947968334, -13.828854213193, -14.0537136294627, 
-14.2785730456409, -14.5034324617257, -14.7282918777155, -14.9531512936086, 
-15.1780107094032, -15.4028701250975, -15.6277295406897, -15.8525889561781, 
-16.0774483715609, -16.3023077868361, -16.5271672020021, -16.7520266170569, 
-16.9768860319987, -17.2017454468256, -17.4266048615357, -17.6514642761271, 
-17.8763236905978, -18.101183104946, -18.3260425191695, -18.5509019332666, 
-18.775761347235, -19.0006207610729, -19.2254801747782, -19.4503395883489, 
-19.6751990017828, -19.9000584150778, -20.1249178282319, -20.3497772412429, 
-20.5746366541086, -20.7994960668269, -21.0243554793955, -21.2492148918122, 
-21.4740743040749, -21.6989337161811, -21.9237931281286, -22.1486525399151, 
-22.3735119515383, -22.5983713629957, -22.823230774285, -23.0480901854038, 
-23.2729495963495, -23.4978090071198, -23.7226684177121, -23.9475278281239, 
-24.1723872383526, -24.3972466483957, -24.6221060582504, -24.8469654679143, 
-25.0718248773845, -25.2966842866584, -25.5215436957333, -25.7464031046063, 
-25.9712625132746, -26.1961219217355, -26.4209813299859, -26.6458407380231, 
-26.870700145844, -27.0955595534457, -27.3204189608252, -27.5452783679793, 
-27.770137774905, -27.9949971815992, -28.2198565880586, -28.44471599428, 
-28.6695754002602, -28.8944348059959, -29.1192942114836, -29.3441536167201, 
-29.5690130217019, -29.7938724264254, -30.0187318308872, -30.2435912350837, 
-30.4684506390112, -30.693310042666, -30.9181694460445, -31.1430288491428, 
-31.3678882519571, -31.5927476544835, -31.8176070567181, -32.0424664586568, 
-32.2673258602956, -32.4921852616304, -32.7170446626569, -32.941904063371, 
-33.1667634637684, -33.3916228638447, -33.6164822635954, -33.841341663016, 
-34.066201062102, -34.2910604608488, -34.5159198592516, -34.7407792573057, 
-34.9656386550062, -35.1904980523482, -35.4153574493267, -35.6402168459366, 
-35.8650762421728, -36.0899356380299, -36.3147950335027, -36.5396544285858, 
-36.7645138232737, -36.9893732175608, -37.2142326114413, -37.4390920049096, 
-37.6639513979598, -37.8888107905859, -38.1136701827818, -38.3385295745415, 
-38.5633889658586, -38.7882483567267, -39.0131077471394, -39.2379671370901, 
-39.4628265265721, -39.6876859155785, -39.9125453041025, -40.137404692137, 
-40.3622640796748, -40.5871234667086, -40.8119828532309, -41.0368422392342, 
-41.2617016247108, -41.4865610096528, -41.7114203940523, -41.9362797779011, 
-42.161139161191, -42.3859985439135, -42.61085792606, -42.8357173076218, 
-43.06057668859, -43.2854360689555, -43.510295448709, -43.7351548278412, 
-43.9600142063424, -44.1848735842028, -44.4097329614124, -44.6345923379612, 
-44.8594517138386, -45.0843110890342, -45.3091704635371, -45.5340298373364, 
-45.7588892104209, -45.983748582779, -46.2086079543992, -46.4334673252694, 
-46.6583266953776, -46.8831860647114, -47.1080454332581, -47.3329048010047, 
-47.5577641679382, -47.7826235340449, -48.0074828993112, -48.232342263723, 
-48.457201627266, -48.6820609899255, -48.9069203516865, -49.1317797125338, 
-49.3566390724517, -49.5814984314242, -49.806357789435, -50.0312171464674, 
-50.2560765025044, -50.4809358575284, -50.7057952115217, -50.930654564466, 
-51.1555139163426, -51.3803732671325, -51.605232616816, -51.8300919653731, 
-52.0549513127834, -52.279810659026, -52.5046700040793, -52.7295293479214, 
-52.9543886905298, -53.1792480318815, -53.4041073719528, -53.6289667107195, 
-53.8538260481569, -54.0786853842395, -54.3035447189414, -54.5284040522357, 
-54.7532633840952, -54.9781227144917, -55.2029820433965, -55.4278413707801, 
-55.652700696612, -55.8775600208612, -56.1024193434958, -56.327278664483, 
-56.5521379837891, -56.7769973013796, -57.001856617219, -57.2267159312708, 
-57.4515752434975, -57.6764345538606, -57.9012938623206, -58.1261531688367, 
-58.351012473367, -58.5758717758686, -58.8007310762971, -59.025590374607, 
-59.2504496707513, -59.4753089646818, -59.7001682563488, -59.9250275457011, 
-60.149886832686, -60.3747461172492, -60.5996053993346, -60.8244646788845, 
-61.0493239558396, -61.2741832301384, -61.4990425017176, -61.723901770512, 
-61.9487610364542, -62.1736202994746, -62.3984795595014, -62.6233388164605, 
-62.8481980702752, -63.0730573208663, -63.297916568152, -63.5227758120477, 
-63.7476350524659, -63.972494289316, -64.1973535225043, -64.422212751934, 
-64.6470719775044, -64.8719311991118, -65.0967904166482, -65.3216496300021, 
-65.5465088390577, -65.7713680436948, -65.996227243789, -66.2210864392109, 
-66.4459456298263, -66.6708048154959, -66.8956639960749, -67.1205231714128, 
-67.3453823413531, -67.5702415057331, -67.7951006643835, -68.019959817128, 
-68.2448189637832, -68.4696781041579, -68.6945372380528, -68.9193963652602, 
-69.1442554855634, -69.3691145987363, -69.5939737045428, -69.8188328027362, 
-70.0436918930588, -70.2685509752413, -70.4934100490016, -70.7182691140447, 
-70.9431281700618, -71.1679872167291, -71.3928462537072, -71.6177052806403, 
-71.8425642971547, -72.0674233028583, -72.2922822973387, -72.5171412801625, 
-72.7420002508738, -72.9668592089926, -73.1917181540129, -73.4165770854017, 
-73.6414360025965, -73.8662949050035, -74.0911537919953, -74.3160126629084, 
-74.5408715170409, -74.7657303536496, -74.9905891719463, -75.2154479710953, 
-75.4403067502091, -75.6651655083445, -75.8900242444982, -76.1148829576022, 
-76.3397416465176, -76.5646003100298, -76.7894589468414, -77.0143175555649, 
-77.2391761347153, -77.464034682701, -77.6888931978141, -77.9137516782196, 
-78.1386101219434, -78.3634685268588, -78.5883268906718, -78.8131852109035, 
-79.0380434848719, -79.2629017096704, -79.4877598821437, -79.7126179988608, 
-79.9374760560837, -80.1623340497331, -80.3871919753479, -80.6120498280398, 
-80.8369076024407, -81.0617652926422, -81.2866228921265, -81.5114803936852, 
-81.7363377893254, -81.9611950701603, -82.1860522262803, -82.4109092466016, 
-82.6357661186873, -82.8606228285338, -83.0854793603169, -83.3103356960851, 
-83.5351918153906, -83.760047694839, -83.9849033075396, -84.2097586224261, 
-84.4346136034139, -84.6594682083445, -84.884322387651, -85.1091760826566, 
-85.3340292233812, -85.5588817256825, -85.7837334874826, -86.0085843837221, 
-86.2334342595074, -86.4582829206533, -86.6831301203839, -86.9079755402427, 
-87.1328187620395, -87.3576592255104, -87.5824961624204, -87.8073284902638, 
-88.0321546334029, -88.2569722065048, -88.4817774185774, -88.706563860905, 
-88.9313197834772, -89.1560210950552, -89.3806095512502, -89.6049004900231, 
-89.8278746458936, 
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
    660, 664, 668, 672, 676, 680, 684, 688, 692, 696,
    700, 704, 708, 712, 716, 720, 724, 728, 732, 736,
    740, 744, 748, 752, 756, 760, 764, 768, 772, 776,
    780, 784, 788, 792, 796, 800, 804, 808, 812, 816,
    820, 824, 828, 832, 836, 840, 844, 848, 852, 856,
    860, 864, 868, 872, 876, 880, 884, 888, 892, 896,
    900, 904, 908, 912, 916, 920, 924, 928, 932, 936,
    940, 944, 948, 952, 956, 960, 964, 968, 972, 976,
    980, 984, 988, 992, 996, 1000, 1004, 1008, 1012, 1016,
    1020, 1024, 1028, 1032, 1036, 1040, 1044, 1048, 1052, 1056,
    1060, 1064, 1068, 1072, 1076, 1080, 1084, 1088, 1092, 1096,
    1100, 1104, 1108, 1112, 1116, 1120, 1124, 1128, 1132, 1136,
    1140, 1144, 1148, 1152, 1156, 1160, 1164, 1168, 1172, 1176,
    1180, 1184, 1188, 1192, 1196, 1200, 1204, 1208, 1212, 1216,
    1220, 1224, 1228, 1232, 1236, 1240, 1244, 1248, 1252, 1256,
    1260, 1264, 1268, 1272, 1276, 1280, 1284, 1288, 1292, 1296,
    1300, 1304, 1308, 1312, 1316, 1320, 1324, 1328, 1332, 1336,
    1340, 1344, 1348, 1352, 1356, 1360, 1364, 1368, 1372, 1376,
    1380, 1384, 1388, 1392, 1396, 1400, 1404, 1408, 1412, 1416,
    1420, 1424, 1428, 1432, 1436, 1440, 1444, 1448, 1452, 1456,
    1460, 1464, 1468, 1472, 1476, 1480, 1484, 1488, 1492, 1496,
    1500, 1504, 1508, 1512, 1516, 1520, 1524, 1528, 1532, 1536,
    1540, 1544, 1548, 1552, 1556, 1560, 1564, 1568, 1572, 1576,
    1580, 1584, 1588, 1592, 1596, 1600, 1604, 1608, 1612, 1616,
    1616, 1612, 1608, 1604, 1600, 1596, 1592, 1588, 1584, 1580,
    1576, 1572, 1568, 1564, 1560, 1556, 1552, 1548, 1544, 1540,
    1536, 1532, 1528, 1524, 1520, 1516, 1512, 1508, 1504, 1500,
    1496, 1492, 1488, 1484, 1480, 1476, 1472, 1468, 1464, 1460,
    1456, 1452, 1448, 1444, 1440, 1436, 1432, 1428, 1424, 1420,
    1416, 1412, 1408, 1404, 1400, 1396, 1392, 1388, 1384, 1380,
    1376, 1372, 1368, 1364, 1360, 1356, 1352, 1348, 1344, 1340,
    1336, 1332, 1328, 1324, 1320, 1316, 1312, 1308, 1304, 1300,
    1296, 1292, 1288, 1284, 1280, 1276, 1272, 1268, 1264, 1260,
    1256, 1252, 1248, 1244, 1240, 1236, 1232, 1228, 1224, 1220,
    1216, 1212, 1208, 1204, 1200, 1196, 1192, 1188, 1184, 1180,
    1176, 1172, 1168, 1164, 1160, 1156, 1152, 1148, 1144, 1140,
    1136, 1132, 1128, 1124, 1120, 1116, 1112, 1108, 1104, 1100,
    1096, 1092, 1088, 1084, 1080, 1076, 1072, 1068, 1064, 1060,
    1056, 1052, 1048, 1044, 1040, 1036, 1032, 1028, 1024, 1020,
    1016, 1012, 1008, 1004, 1000, 996, 992, 988, 984, 980,
    976, 972, 968, 964, 960, 956, 952, 948, 944,
    940, 936, 932, 928, 924, 920, 916, 912, 908,
    904, 900, 896, 892, 888, 884, 880, 876, 872,
    868, 864, 860, 856, 852, 848, 844, 840, 836,
    832, 828, 824, 820, 816, 812, 808, 804, 800,
    796, 792, 788, 784, 780, 776, 772, 768, 764,
    760, 756, 752, 748, 744, 740, 736, 732, 728,
    724, 720, 716, 712, 708, 704, 700, 696, 692,
    688, 684, 680, 676, 672, 668, 664, 660, 656,
    652, 648, 644, 640, 636, 632, 628, 624, 620,
    616, 612, 608, 604, 600, 596, 592, 588, 584,
    580, 576, 572, 568, 564, 560, 556, 552, 548,
    544, 540, 536, 532, 528, 524, 520, 516, 512,
    508, 504, 500, 496, 492, 488, 484, 480, 476,
    472, 468, 464, 460, 456, 452, 448, 444, 440,
    436, 432, 428, 424, 420, 416, 412, 408, 404,
    400, 396, 392, 388, 384, 380, 376, 372, 368,
    364, 360, 356, 352, 348, 344, 340, 336, 332,
    328, 324, 320, 316, 312, 308, 304, 300, 296,
    292, 288, 284, 280, 276, 272, 268, 264, 260,
    256, 252, 248, 244, 240, 236, 232, 228, 224,
    220, 216, 212, 208, 204, 200, 196, 192, 188,
    184, 180, 176, 172, 168, 164, 160, 156, 152,
    148, 144, 140, 136, 132, 128, 124, 120, 116,
    112, 108, 104, 100, 96, 92, 88, 84, 80,
    76, 72, 68, 64, 60, 56, 52, 48, 44,
    40, 36, 32, 28, 24, 20,
)