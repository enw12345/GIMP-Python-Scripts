#!/usr/bin/env python

# Import the GIMP module
from gimpfu import *

# 11.8, 51.4, 27.5


def get_all_layers(image, drawable, replace, place):
    layers = image.layers

    old_foreground_color = pdb.gimp_context_get_foreground()
    old_paint_mode = pdb.gimp_context_get_paint_mode()
    old_sample_transparent = pdb.gimp_context_get_sample_transparent()
    old_sample_threshold = pdb.gimp_context_get_sample_threshold()
    old_sample_merged = pdb.gimp_context_get_sample_merged()

    pdb.gimp_context_set_sample_transparent(0)
    pdb.gimp_context_set_foreground(place)
    pdb.gimp_context_set_paint_mode(28)
    pdb.gimp_context_set_sample_threshold(0)
    pdb.gimp_context_set_sample_merged(0)

    for x in layers:
        set_active_layer(image, x)
        change_active_layer_color(image, replace)

    pdb.gimp_context_set_foreground(old_foreground_color)
    pdb.gimp_context_set_paint_mode(old_paint_mode)
    pdb.gimp_context_set_sample_transparent(old_sample_transparent)
    pdb.gimp_context_set_sample_threshold(old_sample_threshold)
    pdb.gimp_context_set_sample_merged(old_sample_merged)


def set_active_layer(image, layer):
    try:
        if layer:
            # Set the found layer as the active layer
            pdb.gimp_image_set_active_layer(image, layer)
        else:
            pdb.gimp_message("Layer with ID {} not found in the image.".format(layer))

    except Exception as e:
        pdb.gimp_message("Error: {}".format(str(e)))


def change_active_layer_color(image, replace):
    active_layer = pdb.gimp_image_get_active_layer(image)

    # Find the color in that layer and make it a part of the selection
    pdb.gimp_image_select_color(image, 2, active_layer, replace)

    # Change the slection color to that color
    pdb.gimp_drawable_edit_fill(active_layer, 0)


# Register the Python-Fu procedure with GIMP
register(
    "python_fu_change_replace_in_all_layers",
    "Replace Color In All Layers",
    "Goes through all layers and replaces the color of the selection in all the layers of the image.",
    "Evan Williams",
    "Evan Williams",
    "2023",
    "<Image>/Filters/Evan's Custom Scripts/Replace color in all layers...",
    "*",
    [
        (PF_COLOR, "replace", "The color to replace in all layers:", (11, 51, 27)),
        (PF_COLOR, "place", "The color to place in all layers:", (255, 255, 255)),
    ],
    [],
    get_all_layers,
)

# Create a GIMP menu entry under "Filters"
main()
