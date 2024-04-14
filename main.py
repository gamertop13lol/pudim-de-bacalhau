from guizero import TextBox, App, Text, PushButton, Box
from tkinter import Tk, Frame, Label, Button, X, Y, BOTH
import ttkbootstrap as ttk
import math
import pyaudio
from makesample import WAVE4000

w = Tk()
w.title("pudim-de-bacalhau")
w.geometry("600x600")
PyAudio = pyaudio.PyAudio
SAMPLERATE = 44800
alphabet = "abcdefghijklmnopqrstuvwxyz"
whitekeys = {"c":0,"d":2,"e":4,"f":5,"g":7,"a":9,"b":11}
p = PyAudio()
stream = p.open(format = p.get_format_from_width(2), channels = 1, rate = SAMPLERATE, output = True)

# the great wall of functions
def playnote(note: str, length: int, channel: int, volume: int):
    frequency = makefreq12tet(tonotefromc0(note.lower()))

    frames = int(SAMPLERATE * length)
    trailframes = frames % SAMPLERATE
    sinchange = 4000/SAMPLERATE
    dt = b''

    if channel == 3:
        for x in range(frames): # Wave
            a=int(WAVE4000[int((x*frequency*sinchange)%4000)]*volume/64)
            dt+=bytes([a%256,a//256])
    for x in range(trailframes):
            dt+=bytes([0, 0])

    stream.write(dt)

def tutorialpudding():
    pass

def tonotefromc0(notename: str):
    base = whitekeys[notename[0]]
    acc = 0
    if notename[1] in "#b":
        acc = 1 if notename[1]=="#" else -1
        octave = int(notename[2])
    else:
        octave = int(notename[1])
    return octave*12+base+acc
def makefreq12tet(notefromc0: int):
    twelfthRootOf2 = 1.0594630943593
    change = notefromc0-57
    a4 = 440
    return a4 * twelfthRootOf2**change
# The UI
o = Frame(w)
l = Frame(w)
r = Frame(w)

welcometext = Label(o, text="welcome to pudim-de-bacalhau", font="Helvetica 18")
inputencouragementtext = Label(l, text="Input some notes!", font="Helvetica 18")
tutorial = Button(r, text="Tutorial", command=tutorialpudding, pady=8)
inputencouragementtext.pack()
welcometext.pack()
tutorial.pack(fill=X)

o.pack(pady=5, padx=5, side="top", fill=X)
l.pack(padx=5, side="left", fill=BOTH, expand=1)
r.pack(padx=5, side="left", fill=BOTH, expand=1)

playnote("Bb3", 0.25, 3, 16)
playnote("D4", 0.25, 3, 16)
playnote("F4", 0.25, 3, 16)
stream.stop_stream()
stream.close()
p.terminate()

w.mainloop()