from cgitb import reset
import random as randint
import tkinter as tk
from tkinter import *
from functools import partial
import urllib.request
import re

 
 


#Function
def DestroyButton():
    main.destroy()
 
        
def AddFunction(Song):
    
    Song1 = (Song.get())
    
    
    #global Song_list
    Song_list.append(Song1)

    #This for loops allowes me to check strings to make sure that there are no 'empty' strings
    for song in Song_list:
        #This removes repeats 
        if song == " " or song == '':
            Song_list.remove(song)
        
    
    Song_listvar = tk.StringVar(value = Song_list)
    
    #Inserts my list into a listbox.
    ListBox = tk.Listbox(main, listvariable = Song_listvar, width = "20", font = "40").grid(column = 1, row = 8)
    
    #SongEntry.delete(0, END)
    
    

            
def RandomizeScreen(Finished_list):
    def ClearResponse():
        Rand.destroy()
    
    #NOS stands for Name of Song
    #This function is going to search up the song on youtube then print it out
        
    #Creating new screen
    Rand = tk.Tk()
    Rand.geometry("900x175")
    Rand.title("Randomize")

    #Randomizing the list
    len_Finished_list = len(Finished_list)

    OutputSongNum = randint.randint(0, len_Finished_list - 1) 
    
    SongOutput = Finished_list[OutputSongNum] 
    
    WebsiteSearch = str(SongOutput).replace(" ", "+")
      
    #Line 65-68 borrowed from https://codefather.tech/blog/youtube-search-python/
    websitestart = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + WebsiteSearch)
    video_link = re.findall(r"watch\?v=(\S{11})", websitestart.read().decode())
    
    SongWebsite = "https://www.youtube.com/watch?v=" + video_link[0]
    print("https://www.youtube.com/watch?v=" + video_link[0])
    
    WebsiteSong = "The Youtube URL of the Song is " + SongWebsite
    OutputSong = "The Song you should start with is, " + SongOutput

    
    #Creating Labels and Buttons
    FinalLabel = tk.Label(Rand, text = OutputSong,font = '40').pack(pady = 10)
    
    WebsiteLink = tk.Label(Rand, text = WebsiteSong, font = '40').pack(pady = 5)

    Deletebutton = tk.Button(Rand, text = "Exit", command = ClearResponse).pack(pady = 20)

    Rand.mainloop()

#Using tkdocs.com/tutorial/index.html
    
     
#Creating the screen
main = tk.Tk()
main.geometry("350x500")
main.title("Random Starter Song")

        
        

Song_list = []
Song_list_repetition_checker = []
SongWebsite = ''

SongName = tk.Variable()

RandomizeButton = partial(RandomizeScreen, Song_list)
FinalButton = tk.Button(main, text = "Randomize", command = RandomizeButton).grid(column = 1, row = 5)
    

#Creating the Label
Title = tk.Label(main, text = "Best First Song Randomizer", font = "ComicSans, 20", fg = "Brown").grid(column = 1, row = 1)

Song = tk.Label(main, text = "Song", font = "15").grid(column = 1, row =2)

SongEntry = tk.Entry(main, textvariable = SongName, bd = 4, font = "40").grid(column = 1, row = 3)

AddFunction =  partial(AddFunction, SongName) 
AddButton = tk.Button(main, text = "Add", command = AddFunction).grid(column = 1, row = 4)


Deletebutton = tk.Button(main, text = "Exit", command = DestroyButton).grid(column = 1, row = 6)

main.mainloop()