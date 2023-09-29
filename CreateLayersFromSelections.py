#!/usr/bin/env python

# Import the GIMP module
from gimpfu import *


def create_layer_from_selection(image, drawable):
    if pdb.gimp_selection_is_empty(image):
        pdb.gimp_message("No selection found. Please make a selection first.")
        return
    sel = pdb.gimp_selection_float(image.active_layer, 0, 0)
    pdb.gimp_floating_sel_to_layer(sel)
    pdb.gimp_item_set_name(sel, "New Layer from Selection")
    pdb.gimp_item_set_visible(sel, 0)


# Register the Python-Fu procedure with GIMP
register(
    "python_fu_create_layer_from_selection",
    "Create Layer From Selection",
    "Creates a layer from the current selection.",
    "Evan Williams",
    "Evan Williams",
    "2023",
    "<Image>/Filters/Evan's Custom Scripts/Create Layer From Selection...",
    "*",
    [],
    [],
    create_layer_from_selection,
)

# Create a GIMP menu entry under "Filters"
main()
