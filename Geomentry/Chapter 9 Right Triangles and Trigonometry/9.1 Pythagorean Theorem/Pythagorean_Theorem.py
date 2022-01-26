import math
def Pythagorean_theorem(leg,base,hyp):
    if hyp == 0:
        return(f"Missing side is {math.sqrt(leg**2+base**2)}")
    if leg == 0 or base == 0:
        if leg == 0 and base == 0:
            return "Invalid Triangle"
        if leg == 0:
            return (f"Missing side is {math.sqrt((hyp**2)-(base**2))}")
        else:
            return (f"Missing side is {math.sqrt((hyp**2)-(leg**2))}")
    
print("Enter Triangle Sides; Enter 0 if blank")

while True:
    leg = int(input("Enter leg:"))
    base = int(input("Enter base:"))
    hyp = int(input("Enter hypotenuse:"))
    print(Pythagorean_theorem(leg,base,hyp))
    print("")
