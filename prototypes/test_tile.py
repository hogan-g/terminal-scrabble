import tile

# print(tile.tile_info["x"])

# test_tile = tile.Tile("a")

# print(test_tile)

test_bag = tile.TileBag()

#print(test_bag)

# test_bag.remove_tile("x")

# print(test_bag)

test_rack = tile.TileRack()

#print(test_rack.pretty_print())

test_rack.refill(test_bag)

print(test_rack.pretty_print())

test_rack.swap_out(test_bag)

print(test_rack.pretty_print())

#test_rack.shuffle()

#print(test_rack.pretty_print())

#test_rack.sort()

#print(test_rack.pretty_print())

#print("\n", test_bag, sep="")