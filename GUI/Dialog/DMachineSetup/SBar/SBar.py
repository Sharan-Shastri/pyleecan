# -*- coding: utf-8 -*-
"""@package pyleecan.GUI.Dialog.DMachineSetup.SBar.SBar
Last Page of the Machine (Type 1 only) Setup: Rotor Bar
@date Created on Thu Jul 30 10:47:56 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from pyleecan.GUI import gui_option
from pyleecan.GUI.Dialog.DMachineSetup.SBar.Gen_SBar import Gen_SBar
from pyleecan.GUI.Dialog.DMachineSetup.SBar.PCondType21.PCondType21 import PCondType21
from pyleecan.GUI.Dialog.DMachineSetup.SBar.PCondType22.PCondType22 import PCondType22

# Information to fill the conductor type combobox
WIDGET_LIST = [PCondType21, PCondType22]
INIT_INDEX = [wid.cond_type for wid in WIDGET_LIST]
COND_NAME = [wid.cond_name for wid in WIDGET_LIST]


class SBar(Gen_SBar, QWidget):
    """Step to setup the Rotor Bar for SCIM machine
    """

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()
    # Information for the DMachineSetup nav
    step_name = "Bar"

    def __init__(self, machine, matlib=[], is_stator=False):
        """Initialize the widget according to machine

        Parameters
        ----------
        self : SBar
            A SBar widget
        machine : Machine
            current machine to edit
        matlib : list
            List of available Material
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Saving arguments
        self.machine = machine
        self.matlib = matlib
        self.is_stator = is_stator

        # Set FloatEdit unit
        self.lf_Hscr.unit = "m"
        self.lf_Lscr.unit = "m"
        self.lf_Lewout.unit = "m"
        # Set unit name (m ou mm)
        wid_list = [self.unit_Hscr, self.unit_Lscr, self.unit_Lewout]
        for wid in wid_list:
            wid.setText(gui_option.unit.get_m_name())

        # Set materials
        self.w_mat.def_mat = "Copper1"
        self.w_mat.setText("Ring material:")
        self.w_mat.update(self.machine.rotor, 'ring_mat', matlib)

        # Initialize the GUI with the current machine value
        self.lf_Hscr.setValue(machine.rotor.Hscr)
        self.lf_Lscr.setValue(machine.rotor.Lscr)
        self.lf_Lewout.setValue(machine.rotor.winding.Lewout)

        # Fill the combobox
        self.c_bar_type.clear()
        for cond in COND_NAME:
            self.c_bar_type.addItem(cond)
        # Initialize the needed conductor page
        conductor = machine.rotor.winding.conductor
        if type(conductor) in INIT_INDEX:
            index = INIT_INDEX.index(type(conductor))
            self.g_bar.layout().removeWidget(self.w_bar)
            self.w_bar.setParent(None)
            self.w_bar = WIDGET_LIST[index](self.machine, self.matlib)
            self.g_bar.layout().addWidget(self.w_bar)
            self.c_bar_type.setCurrentIndex(index)
        else:  # Set default conductor
            self.s_set_bar_type(0)
            self.c_bar_type.setCurrentIndex(0)
        self.w_bar.saveNeeded.connect(self.emit_save)

        # Connect the signal/slot
        self.lf_Hscr.editingFinished.connect(self.set_Hscr)
        self.lf_Lscr.editingFinished.connect(self.set_Lscr)
        self.lf_Lewout.editingFinished.connect(self.set_Lewout)
        self.c_bar_type.currentIndexChanged.connect(self.s_set_bar_type)
        self.b_plot.clicked.connect(self.s_plot)
        self.w_mat.saveNeeded.connect(self.emit_save)

    def emit_save(self):
        """Emit the saveNeeded signal
        """
        self.saveNeeded.emit()

    def set_Hscr(self):
        """Signal to update the value of Hscr according to the line edit

        Parameters
        ----------
        self : SBar
            A SBar object
        """
        self.machine.rotor.Hscr = self.lf_Hscr.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Lscr(self):
        """Signal to update the value of Lscr according to the line edit

        Parameters
        ----------
        self : SBar
            A SBar object
        """
        self.machine.rotor.Lscr = self.lf_Lscr.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Lewout(self):
        """Signal to update the value of Lewout according to the line edit

        Parameters
        ----------
        self : SBar
            A SBar object
        """
        self.machine.rotor.winding.Lewout = self.lf_Lewout.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def s_set_bar_type(self, index):
        """Setup the Gui for the selected conductor type

        Parameters
        ----------
        self : SBar
            A SBar object
        index : int
            Index of the selected conductor type
        """

        # Remove the old widget
        self.g_bar.layout().removeWidget(self.w_bar)
        self.w_bar.setParent(None)

        # Initialize the new widget and conductor
        self.machine.rotor.winding.conductor = INIT_INDEX[index]()
        self.machine.rotor.winding.conductor._set_None()

        self.w_bar = WIDGET_LIST[index](self.machine, self.matlib)
        self.w_bar.saveNeeded.connect(self.emit_save)
        # Refresh the GUi
        self.g_bar.layout().addWidget(self.w_bar)
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def s_plot(self):
        """Try to plot the machine

        Parameters
        ----------
        self : SBar
            A SBar object
        """
        self.machine.plot()
