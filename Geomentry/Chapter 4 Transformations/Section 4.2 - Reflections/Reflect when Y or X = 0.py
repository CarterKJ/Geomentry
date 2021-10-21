def reflect():
    X = []
    Y = []
    YRange = 0
    index = 0
    XRange = 0
    CordNum = int(input("Enter Number of Cords:"))
    for i in range(CordNum):
        CordsX = int(input("Enter X:"))
        X.append(CordsX)
        CordsY = int(input("Enter Y:"))
        Y.append(CordsY)
    mirrorAxis = input("Enter Reflection Axis:").lower()
    if mirrorAxis == "x":
        for item in Y:
            Y[YRange] *= -1
            YRange += 1
        YRange = 0
            
    elif mirrorAxis == "y":
        for item in X:
            X[XRange] *= -1
            XRange += 1
        XRange = 0
    else:
        print("please enter 'x' or 'y'")
        
    for item in X:
        print(f'{index}({X[index]},{Y[index]})')
        index += 1
reflect()
