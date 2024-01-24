import tkinter as tk
import csv
import random as randint

main = tk.Tk()

movieList = {"Action":["Thor: Love and Thunder", "Spider-Man", "Into the SpiderVerse", "Ant-Man Quantamania", "Black Panther", "Black Panther 2","Iron-Man Trilogy"], "Comedy":["My Cousin Vinny","Ted","Ted 2", "Step Brothers(2008)","The Family Plan","Old Dads"],"History":["Napoleon","All Quiet on the Western Front","Operation Valkyrie","Rustin","Tetris","Sound of Freedom"]}


frontText = tk.Label(main, text = "This is Victor's Movie Recommendation\n based on categories.")
frontText.grid(column = 2, row = 1)

comedy = tk.Button(main, text = "Comedy", pady=  10, padx = 10)
comedy.grid(column = 1, row = 2)

history = tk.Button(main, text = "History", pady = 10, padx = 50)
history.grid(column = 2, row  =2, padx = 0)

action = tk.Button(main, text= "Action" , pady = 10, padx = 20, command = lambda:randomMovie("Action"))
action.grid(column = 3, row = 2)


def randomMovie(movieType):
    length = len(movieList[movieType])
    selectedList = movieList[movieType]
    randomNumber = randint.randint(0,length-1)
    
    selectedSong = selectedList[randomNumber]
    
    
    

    
    

main.mainloop()
