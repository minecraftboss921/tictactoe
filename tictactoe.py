from Tkinter import *

gui = Tk()
gui.title("tictactoe")
label = Label(gui,text="hello")
label.grid()

playerX=True
playerO=False

def alternatePlayer(player):
    #player x is true
    global playerX
    global playerO
    if player["text"]=="" and playerX==True:
        player["text"]="X"
        #change turn
        playerX=False
        playerO=True

    #Else player O is true
    elif player["text"]=="" and playerO==True:
        player["text"] = "O"

        playerX=True
        playerO=False
        #change back to X turn



# Main Function
def game(player):
    alternatePlayer(player)
    winner()


def winner():
    #logic of win for X
    if (b["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" or
        b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" or
        b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" or
        b["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or
        b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" or
        b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or
        b["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" or
        b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X"):
        print "Player X wins! :)"
        display["text"]="X Wins"

    elif (b["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" or
            b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" or
            b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" or
            b["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" or
            b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O" or
            b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" or
            b["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" or
            b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O"):
            print "Player O wins! :)"
            display["text"] = "O Wins"

    elif(b["text"] != "" and b2["text"] != "" and b3["text"] != "" and
            b4["text"] != "" and b5["text"] != "" and b6["text"] != "" and
            b7["text"]!= "" and b8["text"] != "" and b9["text"] != "" ):
            print "Draw"
            display["text"]="Draw"




b = Button(gui, text= '',width=23,height=12, command= lambda:game(b) )
b.grid(row=0,column=0)

b2 = Button(gui, text= '', width=23,height=12,command= lambda:game(b2) )
b2.grid(row=0,column=1)

b3 = Button(gui, text= '',width=23,height=12, command= lambda:game(b3) )
b3.grid(row=0,column=2)

b4 = Button(gui, text= '',width=23,height=12, command= lambda:game(b4) )
b4.grid(row=1,column=0)

b5 = Button(gui, text= '', width=23,height=12,command= lambda:game(b5) )
b5.grid(row=1,column=1)


b6 = Button(gui, text= '', width=23,height=12,command= lambda:game(b6) )
b6.grid(row=1,column=2)


b7 = Button(gui, text= '', width=23,height=12,command= lambda:game(b7) )
b7.grid(row=2,column=0)


b8 = Button(gui, text= '', width=23,height=12,command= lambda:game(b8) )
b8.grid(row= 2,column= 1)


b9 = Button(gui, text= '', width=23,height=12,command= lambda:game(b9) )
b9.grid(row=2,column=2)

display=Label(gui,text="Who Wins?")
display.grid(row=0,column=3)


gui.mainloop()


