# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW15.comp_surface
SlotW15 Computation of surface method
@date Created on Mon Nov 27 12:22:18 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from numpy import cos, sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW15
        A SlotW15 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    Rbo = self.get_Rbo()

    Swind = self.comp_surface_wind()

    # The bottom is an arc
    alpha = self.comp_angle_opening()
    Sarc = (Rbo ** 2.0) / 2.0 * (alpha - sin(alpha))
    Harc = float(Rbo * (1 - cos(alpha / 2)))
    S1 = (self.H0 + Harc) * self.W0

    # Because Slamination = S - Zs * Sslot
    if self.is_outwards():
        return S1 + Swind - Sarc
