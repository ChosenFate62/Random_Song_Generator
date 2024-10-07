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
wrong_attempts = []
incorrect = 0
answer = 0

def wordBank(lst):
    global word
    choice = int(random.randint(-1,len(lst)-1))
    word = lst[choice]
    for i in word:
        wordBlank.append("_")

def punishment():
    global incorrect
    wrong_attempts.append("X")
    print(wrong_attempts)
    incorrect += 1
    
def Game():
    global answer
    
    position = 0
    correct =0
    letter = input("Choose a letter: ")
    
    for char in word:
        if char.upper() == letter.upper():
            wordBlank[position] = letter
            correct += 1
            answer += 1
        position += 1
    if correct == 0:
        punishment()
            

wordBank(Topic)   
print(wordBlank)        
while answer < len(wordBlank):
    if incorrect == 7:
        print("You have used up all your attempts. The word was {}".format(word))
        break
    else:
        Game()
        print(wordBlank)
        
if answer == len(wordBlank):
    print("You have won, congrats")
