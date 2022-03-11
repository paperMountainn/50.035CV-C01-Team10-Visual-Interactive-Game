from playsound import playsound
import threading

def play_drum():

    # import required module
    
    
    # for playing note.wav file
    # threading.Thread(target=playsound, args=('sound_file/snare.wav',), daemon=True).start()
    playsound('sound_file/snare.wav')
    print('playing sound using playsound')
    
    
# testing
if __name__ == "__main__":
    play_drum()