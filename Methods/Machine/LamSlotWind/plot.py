# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlotWind.plot
Lamination with Winding plot method
@date Created on Wed Dec 10 10:35:39 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from matplotlib.patches import Patch
from matplotlib.pyplot import axis, legend

from pyleecan.Functions.Winding.find_wind_phase_color import find_wind_phase_color
from pyleecan.Functions.init_fig import init_fig
from pyleecan.Methods.Machine import PHASE_COLOR, PHASE_NAME, ROTOR_COLOR, STATOR_COLOR
from pyleecan.Classes.WindingSC import WindingSC


def plot(
    self,
    fig=None,
    is_lam_only=False,
    sym=1,
    alpha=0,
    delta=0,
    is_edge_only=False,
    is_display=True,
):
    """Plot the Lamination in a matplotlib fig

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object
    fig :
        if None, open a new fig and plot, else add to the current
        one (Default value = None)
    is_lam_only : bool
        True to plot only the lamination (remove the Winding)
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_edge_only: bool
        To plot transparent Patches
    is_display : bool
        False to return the patches
    Returns
    -------
    patches : list
        List of Patches
    """
    if self.is_stator:
        color_lam = STATOR_COLOR
    else:
        color_lam = ROTOR_COLOR

    Zs = self.slot.Zs
    # Get the LamSlot surface(s)
    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)

    patches = list()
    # getting the matrix  wind_mat [Nrad,Ntan,Zs,qs] representing the winding
    if type(self.winding) is WindingSC:
        wind_mat = None
    else:
        try:
            wind_mat = self.winding.comp_connection_mat(Zs)
            (Nrad, Ntan, Zs, qs) = wind_mat.shape
        except Exception:
            wind_mat = None
    if wind_mat is None:
        qs = 1  # getting number of surface in winding Zone in the Slot
    for surf in surf_list:
        if surf.label is not None and "_Ext" in surf.label:
            patches.append(surf.get_patch(color_lam, is_edge_only=is_edge_only))
        elif surf.label is not None and "_In" in surf.label:
            patches.append(surf.get_patch(is_edge_only=is_edge_only))
        elif "Wind" in surf.label or "Bar" in surf.label:
            if not is_lam_only:
                color = find_wind_phase_color(wind_mat=wind_mat, label=surf.label)
                patches.append(surf.get_patch(color=color, is_edge_only=is_edge_only))
        else:
            patches.append(surf.get_patch(is_edge_only=is_edge_only))

    if is_display:
        # Display the result
        (fig, axes, patch_leg, label_leg) = init_fig(fig)
        axes.set_xlabel("(m)")
        axes.set_ylabel("(m)")
        for patch in patches:
            axes.add_patch(patch)
        # Axis Setup
        axis("equal")

        # The Lamination is centered in the figure
        Lim = self.Rext * 1.5
        axes.set_xlim(-Lim, Lim)
        axes.set_ylim(-Lim, Lim)

        # Add the legend
        if not is_edge_only:
            if self.is_stator:
                patch_leg.append(Patch(color=STATOR_COLOR))
                label_leg.append("Stator")
                axes.set_title("Stator with Winding")
            else:
                patch_leg.append(Patch(color=ROTOR_COLOR))
                label_leg.append("Rotor")
                axes.set_title("Rotor with Winding")
            # Add the winding legend only if needed
            if not is_lam_only:
                for ii in range(qs):
                    if not ("Phase " + PHASE_NAME[ii] in label_leg):
                        # Avoid adding twice the same label
                        index = ii % len(PHASE_COLOR)
                        patch_leg.append(Patch(color=PHASE_COLOR[index]))
                        label_leg.append("Phase " + PHASE_NAME[ii])
            legend(patch_leg, label_leg)
        fig.show()
    else:
        return patches
