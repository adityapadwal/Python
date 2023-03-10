#Tic Tac Toe practical 

def draw_board(board):
    row_1="{}|{}|{}".format(board[0],board[1],board[2])
    row_2="{}|{}|{}".format(board[3],board[4],board[5])
    row_3="{}|{}|{}".format(board[6],board[7],board[8])
    print(row_1+"\n"+row_2+"\n"+row_3)
    
def user_move(board, user_type):
    user_choice=int(input("Player 1: Choose your Space between 1 to 9: ")) - 1
    if (board[user_choice] != " "):
        print("Space is already taken! Please try again!")
        user_move(board,user_type)
    else:
        board[user_choice]=user_type
        available_spaces.remove(user_choice)

def comp_move(board,user_type):
    # 1. Computer finds available spaces
    # 2. Computer chooses one of these at random
    # 3. Computer changes the board space with user_type(X or O)
    computer_choice = random.choice(available_spaces)
    board[computer_choice]=user_type
    available_spaces.remove(computer_choice)
    
def check_win(board, x_o):
    if(
        board[0]==x_o and board[1]==x_o and board[2]==x_o
        or
        board[3]==x_o and board[4]==x_o and board[5]==x_o
        or
        board[6]==x_o and board[7]==x_o and board[8]==x_o
        or
        board[0]==x_o and board[3]==x_o and board[6]==x_o
        or
        board[1]==x_o and board[4]==x_o and board[7]==x_o
        or
        board[2]==x_o and board[5]==x_o and board[8]==x_o
        or
        board[0]==x_o and board[4]==x_o and board[8]==x_o
        or
        board[2]==x_o and board[4]==x_o and board[6]==x_o
        ):
        play=False
        print("Yo! {},has won the game!!!".format(x_o))
    else:
        play=True 
    return play
    
#<--------Main-------->
import random
board = [" "] * 9
available_spaces = [0,1,2,3,4,5,6,7,8]
play=True
comp_or_friend=input("Whom would you like to play against? \nA friend or The Computer? \n(Enter c ro f)")
while play==True:
    print("1st Player's Turn!")
    user_move(board,"X")
    draw_board(board)
    play=check_win(board,"X")
    if(play==False):
        continue
    if (comp_or_friend == "f"):
        print("Second Player's Turn!")
        user_move(board,"O")
    elif (comp_or_friend == "c"):
        comp_move(board,"O")
    draw_board(board)
    play=check_win(board,"O")
    
    
print("\n\nEnd OF Game!")
print("Congratulatuons to the winner!")
print("Hard Luck to the Looser!")
    
    
    
    
    
    
    
    
    
    
