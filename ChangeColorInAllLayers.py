#!/usr/bin/env python

# Import the GIMP module
from gimpfu import *

# image = gimp.image_list()[0]
# num_layers, layer_ids = pdb.gimp_image_get_layers(image)
# for x in layer_ids:
# set active layer: pdb.gimp_image_set_active_layer(image, active_layer)


def get_all_layers(image, drawable):
    layers = image.layers

    for x in layers:
        set_active_layer(image, x)


def set_active_layer(image, layer):
    try:
        # Find the layer by its ID
        # layer = pdb.gimp_image_get_layer_by_id(image, layer_id)
        # layer = image.get_layer_by_ID(layer_id)

        if layer:
            # Set the found layer as the active layer
            pdb.gimp_image_set_active_layer(image, layer)
        else:
            pdb.gimp_message("Layer with ID {} not found in the image.".format(layer))
            
        change_active_layer_color(image)

    except Exception as e:
        pdb.gimp_message("Error: {}".format(str(e)))


def change_active_layer_color(image):
    active_layer = pdb.gimp_image_get_active_layer(image)
    


# Register the Python-Fu procedure with GIMP
register(
    "python_fu_change_color_in_all_layers",
    "Change Color In All Layers",
    "Goes through all layers and changes the color of the selection in the layers.",
    "Evan Williams",
    "Evan Williams",
    "2023",
    "<Image>/Filters/Change color in all layers...",
    "*",
    [],
    [],
    get_all_layers,
)

# Create a GIMP menu entry under "Filters"
main()
