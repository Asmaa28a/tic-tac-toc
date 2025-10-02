from tkinter import *
import random


def next_turn(row,col):
    global player
    if game_btns[row][col]["text"] == " " and check_winner() == False:
        if player == players[0]:
            game_btns[row][col]["text"] = player
            if check_winner() == False:
                player = players[1]
                Label.config(text=(player[1] + " turn"))
            elif check_winner() == True:
                Label.config(text=(players[0] + " wins"))
            elif check_winner() == "Tie":
                Label.config(text="Tie, no one wins")
    
    if player == players[1]:
            game_btns[row][col]["text"] = player
            if check_winner() == False:
                player = players[0]
                Label.config(text=(player[0] + " turn"))
            elif check_winner() == True:
                Label.config(text=(players[1] + " wins"))
            elif check_winner() == "Tie":
                Label.config(text="Tie, no one wins")  
                          
                     

def check_winner():
    # check all 3 horizontal rows
    for row in range(3):
        if game_btns[row][0]["text"] == game_btns[row][1]["text"] == game_btns[row][2]["text"] != " ":
            game_btns[row][0].config(bg="green")
            return True
        
    # check all 3 vertical conditions
    for col in range(3):
        if game_btns[0][col]["text"] == game_btns[1][col]["text"] == game_btns[2][col]["text"] != " ":
            game_btns[0][col].config(bg="green")
            game_btns[1][col].config(bg="green")
            game_btns[2][col].config(bg="green")
            return True 
        
    # check 2 diagonals
    if game_btns[0][0]["text"] == game_btns[1][1]["text"] == game_btns[2][2]["text"] != " ":
                game_btns[0][0].config(bg="green")
                game_btns[1][1].config(bg="green")
                game_btns[2][2].config(bg="green")
                return True
    elif game_btns[0][2]["text"] == game_btns[1][1]["text"] == game_btns[2][0]["text"] != " ":
        return True
    
    #if there are no emty spaces left
    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg="red")
        return "Tie"
    else:
     return False            
        
        
    

def check_empty_spaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]["text"] != " ":
                spaces -= 1
                
    if spaces == 0:
        return False
    else:
        return True
                

def start_new_game():
    global player
    player = random.choice(players)
    
    Label.config(text=(player + " turn"))
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text=" ", bg="#F0F0F0")


window=Tk()
window.title("Tic Tac Toe")


players = ["X","O"]
player = random.choice(players) 

game_btns =[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

Label = Label(text=(player + " turn"), font=('arial', 20, 'bold'))
Label.pack(side=TOP)


restart_btn = Button(text="Restart", font=('arial', 20, 'bold'), 
                     command=start_new_game)

restart_btn.pack(side=TOP)

btns_frame = Frame(window)
btns_frame.pack()

for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btns_frame, text=" ", 
                                     font=('arial', 20, 'bold'),
                                     width=5, height=2,
                                     command=lambda row=row, col=col: next_turn(row, col))
        game_btns[row][col].grid(row=row, column=col)
    






window.mainloop()
