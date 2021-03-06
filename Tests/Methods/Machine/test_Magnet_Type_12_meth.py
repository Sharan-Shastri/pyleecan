# -*- coding: utf-8 -*-
"""
@date Created on Thu Dec 18 13:56:20 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from unittest import TestCase

from ddt import ddt, data

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotMFlat import SlotMFlat
from pyleecan.Classes.MagnetType12 import MagnetType12
from pyleecan.Methods.Machine.Magnet.comp_surface import comp_surface

from numpy import exp

Mag12_test = list()
# Internal Slot
lam = LamSlotMag(is_internal=True, Rext=0.1325)
lam.slot = SlotMFlat(H0=5e-3, W0=10e-3, Zs=12)
lam.slot.magnet = [MagnetType12(Hmag=5e-3, Wmag=10e-3)]
Mag12_test.append(
    {"test_obj": lam, "S_exp": 5.062918e-5, "Ao": 0.078449, "H_exp": 5e-3}
)

# Outward Slot
lam = LamSlotMag(is_internal=False, Rint=0.1325)
lam.slot = SlotMFlat(H0=5e-3, W0=10e-3, Zs=12)
lam.slot.magnet = [MagnetType12(Hmag=5e-3, Wmag=10e-3)]
Mag12_test.append({"test_obj": lam, "S_exp": 4.937e-5, "Ao": 0.072745, "H_exp": 5e-3})

# For AlmostEqual
DELTA = 1e-4


@ddt
class test_Magnet_Type_12_meth(TestCase):
    """unittest for MagnetType12 methods
    """

    @data(*Mag12_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

        # Compare numerical and analytical results
        b = comp_surface(test_obj.slot.magnet[0])
        msg = "Analytical: " + str(a) + " Numerical " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*Mag12_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*Mag12_test)
    def test_comp_angle_op(self, test_dict):
        """Check that the computation of the opening angle is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_angle_opening()

        a = result
        b = test_dict["Ao"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)
