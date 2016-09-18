# Simple-Dungeon-Generator
This is a script for creating dungeon like cave maps.
Please feel free to use in your projects.

The script works as an external library. It has the following public methods:
object.mapMaker(100, 100, 5, 10) #creates the map, has to be called after initialization
#x = map width
#y = map height
#z = minimum room size (smallest allowed)
#k = max room size (biggest allowed)
object.printMap() #prints the map
object.getMap() #returns the map in a 2d array
object.save("mapname.txt") #saves the genenerated map to a txt file with the specified name
# if no parameter is given the file will be named "map.txt"