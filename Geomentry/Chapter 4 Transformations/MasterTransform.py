#A combanation of most of the transform scripts
import time
X = []
Y = []
def trans():
    XRange = 0
    YRange = 0
    index = 0
    CordNum = int(input("Enter Number on Cords:"))
    for i in range(CordNum):
        CordsX = int(input("Enter X:"))
        X.append(CordsX)
        CordsY = int(input("Enter Y:"))
        Y.append(CordsY)
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
    for item in X:
        print(f'{index}({X[index]},{Y[index]})')
        index += 1   
        
def transDif():
    x1 = int(input("Enter X1:"))
    y1 = int(input("Enter y1:"))
    x2 = int(input("Enter X2:"))
    y2 = int(input("Enter y2:"))
    print(f'X = {x2 - x1} Y = {y2 - y1}')
    
    
def reflect():
    YRange = 0
    index = 0
    XRange = 0
    CordNum = int(input("Enter Number on Cords:"))
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
    
        
while True:
    X = []
    Y = []
    print()
    mode1 = input("Enter Mode:").lower()
    if 'point' in mode1:
        trans()
    elif 'img' in mode1:
        transDif()
    elif 'reflect' in mode1:
        reflect()
    elif 'ref' in mode1:
        reflect()
    else:
        print("Enter 'point' or 'img'")
    time.sleep(2)
