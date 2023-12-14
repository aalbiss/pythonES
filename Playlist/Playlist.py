from Canzone import *

class Playlist():
    playlist=[]
    
    def inserimento(self,numeroC):
        for i in range(numeroC):
            canzone=Canzone()
            canzone.inserimento()
            self.playlist.append(canzone)

    def __str__(self):
        for i in range(len(self.playlist)):
            return(self.playlist[i])