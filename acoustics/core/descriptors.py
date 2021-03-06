from __future__ import division

import numpy as np

from acoustics.utils.utils import _e10


def _leq(levels, time):
    if type(levels) is list:
        levels = np.array(levels)
    return 10 * np.log10((1/time) * np.sum(_e10(levels)))


def leq(levels, int_time=1):
    '''
    Sum of levels in dB.
    '''
    if type(levels) is list:
        levels = np.array(levels)
    time = levels.size * int_time
    return _leq(levels, time)


def sel(levels):
    '''
    Sound Exposure Level from ``levels`` (NumPy array).
    '''
    if type(levels) is list:
        levels = np.array(levels)
    return _leq(levels, 1)


def lw(W, Wref=1e-12):
    '''
    Sound power level for ``W`` with ``Wref`` as reference ($10^{-12}$
    by default).
    '''
    if type(W) is list:
        W = np.array(W)
    return 10 * np.log10(W/Wref)


def lden(lday, levening, lnight):
    '''
    Calculate $L_{DEN}$ from ``lday``, ``levening`` and ``lnight``.
    '''
    if type(lday) is list:
        lday = np.array(lday)
    if type(levening) is list:
        levening = np.array(levening)
    if type(lnight) is list:
        lnight = np.array(lnight)
    day = 12*_e10(lday)
    evening = 4*_e10(levening+5)
    night = 8*_e10(lnight+10)
    return 10 * np.log10((day + evening + night) / 24)


def ldn(lday, lnight):
    '''
    Calculate $L_{DN}$ from ``lday`` and ``lnight``.
    '''
    if type(lday) is list:
        lday = np.array(lday)
    if type(lnight) is list:
        lnight = np.array(lnight)
    day = 15*_e10(lday)
    night = 9*_e10(lnight+10)
    return 10 * np.log10((day + night) / 24)
