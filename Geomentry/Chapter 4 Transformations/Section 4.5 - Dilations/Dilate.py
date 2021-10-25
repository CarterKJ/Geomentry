def scale():
    X = []
    Y = []
    XRange = 0
    YRange = 0
    index = 0
    CordNum = int(input("Enter Number on Cords:"))
    for i in range(CordNum):
        CordsX = int(input("Enter X:"))
        X.append(CordsX)
        CordsY = int(input("Enter Y:"))
        Y.append(CordsY)
    move_by = input("Enter what to scale by enter 'fract' for fractions, (Exp, x-3, x*2)").lower().strip()
    move_by = move_by.replace("x","")
    index = 0
    
    if "fract" in move_by:
        n = int(input("Enter the numerator: "))
        d = int(input("Enter the denominator: "))
        fract = n/d
        for i in X:
            X[index] *= fract
            Y[index] *= fract
            index += 1  
    elif "-" in move_by:
        move_by = move_by.replace("-","")
        move_by = int(move_by)
        for i in X:
            X[index] -= move_by
            Y[index] -= move_by
            index += 1 
    elif "+" in move_by:
        move_by = move_by.replace("+","")
        move_by = int(move_by)
        for i in X:
            X[index] += move_by
            Y[index] += move_by
            index += 1
    elif "**" in move_by:
        move_by = move_by.replace("**","")
        move_by = int(move_by)
        for i in X:
            X[index] **= move_by
            Y[index] **= move_by
            index += 1 
    elif "*" in move_by:
        move_by = move_by.replace("*","")
        move_by = int(move_by)
        for i in X:
            X[index] *= move_by
            Y[index] *= move_by
            index += 1    
    elif "/" in move_by:
        move_by = move_by.replace("/","")
        move_by = int(move_by)
        for i in X:
            X[index] /= move_by
            Y[index] /= move_by
            index += 1  
    index = 0
    for item in X:
        print(f'{index}({X[index]},{Y[index]})')
        index += 1 
while True:
    index = 0
    scale()
