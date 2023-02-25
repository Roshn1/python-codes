'''Program that calculates the number of rectangular tiles required to cover a rectangular floor if
the dimensions of the floor and the dimensions of a tile are entered by the user'''

l = float(input("Enter the length of floor"))
b = float(input("Enter the breadth of floor"))
areafloor = l*b

lt = float(input("Enter the length of tile"))
bt = float(input("Enter the breadth of tile"))
areatile = lt*bt

numoftile = areafloor/areatile

print("Tiles required = ",numoftile)