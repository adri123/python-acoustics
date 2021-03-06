"""
Weightings according to IEC 61672-1:2003.
"""
from __future__ import division

import numpy as np

from acoustics.core.bands import third

THIRD_OCTAVE_A_WEIGHTING = np.array([-63.4, -56.7, -50.5, -44.7, -39.4, -34.6,
                                    -30.2, -26.2, -22.5, -19.1, -16.1, -13.4,
                                    -10.9,  -8.6,  -6.6,  -4.8,  -3.2,  -1.9,
                                    -0.8,      0,   0.6,     1,   1.2,   1.3,
                                    1.2,       1,   0.5,  -0.1,  -1.1,  -2.5,
                                    -4.3,   -6.6,  -9.3])
"""
A-weighting filter for preferred 1/3-octave band center frequencies, as specified in :attr:`acoustics.core.bands.THIRD_OCTAVE_CENTER_FREQUENCIES`.
"""

THIRD_OCTAVE_C_WEIGHTING = np.array([-11.2, -8.5,  -6.2, -4.4,   -3,   -2,
                                    -1.3,  -0.8,  -0.5, -0.3, -0.2, -0.1,
                                    0,        0,     0,    0,    0,    0,
                                    0,        0,     0, -0.1, -0.2, -0.3,
                                    -0.5,  -0.8,  -1.3,   -2,   -3, -4.4,
                                    -6.2,  -8.5, -11.2])
"""
C-weighting filter for preferred 1/3-octave band center frequencies, as specified in :attr:`acoustics.core.bands.THIRD_OCTAVE_CENTER_FREQUENCIES`.
"""


def a_weighting(first, last):
    """
    Select frequency weightings between ``first`` and ``last``
    centerfrequencies from A-weighting.
    Possible values for these frequencies are third-octave frequencies
    between 12.5 Hz and 20,000 Hz (including them).

    Parameters
    ----------
    first : scalar
       First third-octave centerfrequency.

    last : scalar
        Last third-octave centerfrequency.

    Returns
    -------
    NumPy array with A-weighting between ``first`` and ``last``
    centerfrequencies.
    """
    return _weighting("a", first, last)


def c_weighting(first, last):
    """
    Select frequency weightings between ``first`` and ``last``
    centerfrequencies from C-weighting.
    Possible values for these frequencies are third-octave frequencies
    between 12.5 Hz and 20,000 Hz (including them).

    Parameters
    ----------
    first : scalar
       First third-octave centerfrequency.

    last : scalar
        Last third-octave centerfrequency.

    Returns
    -------
    NumPy array with A-weighting between ``first`` and ``last``
    centerfrequencies.
    """
    return _weighting("c", first, last)


def _weighting(filter_type, first, last):
    third_oct_bands = third(12.5, 20000)
    low = np.where(third_oct_bands == first)[0]
    high = np.where(third_oct_bands == last)[0]

    if filter_type == "a":
        freq_weightings = THIRD_OCTAVE_A_WEIGHTING

    elif filter_type == "c":
        freq_weightings = THIRD_OCTAVE_C_WEIGHTING
        
    return freq_weightings[low: high+1]


def z2a(levels, first, last):
    return levels + a_weighting(first, last)


def a2z(levels, first, last):
    return levels - a_weighting(first, last)


def z2c(levels, first, last):
    return levels + c_weighting(first, last)


def c2z(levels, first, last):
    return levels - c_weighting(first, last)


def a2c(levels, first, last):
    dB = a2z(levels, first, last)
    return z2c(dB, first, last)


def c2a(levels, first, last):
    dB = c2z(levels, first, last)
    return z2a(dB, first, last)
