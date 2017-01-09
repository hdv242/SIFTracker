'''
Created on Jan 6, 2017

@author: Bin
'''

from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import PhotoImage
from tkinter import Tk
from tkinter import messagebox
import matches

entries = []
songs = {'Sunny Day Song': 0}

## clears out entry boxes
def clearEntries() :
    for e in entries :
        e.delete(0, 'end')

## writes submitted information into file
def writeToFile():
    with open("score_match_stats.txt", 'a') as file :
        for e in entries :
            file.write(e.get() + " ")
        file.write("\n")
    file.close()
    clearEntries()

## verifies the inputed song is a real song
def verifySong() :
    return

## facilitates input of information
def inputAnswer() :
    # check for missing fields
    emptyFields = 0
    for e in entries :
        if (e.get() == "") :
            emptyFields += 1
    if (emptyFields > 0) :
        messagebox.showinfo("Failed!", "Missing field(s)")
        return
            
    writeToFile()
    messagebox.showinfo("Success!", "Info submitted")

if __name__ == "__main__"  :
    gui = Tk()
    gui.title("SIF Score Match Tracker")
    gui.geometry("524x333")
    
    # background image
    bgImage = PhotoImage(file = "const-maki.png")
    backgroundLabel = Label(gui, image = bgImage)
    backgroundLabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    # song name input field
    songName = ""
    songX = 100
    songY = 200
    songLabel = Label(gui, text = "Song")
    songLabel.place(x = songX - 33, y = songY)
    songEntry = Entry(gui, textvariable = songName, width = 30)
    songEntry.place(x = songX, y = songY)
    entries.append(songEntry)
    
    # score input field
    score = ""
    scoreX = songX + 250
    scoreY = songY
    scoreLabel = Label(gui, text = "Score")
    scoreLabel.place(x = scoreX - 35, y = scoreY)
    scoreEntry = Entry(gui, textvariable = score, width = 10)
    scoreEntry.place(x = scoreX, y = scoreY)
    entries.append(scoreEntry) 
    
    # combo input field
    combo = ""
    comboX = songX
    comboY = songY + 30
    comboLabel = Label(gui, text = "Combo")
    comboLabel.place(x = comboX - 45, y = comboY)
    comboEntry = Entry(gui, textvariable = combo, width = 10)
    comboEntry.place(x = comboX, y = comboY)
    entries.append(comboEntry)
    
    # rank input field
    rank = ""
    rankX = songX + 250
    rankY = comboY
    rankLabel = Label(gui, text = "Rank")
    rankLabel.place(x = scoreX - 33, y = rankY)
    rankEntry = Entry(gui, textvariable = rank, width = 10)
    rankEntry.place(x = rankX, y = rankY)
    entries.append(rankEntry)
        
    # submit, clear, cancel buttons
    buttonX = 170
    buttonY = 270
    submitButton = Button(gui, text = "Submit", cursor = "heart", 
                                  command = inputAnswer)
    submitButton.place(x = buttonX, y = buttonY)
    clearButton = Button(gui, text = "Clear", cursor = "heart",
                                  command = clearEntries)
    clearButton.place(x = buttonX + 70, y = buttonY)
    cancelButton = Button(gui, text = "Cancel", cursor = "heart",
                                  command = gui.quit)
    cancelButton.place(x = buttonX + 130, y = buttonY)
    
    gui.mainloop()
    