def reflect():
    X = []
    Y = []
    Xdiff=[]
    Ydiff=[]
    YRange = 0
    index = 0
    XRange = 0
    Xdiff.clear()
    Ydiff.clear()
    X.clear()
    Y.clear()
    CordNum = int(input("Enter Number of Cords:"))
    for i in range(CordNum):
        CordsX = int(input("Enter X:"))
        X.append(CordsX)
        CordsY = int(input("Enter Y:"))
        Y.append(CordsY)
    getAxis = input("Enter line with no spaces (Ex. x=9 or y=5):").lower()
    
    if "x=" in getAxis:
        Xnum = getAxis.replace("x=",'').replace(" ", "")
        Xnum = int(Xnum)
        index = 0
        for i in X:
            Xdiff.append(X[index]-(Xnum))
            index += 1
        X.clear()
        index = 0
        for i in Xdiff:
            X.append(Xnum - (Xdiff[index]))
            index +=1         
    elif "y=" in getAxis:
        Ynum = getAxis.replace("y=",'').replace(" ", "")
        Ynum = int(Ynum)
        index = 0
        for i in Y:
            Ydiff.append(Y[index]-(Ynum))
            index += 1
        Y.clear()
        index = 0
        for i in Ydiff:
            Y.append(Ynum - (Ydiff[index]))
            index +=1
    else:
        print("Please enter something like (x=3 or y=3)")
   
    index = 0
    for i in X:
        print(f'{index}({X[index]},{Y[index]})')
        index += 1
while True:
    reflect()
