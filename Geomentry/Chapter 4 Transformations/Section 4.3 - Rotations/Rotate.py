def rotate():
    X = []
    Y = []
    Xhold=[]
    Yhold=[]
    index = 0
    CordNum = int(input("Enter Number of Cords:"))
    for i in range(CordNum):
        CordsX = int(input("Enter X:"))
        X.append(CordsX)
        CordsY = int(input("Enter Y:"))
        Y.append(CordsY)
    Direction = input("Enter C or CC:").lower()
    if Direction == "c":
        deg = input("Enter Rotation ('90','180','270')").lower()
        if deg == "90":
            for i in X:
                X[index] *= -1
                Xhold.append(X[index])
                index+=1
            X.clear()
            index = 0
            for i in Y:
                Yhold.append(Y[index])
                index += 1
            Y.clear()
            index = 0
            for i in Yhold:
                X.append(Yhold[index])
                Y.append(Xhold[index])
                index += 1
            Xhold.clear()
            Yhold.clear()
            index = 0
        if deg == "180":
            for i in X:
                X[index] *= -1 
                Y[index] *= -1
                index += 1 
        index = 0 
        
        if deg == "270":
            for i in X:
                Xhold.append(X[index])
                index+=1
            X.clear()
            index = 0
            for i in Y:
                Y[index] *= -1
                Yhold.append(Y[index])
                index += 1
            Y.clear()
            index = 0
            for i in Yhold:
                X.append(Yhold[index])
                Y.append(Xhold[index])
                index += 1
            Xhold.clear()
            Yhold.clear()
            index += 0
                
            
    elif Direction == "cc":
        deg = input("Enter Rotation ('90','180','270')").lower()
        index = 0
        if deg == "270":
            for i in X:
                X[index] *= -1
                Xhold.append(X[index])
                index+=1
            X.clear()
            index = 0
            for i in Y:
                Yhold.append(Y[index])
                index += 1
            Y.clear()
            index = 0
            for i in Yhold:
                X.append(Yhold[index])
                Y.append(Xhold[index])
                index += 1
            Xhold.clear()
            Yhold.clear()
            index = 0
        
        if deg == "90":
            for i in X:
                Xhold.append(X[index])
                index+=1
            X.clear()
            index = 0
            for i in Y:
                Y[index] *= -1
                Yhold.append(Y[index])
                index += 1
            Y.clear()
            index = 0
            for i in Yhold:
                X.append(Yhold[index])
                Y.append(Xhold[index])
                index += 1
            Xhold.clear()
            Yhold.clear()
            index += 0
        if deg == "180":
            for i in X:
                X[index] *= -1 
                Y[index] *= -1
                index += 1 
            index = 0
        
    else:
        print("Enter 'c' or 'cc'")
    index = 0    
    for item in X:
        print(f'{index}({X[index]},{Y[index]})')
        index += 1
while True:      
    rotate()
