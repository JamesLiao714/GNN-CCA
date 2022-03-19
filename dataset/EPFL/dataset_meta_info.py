# Meta information about datasets

DatasetMetaInfo = {
    'basketball': {
        'annot_fn_pattern': 'match5-c{}.txt',
        'video_fn_pattern': 'match5-c{}.avi',
        'cam_nbr': 4,
        'video_frame_nbr': 9368,
        'valid_frames_range': (0, 9367),
        'video_hwc': (288, 360, 3),
        'homography': [  # ground plane homography
            [  # cam 0
                [0.973210218360093, 0.107672014080801, -589.549693080953],
                [0.660843995806483, -10.3802474969403, 691.576918676405],
                [-5.41776439680038e-05, -0.00341082938790488, 0.115386342207633]
            ],
            [  # cam 1
                [0.651889881765098, -9.29642248626189, 562.350164311156],
                [-1.24737970354096, -10.2911630523550, 1021.77620262286],
                [-0.000140603286167156, -0.00346052744574214, 0.128423692855964]
            ],
            [  # cam 2
                [1.01024676910245, 9.15807731339380, -829.603109385851],
                [0.806454941925672, -1.10323798232598, 357.038302851965],
                [4.85216260160755e-05, 0.00330786999873228, -0.0834408557306429]
            ],
            [  # cam 3
                [-1.07205430845160, 0.376247352099919, -290.636279634342],
                [1.07522284120120, 0.995541758677926, -686.637757692985],
                [4.45250980164576e-05, -0.00409806981593118, 0.157458373405075]
            ]
        ]
    },
    'campus': {
        'annot_fn_pattern': 'campus7-c{}.txt',
        'video_fn_pattern': 'campus7-c{}.avi',
        'cam_nbr': 3,
        'video_frames_nbr': 5884,
        'valid_frames_range': (0, 4870),  # frame 4871 ~ 5847 are broken
        'video_hwc': (288, 360, 3),
        'homography': [
            [
                [-0.211332, -0.405226, 70.781223],
                [-0.019746, -1.564936, 226.377280],
                [-0.000025, -0.001961, 0.160791]
            ],
            [
                [0.000745, 0.350335, -98.376103],
                [-0.164871, -0.390422, 54.081423],
                [0.000021, -0.001668, 0.111075]
            ],
            [
                [0.089976, 1.066795, -152.055667],
                [-0.116343, 0.861342, -75.122116],
                [0.000015, 0.001442, -0.064065]
            ]
        ]
    },
    'laboratory': {
        'annot_fn_pattern': '6p-c{}.txt',
        'video_fn_pattern': '6p-c{}.avi',
        'cam_nbr': 4,
        'video_frames_nbr': 2955,
        'valid_frames_range': (0, 2954),
        'video_hwc': (288, 360, 3),
        'homography': [
            [
                [0.176138, 0.647589, -63.412272],
                [-0.180912, 0.622446, -0.125533],
                [-0.000002, 0.001756, 0.102316]
            ],
            [
                [0.177291, 0.004724, 31.224545],
                [0.169895, 0.661935, -79.781865],
                [-0.000028, 0.001888, 0.054634]
            ],
            [
                [-0.104843, 0.099275, 50.734500],
                [0.107082, 0.102216, 7.822562],
                [-0.000054, 0.001922, -0.068053]
            ],
            [
                [-0.142865, 0.553150, -17.395045],
                [-0.125726, 0.039770, 75.937144],
                [-0.000011, 0.001780, 0.015675]
            ]
        ]
    },
    'passageway': {
        'annot_fn_pattern': 'passageway1-c{}.txt',
        'video_fn_pattern': 'passageway1-c{}.avi',
        'cam_nbr': 4,
        'video_frames_nbr': 2500,
        'valid_frames_range': (0, 2499),
        'video_hwc': (288, 360, 3),
        'homography': [
            [
                [-0.0000245975, -0.0000047863, 0.0181735812],
                [0.0000056945, 0.0000089998, 0.0243277264],
                [-0.0000000067, 0.0000006977, -0.0000552219]
            ],
            [
                [-0.0000110292, 0.0000768559, -0.0105851797],
                [-0.0000097598, 0.0000196797, 0.0130811407],
                [0.0000000029, 0.0000004326, -0.0000362086]
            ],
            [
                [-0.0000145114, -0.0000570495, 0.0140615401],
                [-0.0000033340, -0.0001351901, 0.0189803318],
                [-0.0000000260, -0.0000003176, 0.0000289364]
            ],
            [
                [0.0013816829, 0.0001111826, -0.1471471590],
                [0.0004031272, 0.0153807950, -2.8417419736],
                [0.0000000011, 0.0000330623, -0.0031355590]
            ]
        ]
    },
    'terrace': {
        'annot_fn_pattern': 'terrace1-c{}.txt',
        'video_fn_pattern': 'terrace1-c{}.avi',
        'cam_nbr': 4,
        'video_frames_nbr': 5010,
        'valid_frames_range': (0, 4887),  # frame 4888 ~ 5009 are empty (without any detections)
        'video_hwc': (288, 360, 3),
        'homography': [
            [
                [-1.6688907435, -6.9502305710, 940.69592392565],
                [1.1984806153, -10.7495778320, 868.29873467315],
                [0.0004069210, -0.0209324057, 0.42949125235]
            ],
            [
                [0.6174778372, -0.4836875683, 147.00510919005],
                [0.5798503075, 3.8204849039, -386.096405131],
                [0.0000000001, 0.0077222239, -0.01593391935]
            ],
            [
                [-0.2717592338, 1.0286363982, -17.6643219215],
                [-0.1373600672, -0.3326731339, 161.0109069274],
                [0.0000600052, 0.0030858398, -0.04195162855]
            ],
            [
                [-0.3286861858, 0.1142963200, 130.25528281945],
                [0.1809954834, -0.2059386455, 125.0260427323],
                [0.0000693641, 0.0040168154, -0.08284534995]
            ]
        ]
    }
}