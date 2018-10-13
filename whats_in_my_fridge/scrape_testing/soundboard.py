import sys
from tkinter import *
import simpleaudio
from simpleaudio import *


def playExplosion():
    wave_obj = simpleaudio.WaveObject.from_wave_file("c:\\Users\\Bowen\\Downloads\\117091__lagomen__climactic-boom.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
def playBabyLaugh():
    wave_obj = simpleaudio.WaveObject.from_wave_file("C:\\Users\\Bowen\\Downloads\\110392__soundscalpel-com__human-baby-toddler-male-15-months-laugh.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
def playFart():
    wave_obj = simpleaudio.WaveObject.from_wave_file("C:\\Users\\Bowen\\Downloads\\61046__timtube__fart-2.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
def playBird():
    wave_obj = simpleaudio.WaveObject.from_wave_file("C:\\Users\\Bowen\\Downloads\\34207__cajo__birds-01.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

SoundBoard = Tk()
SoundBoard.geometry("370x170")
SoundBoard.title("SoundBoard")

explosionButton = Button(SoundBoard, height=5, width=25, text='Explosion', command=playExplosion).grid(row=0, column=0)
babyButton = Button(SoundBoard, height=5, width=25, text='Baby Laugh', command=playBabyLaugh).grid(row=1, column=0)
fartButton = Button(SoundBoard, height=5, width=25, text='Fart!', command=playFart).grid(row=0, column=1)
birdButton = Button(SoundBoard, height=5, width=25, text='Bird', command=playBird).grid(row=1, column=1)

SoundBoard.mainloop()
