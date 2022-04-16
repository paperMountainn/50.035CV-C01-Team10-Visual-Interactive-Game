from playsound import playsound
import threading

filepath = "/Users/prispearls/Documents/Github/50.035CV-C01-Team10-Visual-Interactive-Game/prelim_trials/opencv_virt_drum/"

def play_snare():
    playsound(filepath + 'sound_file/snare.wav')
    # print('playing sound using playsound')

def play_hihat():
    playsound(filepath + 'sound_file/hihat.mp3')
    # print('playing sound using playsound')

def play_tom():
    playsound(filepath + 'sound_file/tom.mp3')
    # print('playing sound using playsound')

# testing
if __name__ == "__main__":
    play_snare()
    play_hihat()
    play_tom()