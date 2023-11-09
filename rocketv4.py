
# Moffett, 11/9/2023
# rocketv4.py
# ASCII ART OF A ROCKET, testing loops

size=3
#size cannot = numbers that lead to text wrapping around the screen (for me its high 40's)

def TopJet():
    for i in range(1, size+1):
        print('|'
            + "." * (size-i)
            + "/\\" * (i)
            + ".." * ((size-i))
            + "/\\" * (i)
            + "." * (size-i)
            + "|")
def BotJet():
    for i in range(1, size+1):
        print('|'
            + "." * (i-1)
            + "\\/" * ((size-i)+1)
            + ".." * (i-1)
            + "\\/" * ((size-i)+1)
            + "." * (i-1)
            + "|")
def Bar():
        print(("+")+("=*"* (size*2))+("+"))
#jetfuel issue fixed 
def Cone():
    for i in range(1, (size*2)+1):
        print(
            " " * ((size*2)-i)
            + "/" * (i)
            + "**"
            + "\\" * (i))

def DBody():
    TopJet()
    BotJet()
def HBody():
    BotJet()
    TopJet()
    

#code
Cone()
Bar()
DBody()
Bar()
HBody()
Bar()
Cone()
