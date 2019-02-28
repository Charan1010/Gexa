import inotify.adapters
from threading import Thread
from playsound import playsound
import os
import time 
from gexa import wrapper
def playmusic(music):
    playsound(music)



notifier = inotify.adapters.Inotify()
print("NOTIFIER STARTED")
notifier.add_watch('/home/charan/project')
storage=[]
init_flag=0
play_id=1000
for event in notifier.event_gen():
    play_id=1000
    if event is not None:
        #print(event)      # uncomment to see all events generated
        if 'IN_CREATE' in event[1]:
             #print ("file '{0}' created in '{1}'".format(event[3], event[2]))
             time.sleep(0.02)
             storage.append(wrapper(event[3]))
             if(len(storage)==5 and init_flag==0):
                 play_id=storage[-1]
                 init_flag=1
             if(len(storage)>30):
                 s=set(storage)
                 if(len(s)>1):
                     play_id=storage[-1]
                 storage=[]
    if(play_id!=1000):
        print("INITIATING ALEXA VOICE\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(play_id)
        if(play_id==0):
            print("PLAYING WEATHER for ID  "+str(play_id))
            thread = Thread(target = playmusic, args = ('weather.mp3', ))
            thread.start()
            #playsound('weather.mp3')
        elif(play_id==1 or play_id==4):
            print("PLAYING MUSIC for ID  "+str(play_id))
            thread = Thread(target = playmusic, args = ('music.mp3', ))
            thread.start()
            #playsound('music.mp3')
        
def playmusic(music):
    playsound(music)

                 

             
