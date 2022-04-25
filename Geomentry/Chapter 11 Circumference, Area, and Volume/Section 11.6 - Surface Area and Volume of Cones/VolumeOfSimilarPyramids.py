from fractions import Fraction

def volume_similar_pyramid(height1,height2, vol=0):
    if vol == "0":
        return(f'{height1**3}:{height2**3}')
    # else:
    #     vol = vol.split(" ")
    #     if vol[1] == "2":
    #         fraction = str(Fraction(height1**3,height2**3)).split("/")
    #         return(float(volume[0])/float(fraction[1]))
    #     else:
    #         fraction = str(Fraction(height1**3,height2**3)).split("/")
    #         return(float(fraction[1])/float(volume[0]))
            
    
while True:
    height1 = float(input("Enter Height 1:"))
    height2 = float(input("Enter Height 2:"))
    # volume = input("Enter volume (0 if none, (space 1 or 2 on trig)):")
    try:
        print(volume_similar_pyramid(int(height1), int(height2)))
    except:
        print(volume_similar_pyramid(height1, height2))
    print()
