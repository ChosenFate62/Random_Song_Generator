import random

valueOfCards = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"Jack":11,"Queen":12,"King":13,"Ace":14}
deckOfCards = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"] * 4

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
            warCards = random.randint(0,len(player1Card)-1)
            wardeck.append(player1Card[warCards])
            player1Card.pop(warCards)
            x += 1
            
        while d < 3:
            aiWarCards = random.randint(0,len(player1Card)-1)

            wardeck.append(player1Card[aiWarCards])
            player1Card.pop(p1)
            d += 1
            
        warCard = random.randint(0,len(player1Card))
        aiWarCard = random.randint(0,len(player2Card))   
        
        wardeck.append(player1Card[warCard])
        wardeck.append(player2Card[aiWarCard]) 
        print("This is your new card.")
        print(player1Card[warCard])
        print("This is your opponent's new card.")
        print(player2Card[aiWarCard])
        if valueOfCards[player1Card[warCard]] > valueOfCards[player2Card[aiWarCard]]:
            for i in range(len(wardeck)):
                player1Card.insert(i + 0, wardeck[i])
            print("You Won")
            repeat +=1
        elif valueOfCards[player1Card[warCard]] < valueOfCards[player2Card[aiWarCard]]:
            for i in range(len(wardeck)):
                player2Card.insert(i + 0, wardeck[i])
            print("You lost")
            repeat += 1
        else:
            print("We go Again")
        
            
        
        

def Game():
    #Getting The specific card
    topCard = random.randint(0, len(player1Card)- 1) 
    aiTopCard = random.randint(0, len(player2Card)- 1)    

    print("This is your card.")
    print(player1Card[topCard])
    print("This is your opponent's card.")
    print(player2Card[aiTopCard])
    
    if valueOfCards[player1Card[topCard]] > valueOfCards[player2Card[aiTopCard]]:
        player1Card.insert(0,player2Card[aiTopCard])
        print("You won")
        player2Card.pop(aiTopCard)
    elif valueOfCards[player2Card[aiTopCard]] > valueOfCards[player1Card[topCard]]:
        print("You Lost")
        player2Card.insert(0,player1Card[topCard])
        player1Card.pop(topCard)
    elif valueOfCards[player1Card[topCard]] == valueOfCards[player2Card[aiTopCard]]:
        print("Time for War")
        War(topCard,aiTopCard)
    print("You have {} cards remaining".format(len(player1Card)))
start = True
while start == True or len(player1Card) != 52 or len(player2Card) != 52:
    User = input("Do you want to keep playing. Y/N ").capitalize()
    if User == "Y":
        Game()
    elif User == "N":
        exit()
    

       
