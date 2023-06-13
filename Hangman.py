import random

#Topics

topicInput = input("Choose one of these 3 topics, Food, Movie, Sports: ")

Topicset= {"Food":["chicken", "pie", "fries", "cereals", "bread", "cheese", "potato", "cookies"], "Movie":["Ted", "Bambi", "Frozen", "Hulk", "Titanic", "Twilight", "Shrek", "Cinderella", "Marvel"], "Sports":["Baseball", "Golf", "Hockey", "Bowling", "Soccer", "Football", "Cycling", "Fencing", "Skiing", "Volleyball"]}
Topic = Topicset.get(topicInput.capitalize())
if Topic is None:
    print("You have not given a valid reponse. Make sure to follow the same spelling")
    exit()


print("Once you get 7 X's, you are out")
wordBlank = []
punishment2 = []
incorrect = 0
m = 0

def wordBank(lst):
    global word
    choice = int(random.randint(-1,len(lst)-1))
    word = lst[choice]
    for a in word:
        wordBlank.append("_")

def punishment():
    global incorrect
    x=0
    punishment2.append("X")
    print(punishment2)
    incorrect += 1
    
def Game():
    global m
    
    position = 0
    correct =0
    letter = input("Choose a letter: ")
    for let in word:
        if let.upper() == letter.upper():
            wordBlank[position] = letter
            correct += 1
            m += 1
        position += 1
    if correct == 0:
        punishment()
            

wordBank(Topic)   
print(wordBlank)        
while m < len(wordBlank):
    if incorrect == 7:
        print("You have used up all your attempts. The word was {}".format(wordBank(Topic)))
        break
    else:
        Game()
        print(wordBlank)
        
if m == len(wordBlank):
    print("You have won, congrats")