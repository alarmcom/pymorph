import pymorph
import numpy as np

def test_erode():
    f = np.zeros((8,8), np.bool)
    Bs = [np.reshape(B, (3,3)) for B in (
                    [1,1,0, 1,1,0, 0,0,0],
                    [1,0,0, 1,1,0, 0,0,0],
                    [1,0,0, 0,1,0, 0,0,0],
                    [0,1,0, 0,1,0, 0,0,0],
                    )]
    for B in Bs:
        assert pymorph.erode(f, B != 0).sum() == 0
        assert pymorph.erode(f, B).sum() == 0

def test_erode_mixed_types():
    A  = np.array([[1,0],[0,1]])
    f = np.zeros((4,4), np.bool)
    f[2,2] = 1
    f[3,3] = 1
    assert pymorph.erode(f,A).sum() == 1

