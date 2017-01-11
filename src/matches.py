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
    
    def __init__(self, songName, attribute, diff, fcCombo, maxScore, maxCombo,
                 avgScore, avgCombo, plays, fc) :
        
        self.songName  = songName
        self.attribute = attribute
        self.diff      = diff
        self.fcCombo   = int(fcCombo)
        self.maxScore  = int(maxScore)
        self.maxCombo  = int(maxCombo)
        self.avgScore  = float(avgScore)
        self.avgCombo  = float(avgCombo)
        self.plays     = int(plays)
        self.fc        = int(fc)
        
        
    def play(self, score, combo) :
        self.plays += 1
        score = int(score)
        combo = int(combo)
        
        # update scores and combos
        if (self.plays != 0) :
            self.avgScore = (self.avgScore * (self.plays - 1) + score) / self.plays
            self.avgCombo = (self.avgCombo * (self.plays - 1) + combo) / self.plays
        else :
            self.avgScore = score
            self.avgCombo = combo
        
        if (self.maxScore < score) :
            self.maxScore = score;
        if (self.maxCombo < combo) :
            self.maxCombo = combo
        if (self.fcCombo == combo) :
            self.fc += 1
        
    
    def name (self) :
        return self.songName
    
        
    def fcRate(self) :
        return self.fc / self.plays
    
    
    def write(self, file) :
        file.write(self.songName + " " + 
                   self.attribute + " " +
                   self.diff + " " +
                   str(self.fcCombo) + " " +
                   str(self.maxScore) + " " +
                   str(self.maxCombo) + " " +
                   str(self.avgScore) + " " +
                   str(self.avgCombo) + " " +
                   str(self.plays) + " " +
                   str(self.fc))
