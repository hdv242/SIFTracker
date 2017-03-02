'''
Created on Jan 6, 2017

@author: Bin
'''

from tkinter import Button, Toplevel
from tkinter import Entry
from tkinter import Label
from tkinter import PhotoImage
from tkinter import Tk
from tkinter import messagebox
from tkinter import Listbox
from matches import Song
from tkinter.constants import ACTIVE

songName_i = 0  # index of song name in entries
score_i = 1     # index of score in entries
combo_i = 2     # index of combo in entries
rank_i = 3      # index of rank in entries
homeGUI = Tk()  # creates the home GUI
smGUI = None    # score match GUI
entries = []    # songName, score, combo, and rank
songsList = {}  # songs will be eager cached as name : object
file = ""


## create a new score match file
def newScoreMatch():
    ## add gui here
    return


    

## writes submitted information into file
def writeToFile():
    file = "song_stats.txt"
    with open(file, 'w') as file :
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
    homeGUI.quit()
    
    
## clears out entry boxes
def clearEntries() :
    for e in entries :
        e.delete(0, 'end')


## facilitates input of information
def inputAnswer() :
    # check for missing fields
    if (entries[songName_i].get(ACTIVE) == "" or entries[score_i].get() == ""
        or entries[combo_i].get() == "" or entries[rank_i].get(ACTIVE) == "") :
        messagebox.showerror("Failed!", "Missing field(s)", parent = smGUI)
        return
    
    # check for incorrect song name
    name = entries[songName_i].get(ACTIVE).lower() + " "
    if (songsList.get(name) == None) :
        messagebox.showerror("Failed!", "Cannot find song", parent = smGUI)
        return
    
    # update song info
    songsList.get(name).play(entries[score_i].get(), entries[combo_i].get())
    clearEntries()
    messagebox.showinfo("Success!", "Info submitted", parent = smGUI)
    smGUI.destroy()

## add songs from file
def addSongs() :
    with open("song_stats_u's_ex.txt") as file :
        for line in file :
            # parse from file, fix name, create new Song and add it to songsList
            curSong = line.split();
            curName = curSong[songName_i].split('_')
            tempName = ""
            for part in curName :
                tempName += part + " "
            tempName = tempName.lower()
            songsList[tempName] = Song(curSong[songName_i],
                                       curSong[1], curSong[2], curSong[3],
                                       curSong[4], curSong[5], curSong[6],
                                       curSong[7], curSong[8])
    file.close()


## *************************
##
##         GUI stuff
##
## *************************


## Score Match interface
def setupSMGUI() :
    global smGUI 
    smGUI = Toplevel(homeGUI, height = 333, width = 524)
    # background image
    bgImage = PhotoImage(file = "const-maki.png")
    backgroundLabel = Label(smGUI, image = bgImage)
    backgroundLabel.image = bgImage
    backgroundLabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    # song name list box
    songX = 100
    songY = 200
    songlb = Listbox(smGUI, activestyle = "none", height = 1, width = 30)
    songlb.place(x = songX, y = songY)
    for song in songsList:
        songlb.insert("end", songsList.get(song).formattedName())
    songLabel = Label(smGUI, text = "Song")
    songLabel.place(x = songX - 33, y = songY)
    entries.append(songlb)
    
    # score input field
    score = ""
    scoreX = songX + 250
    scoreY = songY
    scoreLabel = Label(smGUI, text = "Score")
    scoreLabel.place(x = scoreX - 35, y = scoreY)
    scoreEntry = Entry(smGUI, textvariable = score, width = 10)
    scoreEntry.place(x = scoreX, y = scoreY)
    entries.append(scoreEntry) 
    
    # combo input field
    combo = ""
    comboX = songX
    comboY = songY + 30
    comboLabel = Label(smGUI, text = "Combo")
    comboLabel.place(x = comboX - 45, y = comboY)
    comboEntry = Entry(smGUI, textvariable = combo, width = 10)
    comboEntry.place(x = comboX, y = comboY)
    entries.append(comboEntry)
    
    # rank list box
    rankX = songX + 250
    rankY = comboY
    ranklb = Listbox(smGUI, activestyle = "none", height = 1, width = 5)
    ranklb.place(x = rankX, y = rankY)
    for num in [1, 2, 3, 4]:
        ranklb.insert("end", num)
    rankLabel = Label(smGUI, text = "Rank")
    rankLabel.place(x = rankX - 33, y = rankY)
    entries.append(ranklb)
    
    # submit, clear, cancel buttons
    buttonX = 170
    buttonY = 270
    submitButton = Button(smGUI,
                          text = "Submit",
                          cursor = "heart", 
                          command = inputAnswer)
    submitButton.place(x = buttonX, y = buttonY)
    clearButton = Button(smGUI,
                         text = "Clear",
                         cursor = "heart",
                         command = clearEntries)
    clearButton.place(x = buttonX + 70, y = buttonY)
    cancelButton = Button(smGUI,
                          text = "Back",
                          cursor = "heart",
                          command = smGUI.destroy)
    cancelButton.place(x = buttonX + 130, y = buttonY)


def setupHomeGUI() :
    # background image
    bgImage = PhotoImage(file = "const-maki.png")
    backgroundLabel = Label(homeGUI, image = bgImage)
    backgroundLabel.image = bgImage
    backgroundLabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    buttonX = 210
    buttonY = 90
    addNewSMButton = Button(homeGUI,
                            text = "Add new Score Match",
                            cursor = "heart",
                            command = newScoreMatch)
    addNewSMButton.place(x = buttonX, y = buttonY)
    updateSMButton = Button(homeGUI,
                            text = "Update current Score Match",
                            cursor = "heart",
                            command = setupSMGUI)
    updateSMButton.place(x = buttonX - 18, y = buttonY + 40)
    songStatsButton = Button(homeGUI,
                             text = "View song stats",
                             cursor = "heart")
    songStatsButton.place(x = buttonX + 15, y = buttonY + 80)
    exitButton = Button(homeGUI,
                        text = "Save and Exit",
                        cursor = "heart",
                        command = exitApp)
    exitButton.place(x = buttonX + 20, y =  buttonY + 120)
    

if __name__ == "__main__"  :
    homeGUI.title("SIF Score Match Tracker")
    homeGUI.geometry("524x333")
    addSongs()
    setupHomeGUI()
    homeGUI.mainloop()
    