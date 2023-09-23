image = gimp.image_list()[0]
sel = pdb.gimp_selection_float(image.active_layer, 0, 0)
pdb.gimp_floating_sel_to_layer(sel)
pdb.gimp_item_set_visible(sel, 0)
