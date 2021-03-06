# -*- coding: utf-8 -*-
"""File generated according to pyleecan/Generator/ClassesRef/Machine/Notch.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from pyleecan.Classes._check import check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Machine.Notch.get_Rbo import get_Rbo
except ImportError as error:
    get_Rbo = error

try:
    from pyleecan.Methods.Machine.Notch.is_outwards import is_outwards
except ImportError as error:
    is_outwards = error


from pyleecan.Classes._check import InitUnKnowClassError


class Notch(FrozenClass):
    """Abstract class for notches"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.Notch.get_Rbo
    if isinstance(get_Rbo, ImportError):
        get_Rbo = property(
            fget=lambda x: raise_(
                ImportError("Can't use Notch method get_Rbo: " + str(get_Rbo))
            )
        )
    else:
        get_Rbo = get_Rbo
    # cf Methods.Machine.Notch.is_outwards
    if isinstance(is_outwards, ImportError):
        is_outwards = property(
            fget=lambda x: raise_(
                ImportError("Can't use Notch method is_outwards: " + str(is_outwards))
            )
        )
    else:
        is_outwards = is_outwards
    # save method is available in all object
    save = save

    def __init__(self, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, [])
        # The class is frozen, for now it's impossible to add new properties
        self.parent = None
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Notch_str = ""
        if self.parent is None:
            Notch_str += "parent = None " + linesep
        else:
            Notch_str += "parent = " + str(type(self.parent)) + " object" + linesep
        return Notch_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Notch_dict = dict()
        # The class name is added to the dict fordeserialisation purpose
        Notch_dict["__class__"] = "Notch"
        return Notch_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""
