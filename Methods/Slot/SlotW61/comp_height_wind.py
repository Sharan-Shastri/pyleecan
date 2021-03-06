# -*- coding: utf-8 -*-
"""@packageMethods.Machine.SlotW60.comp_height_wind
Slot Type_6_0 computation of the height of the winding area method
@date Created on Wed Aug 01 12:31:16 2018
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import pi, exp


def comp_height_wind(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW61
        A SlotW61 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10] = self._comp_point_coordinate()

    # Compute the point in the tooth ref
    hsp = pi / self.Zs
    Z4t = Z4 * exp(1j * hsp)
    Z5t = Z5 * exp(1j * hsp)
    Zw4t = Z4t - self.H3 + 1j * ((self.W1 - self.W2) / 2 - self.W3)
    Zw2t = Z5t + self.H4

    return abs(Zw4t) - abs(Zw2t)
