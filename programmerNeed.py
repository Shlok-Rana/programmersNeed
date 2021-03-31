#Healthy programmer
#Working time of a programmer 9am to 5pm
#water  water.mp3 (3.5 litres) - every 30 min
#eyes eyes.mp3  - every 120 min
#physical activity physical.mp3 - every 45 min
#pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time
print('**************** Programmers need ****************')
print("'done' ---> Water")
print("'doneeye' ---> Eyes")
print("'donephy' ---> Physical Activity")
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(50)#made the loop and play the audio 50 times
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 30*60
    exsecs = 45*60
    eyessecs = 120*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'done' to stop the alarm.")
            musiconloop('water.mp3', 'done')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeye' to stop the alarm.")
            musiconloop('eyes.mp3', 'doneeye')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('physical.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")

