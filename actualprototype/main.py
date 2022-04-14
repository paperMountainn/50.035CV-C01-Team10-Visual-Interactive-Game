from playsound import playsound
import time
import os

def play_drum(drum):
    #gotta use mp3
    #pip install playsound==1.2.2 first
    audiofile = os.path.dirname(__file__)+'/drumsounds/'+drum+'.mp3'
    playsound(audiofile,False)

def do_they_intersect(drumpos,markerpos):
    #drumpos = (dx1,dy1,dx2,dy2)
    #markerpos = (mx1,my1,mx2,my2)
    dx1,dy1,dx2,dy2 = drumpos
    mx1,my1,mx2,my2 = markerpos
    return not(mx1 > dx2 or mx2<dx1 or my1 > dy2 or my2<dy1)
    
drumkit = ["snaredrum","hihats","crashcymbal","hightom","bassdrum","midtom","ridecymbal","lowtom"]
noofdrums = 8
f=open("fakedata.txt","r")
chosen_drumkit = drumkit[:noofdrums-1]

drum = (0,0,5,5)
marker = (5,5,10,13)
print(do_they_intersect(drum,marker))

for i in range(10): #change to while true later
    toplay = f.readline()
    toplay = toplay.strip()
    print(toplay)
    for drum in chosen_drumkit:
        if toplay == drum:
            play_drum(drum)
            time.sleep(2)
            
