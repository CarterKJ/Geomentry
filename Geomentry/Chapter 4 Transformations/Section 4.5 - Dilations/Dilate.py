def scale():
    X = []
    Y = []
    XRange = 0
    YRange = 0
    index = 0
    CordNum = int(input("Enter Number on Cords:"))
    for i in range(CordNum):
        CordsX = float(input("Enter X:"))
        X.append(CordsX)
        CordsY = float(input("Enter Y:"))
        Y.append(CordsY)
    move_by = input("Enter what to scale by enter 'fract' for fractions (put ** for power, or / for div):").lower().strip()
    index = 0
    
    if "fract" in move_by:
        n = float(input("Enter the numerator: "))
        d = float(input("Enter the denominator: "))
        fract = n/d
        for i in X:
            X[index] *= fract
            Y[index] *= fract
            index += 1 
    elif "**" in move_by:
        move_by = move_by.replace("**","")
        move_by = float(move_by)
        for i in X:
            X[index] **= move_by
            Y[index] **= move_by
            index += 1    
    elif "/" in move_by:
        move_by = move_by.replace("/","")
        move_by = float(move_by)
        for i in X:
            X[index] /= move_by
            Y[index] /= move_by
            index += 1  
    else:
        move_by = float(move_by)
        for i in X:
            X[index] *= move_by
            Y[index] *= move_by
            index += 1 
    index = 0
    for item in X:
        print(f'{index}({X[index]},{Y[index]})')
        index += 1 
while True:
    index = 0
    scale()
