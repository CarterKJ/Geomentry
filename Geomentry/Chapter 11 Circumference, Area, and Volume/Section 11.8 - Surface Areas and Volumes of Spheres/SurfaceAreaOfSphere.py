def surf_area_sphere(rad):
    return(round(4*3.14*rad**2,2))
    
while True:
    rad = float(input("Enter radius:"))
    print(surf_area_sphere(rad))
    print()
