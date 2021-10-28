X=[]
Y=[]
def reflect():
    global X
    global Y
    Xdiff=[]
    Ydiff=[]
    YRange = 0
    index = 0
    XRange = 0
    Xdiff.clear()
    Ydiff.clear()
    getAxis = input("Enter line with no spaces (Ex. x=9 or y=x(only y=+-x)):").lower()
    index = 0
    if getAxis == "y=x":
        for i in X:
            Xdiff.append(X[index])
            Ydiff.append(Y[index])
            index += 1
        X.clear()
        Y.clear()
        index = 0
        for i in Xdiff:
            X.append(Ydiff[index])
            Y.append(Xdiff[index])
            index += 1
        Xdiff.clear()
        Ydiff.clear()
    
    elif "x=" in getAxis:
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

def rotate():
    global X
    global Y
    Xhold=[]
    Yhold=[]
    index = 0
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
        
def trans():
    global X
    global Y
    XRange = 0
    YRange = 0
    index = 0
    UP_Displace = int(input("Enter Up:"))
    DOWN_Displace = int(input("Enter Down:"))
    RIGHT_Displace = int(input("Enter Right:"))
    LEFT_Displace = int(input("Enter Left:"))
    for item in X:
        X[XRange] += UP_Displace
        XRange +=1
    XRange = 0
    for item in X:
        X[XRange] -= DOWN_Displace
        XRange +=1
    for item in Y:
        Y[YRange] += RIGHT_Displace
        YRange+=1
    YRange = 0
     
    for item in Y:
        Y[YRange] -= LEFT_Displace
        YRange+=1
    print("""
    """)


def end_seq():
    index = 0
    for i in X:
        print(f'{index}({X[index]},{Y[index]})')
        index += 1

        
        
        
CordNum = int(input("Enter Number on Cords:"))
for i in range(CordNum):
    CordsX = int(input("Enter X:"))
    X.append(CordsX)
    CordsY = int(input("Enter Y:"))
    Y.append(CordsY)
        
while True:
    MainInput = input("Enter Mode 'done' to get cords, 'help':").lower()
    if "done" in MainInput:
        end_seq()
    elif "trans" in MainInput:
        trans()
    elif "rot" in MainInput:
        rotate()
    elif "ref" in MainInput:
        reflect()
    elif "clear" in MainInput:
        X.clear
        Y.clear
    elif "help" in MainInput:
        print("enter 'trans' to transform, 'rot' to rotate, 'ref' to reflect and 'clear' to clear cords")
    
    
