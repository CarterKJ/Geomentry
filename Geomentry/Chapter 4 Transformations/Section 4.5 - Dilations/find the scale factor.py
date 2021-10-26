def find_scale():
    x = int(input("Enter x1 (base graph):"))
    y = int(input("Enter y1 (base graph):"))
    x2 = int(input("Enter x2:"))
    y2 = int(input("Enter y2:"))
    scale_factor_X = x2/x
    scale_factor_Y = y2/y
    
    if scale_factor_X == 0:
        print("The scale is", round(scale_factor_Y,3))
    else:    
        print("The scale is", round(scale_factor_X,3))

while True:
    find_scale()
