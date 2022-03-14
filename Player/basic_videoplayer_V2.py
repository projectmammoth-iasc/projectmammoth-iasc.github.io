import vlc
import os
import time

HOMEFOLDER = "/home/pi/Desktop/projectmammoth-iasc.github.io-main/Player/Model/"
PLAYLIST = [file for file in os.walk(HOMEFOLDER)]
print(PLAYLIST[0][2])

def main():
    def play_video(video):
        player = vlc.MediaPlayer(video)
        player.play()
        player.toggle_fullscreen()
        
    for video in PLAYLIST[0][2]:
        play_video(HOMEFOLDER + video)
        
       
if __name__=="__main__":
    main()
