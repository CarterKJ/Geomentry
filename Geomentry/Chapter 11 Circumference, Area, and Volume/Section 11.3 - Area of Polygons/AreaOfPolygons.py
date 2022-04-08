def AreaPoly(rad,sidelen,sides):
    return(.5*(rad*(sidelen*sides)))
    
while True:
    rad = float(input("Enter rad:"))
    sidelen = float(input("Enter side length:"))
    sides = int(input("Enter num of sides:"))
    print(AreaPoly(rad,sidelen,sides))
    print()
