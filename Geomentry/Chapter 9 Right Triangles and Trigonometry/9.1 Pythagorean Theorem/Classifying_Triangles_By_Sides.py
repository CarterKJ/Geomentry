def Verify_Triangle(leg,base,hyp):
    if leg + base < hyp:
        return "Invalid Triangle"
    elif leg**2 + base**2 == hyp **2:
        return "Right Triangle"
    elif hyp**2 < leg**2 + base **2:
        return "Acute Triangle"
    elif hyp**2 > leg**2 + base **2:
        return "Obtuse Triangle"
    else:
        return "Prossed failed"


while True:
    leg = float(input("Enter leg:"))
    base = float(input("Enter base:"))
    hyp = float(input("Enter hypotenuse:"))
    print(Verify_Triangle(leg,base,hyp))
    print("")
