def Verify_Triangle(leg,base,hyp):
    if leg**2 + base**2 == hyp **2:
        return "Right Triangle"
    elif hyp**2 < leg**2 + base **2:
        return "Acute Triangle"
    elif hyp**2 > leg**2 + base **2:
        return "Obtuse Triangle"
    else:
        return "Prossed failed"


while True:
    leg = int(input("Enter leg:"))
    base = int(input("Enter base:"))
    hyp = int(input("Enter hypotenuse:"))
    print(Verify_Triangle(leg,base,hyp))
    print("")
