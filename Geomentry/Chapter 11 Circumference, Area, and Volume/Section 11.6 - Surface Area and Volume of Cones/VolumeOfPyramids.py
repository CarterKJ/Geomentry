#Only works for triangular and rectangular pyramids so far
def volume_pyramid(side1,side2,height,sides):
    if sides == 3:
        return (1/3)*((side2*side1)/2)* height
    else:
        return (1/3)*(side2*side1)* height
    
while True:
    sides = float(input("Ender base sides:"))
    side1 = float(input("Ender side 1:"))
    side2 = float(input("Ender side 2:"))
    height = float(input("Ender height:"))
    print(volume_pyramid(side1,side2,height,sides))
    print()
