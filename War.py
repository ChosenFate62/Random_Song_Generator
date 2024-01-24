import random

valueOfCards = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"Jack":11,"Queen":12,"King":13,"Ace":14}
deckOfCards = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace",]
 
player1Card = random.sample(deckOfCards, 26)
player2Card = deckOfCards[:] 

for card in player1Card:
    player2Card.remove(card)
    

def War(p1,p2):
    wardeck = [player1Card[p1], player2Card[p2]]
    player1Card.pop(p1)
    player2Card.pop(p2)
    repeat = 0
    while repeat == 0:
        x=0
        d= 0
        while x < 3:
            cd = random.randint(0,len(player1Card))
            wardeck.append(player1Card[cd])
            player1Card.pop(cd)
            x += 1
            
        while d < 3:
            c = random.randint(0,len(player1Card))

            wardeck.append(player1Card[c])
            player1Card.pop(p1)
            d += 1
            
        b = random.randint(0,len(player1Card))
        b2 = random.randint(0,len(player2Card))   
        
        wardeck.append(player1Card[b])
        wardeck.append(player2Card[b2]) 
        if valueOfCards[player1Card[b]] > valueOfCards[player2Card[b2]]:
            for i in range(len(wardeck)):
                player1Card.insert(i + 0, wardeck[i])
            print("You Won")
            repeat +=1
        elif valueOfCards[player1Card[b]] < valueOfCards[player2Card[b2]]:
            for i in range(len(wardeck)):
                player2Card.insert(i + 0, wardeck[i])
            print("You lost")
            repeat += 1
        else:
            print("We go Again")
            
        
        

def Game():
    #Getting The specific card
    p1 = random.randint(0, len(player1Card)- 1) 
    p2 = random.randint(0, len(player2Card)- 1)    

    print("This is your card.")
    print(player1Card[p1])
    print("This is your opponent's card.")
    print(player2Card[p2])
    
    if valueOfCards[player1Card[p1]] > valueOfCards[player2Card[p2]]:
        player1Card.insert(0,player2Card[p2])
        print("You won")
        player2Card.pop(p2)
    elif valueOfCards[player2Card[p2]] > valueOfCards[player1Card[p1]]:
        print("You Lost")
        player2Card.insert(0,player1Card[p1])
        player1Card.pop(p1)
    elif valueOfCards[player1Card[p1]] == valueOfCards[player2Card[p2]]:
        print("Time for War")
        War(p1,p2)
        
game_on = True
while game_on == True or len(player1Card) != 52 or len(player2Card) != 52:
    User = input("Do you want to keep playing. Y/N ").capitalize()
    if User == "Y":
        Game()
    elif User == "N":
        bo = False
    

       
