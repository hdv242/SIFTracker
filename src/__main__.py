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
from matches import Song

songName_i = 0  # index of song name in entries
score_i = 1     # index of score in entries
combo_i = 2     # index of combo in entries
gui = Tk()      # creates the gui
entries = []    # songName, score, combo, and rank
songsList = {}  # songs will be eager cached as name : object


## writes submitted information into file
def writeToFile():
    with open("song_stats.txt", 'w') as file :
        for key in songsList.keys() :
            songsList[key].write(file)
            file.write("\n")
    
    #with open("score_match_stats.txt", 'a') as file :
    #    for e in entries :
    #        file.write(e.get() + " ")
    #    file.write("\n")
    file.close()


## exits app
def exitApp() :
    writeToFile()
    gui.quit()
    
    
## clears out entry boxes
def clearEntries() :
    for e in entries :
        e.delete(0, 'end')


## facilitates input of information
def inputAnswer() :
    # check for missing fields
    emptyFields = 0
    for e in entries :
        if (e.get() == "") :
            emptyFields += 1
    if (emptyFields > 0) :
        messagebox.showerror("Failed!", "Missing field(s)")
        return
    
    # check for incorrect song name
    name = entries[songName_i].get().lower() + " "
    if (songsList.get(name) == None) :
        messagebox.showerror("Failed!", "Cannot find song")
        return
    
    # update song info
    songsList.get(name).play(entries[score_i].get(), entries[combo_i].get())
    clearEntries()
    messagebox.showinfo("Success!", "Info submitted")


## add songs from file
def addSongs() :
    with open("song_stats.txt") as file :
        for line in file :
            # parse from file, fix name, create new Song and add it to songsList
            curSong = line.split();
            curName = curSong[songName_i].split('_')
            tempName = ""
            for part in curName :
                tempName += part + " "
            tempName = tempName.lower()
            
            songsList[tempName] = (Song(curSong[songName_i],
                                        curSong[1], curSong[2], curSong[3],
                                        curSong[4], curSong[5], curSong[6],
                                        curSong[7], curSong[8], curSong[9]))
    file.close()
 

## Score Match interface
def smgui() : 
    # background image
    bgImage = PhotoImage(file = "const-maki.png")
    backgroundLabel = Label(gui, image = bgImage)
    backgroundLabel.image = bgImage
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
                                  command = exitApp)
    cancelButton.place(x = buttonX + 130, y = buttonY)


if __name__ == "__main__"  :
    gui.title("SIF Score Match Tracker")
    gui.geometry("524x333")
    addSongs()
    smgui()
    gui.mainloop()
    