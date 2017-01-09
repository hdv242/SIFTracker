'''
Created on Jan 8, 2017

@author: Bin
'''

class Match :
    
    def __init__(self, songName, score, combo, rank) :
        self.songName = songName
        self.score = score
        self.combo = combo
        self.rank = rank
        
class Song :
    
    def __init__(self, songName, attribute, maxCombo) :
        self.songName = songName
        self.attribute = attribute
        self.maxCombo = maxCombo
        self.plays = 0
        self.fc = 0
        
    def play(self) :
        self.plays += 1
    
    def fc(self) :
        self.fc += 1
        
    def fcRate(self) :
        return self.fc / self.plays
