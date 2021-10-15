import time
def PDS(x,y,x2,y2,n,m):
    PointX = (m*x2+n*x)/(n+m)
    PointY = (m*y2+n*y)/(n+m)
    return(f'Point is ({PointX},{PointY})')
    
while True:
    time.sleep(1)
    xy1=float(input("x1:"))
    xy2=float(input("y1:"))
    xy3=float(input("x2:"))
    xy4=float(input("y2:"))
    m1 = float(input("Enter M (M:N):"))
    n1 = float(input("Enter N (M:N):"))
    print(PDS(xy1,xy2,xy3,xy4,n1,m1))

