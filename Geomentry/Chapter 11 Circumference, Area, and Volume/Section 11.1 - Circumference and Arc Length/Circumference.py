def Circumference(length,rad):
    return(f'{length*(360/(2*rad))}')
while True:
    length = int(input("Enter length:"))
    rad = int(input("Enter rad:"))
    print(Circumference(length,rad))
    print("")
