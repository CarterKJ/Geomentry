def vol_sphere(rad):
    return(round((4/3)*3.14*rad**3,2))
    
while True:
    rad = float(input("Enter radius:"))
    print(vol_sphere(rad))
    print()
