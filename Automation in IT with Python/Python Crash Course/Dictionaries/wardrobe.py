wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item in wardrobe:
	for color in wardrobe[item]:
		print("{} {}".format(color, item))
