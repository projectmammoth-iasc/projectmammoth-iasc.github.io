import vlc
import os
import time
import flicklib
import pygame

HOMEFOLDER = "/home/pi/Desktop/projectmammoth-iasc.github.io-main/Player/Model/"
PLAYLIST = [file for file in os.walk(HOMEFOLDER)]
print(PLAYLIST[0][2])
pygame.mixer.init()

def main():

    player = vlc.MediaListPlayer()

    def play_video():
        player.set_media_list(mediaList)
        player.play()
        player.get_media_player().toggle_fullscreen()
        
    playerInstance = vlc.Instance()
    mediaList = playerInstance.media_list_new()
    
    for video in PLAYLIST[0][2]:
        print(video)
        media = playerInstance.media_new(HOMEFOLDER+video)
        mediaList.add_media(media)
        
    print(playerInstance)
    
    def play_music(backgroundMusic):
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load(backgroundMusic)
        pygame.mixer.music.play(loops=0)
    def play_narration():
        soundNarra = pygame.mixer.Sound(varNarration)
        pygame.mixer.Sound.play("Sound/polar-bear-samples/roar-sound.wav")
        pygame.mixer.set_num_channels(1)
        soundNarra.set_volume(0.5)
        
    
    play_video()
    play_music("Sound/coralbackgrnd.mp3")
        

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
    main()
