import math
from fractions import Fraction
def ArcLen(deg, rad):
    return(f'{Fraction((rad*2)*(deg/360)).limit_denominator()}π or {(rad*math.pi*2)*(deg/360)}')
while True:
    deg = int(input("Enter deg:"))
    rad = int(input("Enter rad:"))
    print(ArcLen(deg,rad))
    print("")
