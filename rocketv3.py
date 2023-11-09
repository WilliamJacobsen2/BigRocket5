
# Moffett, 11/9/2023
# rocketshipv3.py
# ASCII ART OF A ROCKET, testing loops



def TopJet():
    for i in range(1, 4):
        print('|'
            + "." * (3-i)
            + "/\\" * (i)
            + ".." * ((3-i))
            + "/\\" * (i)
            + "." * (3-i)
            + "|")
def BotJet():
    for i in range(1, 4):
        print('|'
            + "." * (i-1)
            + "\\/" * ((3-i)+1)
            + ".." * (i-1)
            + "\\/" * ((3-i)+1)
            + "." * (i-1)
            + "|")
def Bar():
        print(("+")+("=*"* (3*2))+("+"))

def Cone():
    for i in range(1, 6):
        print(
            " " * (6-i)
            + "/" * (i)
            + "**"
            + "\\" * (i))

def DBody():
    TopJet()
    BotJet()
def HBody():
    BotJet()
    TopJet()
    

#Rocket
Cone()
Bar()
DBody()
Bar()
HBody()
Bar()
Cone()
