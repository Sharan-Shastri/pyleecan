# -*- coding: utf-8 -*-
"""
@date Created on Tue Apr 25 12:02:09 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
"""

import sys
from random import uniform
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW13 import SlotW13
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot13.PWSlot13 import PWSlot13


class test_PWSlot13(TestCase):
    """Test that the widget PWSlot13 behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW13(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            W3=0.16,
            H1_is_rad=False,
        )
        self.widget = PWSlot13(self.test_obj)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot13")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        self.assertEqual(self.widget.lf_H0.value(), 0.10)
        self.assertEqual(self.widget.lf_H1.value(), 0.11)
        self.assertEqual(self.widget.lf_H2.value(), 0.12)
        self.assertEqual(self.widget.lf_W0.value(), 0.13)
        self.assertEqual(self.widget.lf_W1.value(), 0.14)
        self.assertEqual(self.widget.lf_W2.value(), 0.15)
        self.assertEqual(self.widget.lf_W3.value(), 0.16)
        # Index 0 is m
        self.assertEqual(self.widget.c_H1_unit.currentIndex(), 0)

        self.test_obj.slot = SlotW13(
            H0=0.20,
            H1=0.21,
            H2=0.22,
            W0=0.23,
            W1=0.24,
            W2=0.25,
            W3=0.26,
            H1_is_rad=True,
        )
        self.widget = PWSlot13(self.test_obj)
        self.assertEqual(self.widget.lf_H0.value(), 0.20)
        self.assertEqual(self.widget.lf_H1.value(), 0.21)
        self.assertEqual(self.widget.lf_H2.value(), 0.22)
        self.assertEqual(self.widget.lf_W0.value(), 0.23)
        self.assertEqual(self.widget.lf_W1.value(), 0.24)
        self.assertEqual(self.widget.lf_W2.value(), 0.25)
        self.assertEqual(self.widget.lf_W3.value(), 0.26)
        # Index 1 is rad
        self.assertEqual(self.widget.c_H1_unit.currentIndex(), 1)

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H0, str(value))
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H0, value)

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H1, str(value))
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H1, value)

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H2, str(value))
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H2, value)

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        self.widget.lf_W0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W0, str(value))
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W0, value)

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        self.widget.lf_W1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W1, str(value))
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W1, value)

    def test_set_W2(self):
        """Check that the Widget allow to update W2"""
        self.widget.lf_W2.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W2, str(value))
        self.widget.lf_W2.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W2, value)

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W3, str(value))
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W3, value)

    def test_set_H1_is_rad(self):
        """Check that the Widget allow to update H1_is_rad"""
        self.assertTrue(not self.test_obj.slot.H1_is_rad)

        self.widget.c_H1_unit.setCurrentIndex(1)  # Index 1 is rad

        self.assertTrue(self.test_obj.slot.H1_is_rad)

    def test_output_txt(self):
        """Check that the Output text is computed and correct
        """
        self.test_obj.slot = SlotW13(
            H0=0.005,
            H1=0.01,
            H2=0.02,
            W0=0.005,
            W1=0.02,
            W2=0.01,
            W3=0.025,
            H1_is_rad=False,
        )
        self.widget = PWSlot13(self.test_obj)
        self.assertEqual(
            self.widget.w_out.out_slot_height.text(), "Slot height: 0.03502 m"
        )
