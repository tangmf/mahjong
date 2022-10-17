from tkinter import *
from tkinter import ttk

allList = []
side = 1
sideRound = 1

# Classes

class Player:
    def __init__(self, index, name, score):
        self.index = index
        self.name = name
        self.score = score
    def __str__(self):
        return f"{self.index}:{self.name}({self.score})"

# Raw func

def Write(file, text):
    f = open(file, "w")
    f.write(text)
    f.close()

def Read(file):
    f = open(file, "r")
    print(f.read())
    return(f.read())

# Func

def SaveScore(player):
    Write( (str(player.index) + ".txt"), player.name + ": " + str(player.score))

def AddScore(player, amt):
    amt = int(amt)
    player.score += amt
    print(player)
    SaveScore(player)

def SubtractScore(player, amt):
    amt = int(amt)
    player.score -= amt
    # Uncomment if score not supposed to go below 0
    '''
    if(player.score <= 0):
        player.score = 0
    '''
    print(player)
    SaveScore(player)

def Zimo(playerIndex, amt):
    player = GetPlayer(playerIndex)
    NewLine()
    print("Zimo (" + player.name + ")")
    amt = int(amt)
    addAmt = 0
    # Subtract the rest
    Line()
    print("Subtracted (" + str(amt) + " each)")
    Line()
    for p in allList:
        if(p.index != player.index):
            SubtractScore(p, amt)
            addAmt += amt

    # Add accumulated for this player
    Line()
    print("Added (" + str(addAmt) + ")")
    Line()
    AddScore(player,addAmt)

def Shoot(playerIndex, amt):
    player = GetPlayer(playerIndex)
    NewLine()
    amt = int(amt)
    print("Shoot (" + player.name + ")")
    Line()
    print("Added (" + str(amt) + ")")
    Line()
    AddScore(player, amt)

def ShowScores():
    NewLine()
    Line()
    print("Scoreboard")
    Line()
    for p in allList:
        print(p)

def NewLine():
    print("\n")

def Line():
    print("------------------------")
    
def GetPlayer(playerIndex):
    for p in allList:
        if(p.index == playerIndex):
            return p
    return ''

def NextRound():
    global side
    global sideRound
    if(sideRound == 1):
        sideRound = 4
    else:
        sideRound-=1
        if(sideRound == 1):
            if(side == 4):
                side = 1
            else:
                side+=1

    SaveRound()

def PrevRound():
    global side
    global sideRound
    if(sideRound == 4):
        sideRound = 1
    else:
        sideRound+=1
        if(sideRound == 2):
            if(side == 1):
                side = 4
            else:
                side-=1
    SaveRound()

def ResetRound():
    global side
    global sideRound
    side = 1
    sideRound = 1
            

    SaveRound()

def SaveRound():

    
    Write("sideRound.txt", str(sideRound))
    strSide = ''
    
    if(side==1):
        strSide = 'dong'
    elif(side==2):
        strSide = 'nan'
    elif(side==3):
        strSide = 'xi'
    elif(side==4):
        strSide = 'bei'

    Write("side.txt", strSide)
    NewLine()
    Line()
    print("Round: " + str(strSide) + " / " + str(sideRound))
    Line()

    
    

    


# Player initialization

p1 = Player(1, "Player1", 0)
allList.append(p1)
p2 = Player(2, "Player2", 0)
allList.append(p2)
p3 = Player(3, "Player3", 0)
allList.append(p3)
p4 = Player(4, "Player4", 0)
allList.append(p4)

for p in allList:
    SaveScore(p)

# Initialization
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

# Main int

ttk.Label(frm, text="Menu").grid(column=0, row=0)
ttk.Button(frm, text="Show Score", command= lambda: ShowScores()).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)

v1 = StringVar()
ttk.Entry(frm,textvariable=v1).grid(column=3, row=0)

# Player 1 int
for p in allList:
    ttk.Label(frm, text= p.name).grid(column=0, row=p.index)
    ttk.Button(frm, text="Shoot", command= lambda p=p: Shoot(p.index,v1.get())).grid(column=1, row=p.index)
    ttk.Button(frm, text="Zimo", command= lambda p=p: Zimo(p.index,v1.get())).grid(column=2, row=p.index)
'''
ttk.Label(frm, text="Player1").grid(column=0, row=1)
ttk.Button(frm, text="Shoot", command= lambda: Shoot(p1,v1.get())).grid(column=1, row=1)
ttk.Button(frm, text="Zimo", command= lambda: Zimo(p1,v1.get())).grid(column=2, row=1)
'''
ttk.Button(frm, text="Prev", command= lambda : PrevRound()).grid(column=0, row=5)
ttk.Button(frm, text="Reset", command= lambda : ResetRound()).grid(column=1, row=5)
ttk.Button(frm, text="Next", command= lambda : NextRound()).grid(column=2, row=5)



# Mainloop
root.mainloop()
