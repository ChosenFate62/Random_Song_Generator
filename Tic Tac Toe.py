def display_board(board):
  # Remember, this only works in jupyter!
    
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


# In[2]:


test_board = [' ']*10
display_board(test_board)


# In[3]:


def player_input():
    
    choice = 'Wrong'
    playables = ["X" , "O"]
    
    while choice not in playables :
        choice = input("Player 1: Do you want to be X or O? ").upper()
        
    
    if choice == 'X':
        return ('X','O')
    else:
        return ('O','X')

        


# In[4]:


def place_marker(board, marker, position):
    board[position] = marker
       


# In[5]:


#place_marker(test_board,'$',8)
#display_board(test_board)


# In[6]:


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal




import random

def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'
    


# In[9]:


def space_check(board, position):
    
    return board[position] == ' '


# In[10]:


def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    #Board is full if tru.
    return True


# In[11]:


def player_choice(board):
    position = 0
    choices = [1,2,3,4,5,6,7,8,9]
    while position not in choices or not space_check(board,position):
        position = int(input("What position do you wish to use. 0-8 "))
            
    return position


# In[12]:


#player_choice(test_board)


# In[13]:


def replay():
    choice = 1
    while choice == 1:
        response = 'Wrong'
        choices = ['Y','N']
        while response not in choices:
            response = input("Do you want to play again. Y/N: ")
            if response not in choices:
                print("Please try again. For reference, Y means yes, and N means no. CAPSLOCKED SENSITIVE")
        if response == 'Y':
            return True
        else:
            return False


# In[14]:


#replay()


# In[ ]:





# In[ ]:


print("Welcome to Tic Tac Toe!")

while True:
    
    #Play the Game
    
    #Set Everything up (Board, WHOS FIRST, CHOOSE MARKERS X,O )
    
    the_board=[' ']*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn +' will go first')

    
    play_game = input('Ready to play?(y or n) ')
    print(play_game)
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    
    #Game play
    while game_on:
        if turn == 'Player 1':
            
            #show the board
            display_board(the_board)
            #Choose a position
            position = player_choice(the_board)
            #Place the marker on the position
            place_marker(the_board, player1_marker,position)
            #Check if they won
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Congratulations, Player 1 has won Tic Tac Toe")
                game_on = False
            
            #Or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False
                else:
                    turn = 'Player 2'

                #No tie and no win? The next player's turn
            
        else:
            
            #show the board
            display_board(the_board)
            #Choose a position
            position = player_choice(the_board)
            #Place the marker on the position
            place_marker(the_board, player2_marker,position)
            #Check if they won
            
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Congratulations, Player 2 has won Tic Tac Toe")
                game_on = False
            
            #Or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:





# In[ ]:




