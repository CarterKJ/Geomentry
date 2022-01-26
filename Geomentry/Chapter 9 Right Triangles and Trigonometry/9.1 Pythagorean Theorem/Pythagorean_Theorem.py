import math
def Pythagorean_theorem(leg,base,hyp):
    if hyp == 0:
        return(f"Missing side is {round(math.sqrt(leg**2+base**2),1)}")
    if leg == 0 or base == 0:
        if leg == 0 and base == 0:
            return "Invalid Triangle"
        if leg == 0:
            return (f"Missing side is {round(math.sqrt((hyp**2)-(base**2)),1)}")
        else:
            return (f"Missing side is {round(math.sqrt((hyp**2)-(leg**2)),1)}")
    
print("Enter Triangle Sides; Enter 0 if blank")

while True:
    leg = float(input("Enter leg:"))
    base = float(input("Enter base:"))
    hyp = float(input("Enter hypotenuse:"))
    print(Pythagorean_theorem(leg,base,hyp))
    print("")
