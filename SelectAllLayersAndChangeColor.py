image = gimp.image_list()[0]
num_layers, layer_ids = pdb.gimp_image_get_layers(image)
for x in layer_ids:
    #set active layer: pdb.gimp_image_set_active_layer(image, active_layer)