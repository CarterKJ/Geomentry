import math, time
def distance(x1,y1,x2,y2):
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2),1)

while True:
    time.sleep(1)
    xy1=float(input("x1:"))
    xy2=float(input("y1:"))
    xy3=float(input("x2:"))
    xy4=float(input("y2:"))
    print("Distance is",distance(xy1,xy2,xy3,xy4))
