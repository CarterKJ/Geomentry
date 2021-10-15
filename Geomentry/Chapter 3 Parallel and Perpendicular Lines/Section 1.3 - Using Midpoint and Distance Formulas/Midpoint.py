import time
def midpoint(x1,y1,x2,y2):
    return(f'({x1+x2/2},{y1+y2/2})')
    
while True:
    time.sleep(1)
    xy1=float(input("x1:"))
    xy2=float(input("y1:"))
    xy3=float(input("x2:"))
    xy4=float(input("y2:"))
    print("Midpoint is",midpoint(xy1,xy2,xy3,xy4))
