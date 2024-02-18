# PROGRAMME to print out different types of boxes
# TENDAI KEITH NYEVEDZANAI
# 10 MARCH 2022
# NYVTEN001

def print_square():    
    i = "* "*5       
    for j in range(3):
        j = "*       *"
        return i + "\n" + j +"\n"+ j+"\n" + j + "\n" + i# print each code in a different line to form a square
def print_rectangle(width,height):
   
    for k in range(height):
        for l in range(width):
            if k == 0 or k == height - 1 or l == 0 or l == width - 1:
                print("*",end=" ")# allows the shape to have valid spacing points
            else:
                print(" ",end=" ")# if our iintial condition does not saticify we print empty spaces
        print() # allows to print our stars in a vertical and horizontal  asymetry 
        
def get_rectangle(width, height):
    figure = ""
    for c in range(height):        
        for m in range(width):
            if c == 0 or c == height - 1 or m == 0 or m == width - 1:# our width has to subtracted since aour major print point is vertical
                figure = figure + "* "
            else:
                figure = figure + "  "
        figure = figure + "\n"
        
    return figure