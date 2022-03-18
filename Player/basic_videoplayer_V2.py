import vlc
import os
import time
import flicklib

HOMEFOLDER = "/home/pi/Desktop/projectmammoth-iasc.github.io-main/Player/Model/"
PLAYLIST = [file for file in os.walk(HOMEFOLDER)]
print(PLAYLIST[0][2])

def main():

    player = vlc.MediaListPlayer()
#    vlc.libvlc_toggle_fullscreen()

    def play_video():
        player.set_media_list(mediaList)
        player.play()
#         player.toggle_fullscreen()
        
    playerInstance = vlc.Instance()
    mediaList = playerInstance.media_list_new()
    
    for video in PLAYLIST[0][2]:
        print(video)
        media = playerInstance.media_new(HOMEFOLDER+video)
        mediaList.add_media(media)
        
    print(playerInstance)
    
    play_video()
        
#    media = PLAYLIST[0][2][1]
#    print(media)
#    play_video(HOMEFOLDER + media)

    @flicklib.flick()
    def flick(start,finish):
        global flicktxt
        flicktxt = start + ' - ' + finish
        if finish == "west":
            print(flicktxt)
            player.previous()
        elif finish == "east":
            print(flicktxt)
            player.next()
            
            

if __name__=="__main__":
    main()
