import time
def trans():
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
trans()
