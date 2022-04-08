#! /usr/bin/thonny
import vlc
import os
import time
import flicklib

HOMEFOLDER = "/home/pi/Desktop/projectmammoth/Player/Model/"
PLAYLIST = [file for file in os.walk(HOMEFOLDER)]

player = vlc.MediaListPlayer()
playerInstance = vlc.Instance()
mediaList = playerInstance.media_list_new()

for video in PLAYLIST[0][2]:
    #print(video)
    media = playerInstance.media_new(HOMEFOLDER+video)
    mediaList.add_media(media)

def play_video():
    player.set_media_list(mediaList)
    player.play()
    player.get_media_player().toggle_fullscreen()
    player.set_playback_mode(vlc.PlaybackMode.repeat)
       

@flicklib.flick()
def flick(start,finish):
    global flicktxt
    flicktxt = start + ' - ' + finish
    if finish == "west":
        print(flicktxt)
        player.set_playback_mode(vlc.PlaybackMode.default)
        player.previous()
        player.set_playback_mode(vlc.PlaybackMode.repeat)
    elif finish == "east":
        print(flicktxt)
        player.set_playback_mode(vlc.PlaybackMode.default)
        player.next()
        player.set_playback_mode(vlc.PlaybackMode.repeat)
    elif finish == "north":
        print(flicktxt)
        currentVolume = player.get_media_player().audio_get_volume()
        player.get_media_player().audio_set_volume(currentVolume + 10)
        print("The volume is now" + str(currentVolume))
    elif finish == "south":
        print(flicktxt)
        currentVolume = player.get_media_player().audio_get_volume()
        player.get_media_player().audio_set_volume(currentVolume - 10)
        print("The volume is now" + str(currentVolume))
        
@flicklib.tap()
def tap(position):
    global taptxt
    print(position)
    player.get_media_player().pause()
    time.sleep(1)
    

if __name__=="__main__":
    play_video()