from playsound import playsound
import threading

def play_snare():
    playsound('/Users/prispearls/Documents/50.035CV-C01-Team10-Visual-Interactive-Game/prelim_trials/opencv_virt_drum/sound_file/snare.wav')
    print('playing sound using playsound')

def play_hihat():
    playsound('sound_file/hihat.mp3')
    print('playing sound using playsound')

def play_tom():
    playsound('sound_file/tom.mp3')
    print('playing sound using playsound')

# testing
if __name__ == "__main__":
    play_snare()
    play_hihat()
    play_tom()