from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == "__main__":

    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    exsecs = 45*60
    eyessecs = 30*60

    while True:
        if time() - init_water > watersecs:
            print("Water drinking time Enter 'drank' to stop the alarm")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            print("Eye Exercise Time Enter 'done' to stop the alarm")
            musiconloop('eyes.mp3', 'done')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("PHYSICAL Exercise Time Enter 'done' to stop the alarm")
            musiconloop('physical.mp3', 'done')
            init_exercise = time()
            log_now("Physical Workout Done at")
