from guizero import TextBox, App, Text, PushButton, Box
# the great wall of function
def tutorialpudding():
    pass
alphabet = "abcdefghijklmnopqrstuvwxyz"
whitekeys = {"c":0,"d":2,"e":4,"f":5,"g":7,"a":9,"b":11}
def tonotefromc0(notename: str):
    base = whitekeys[notename[0]]
    acc = 0
    if notename[1] in "#b":
        acc = 1 if notename[1]=="#" else -1
        octave = int(notename[2])
    else:
        octave = int(notename[1])
    return octave*12+base+acc
    
# the great wall of frequencies
notefromc0_freq12tet = [16.35,17.32,18.35,19.45,20.6,21.83,23.12,24.5,25.96,27.5,29.14,30.87,32.7,34.65,36.71,38.89,41.2,43.65,46.25,49,51.91,55,58.27,61.74,65.41,69.3,73.42,77.78,82.41,87.31,92.5,98,103.83,110,116.54,123.47,130.81,138.59,146.83,155.56,164.81,174.61,185,196,207.65,220,233.08,246.95,261.63,277.18,293.66,311.13,329.63,349.23,369.99,392,415.3,440,466.16,493.88,523.25,554.37,587.33,622.25,659.25,698.46,739.99,783.99,830.61,880,932.33,987.77,1046.5,1108.73,1174.66,1244.51,1318.51,1396.91,1479.98,1567.98,1661.22,1760.00,1864.66,1975.53]
# UI is not so hell in guizero, I say that because I don't know how to use tkinter. oops
o = App("pudim-de-bacalhau", width=800, height=600)
l = Box(o, align="left", width="fill", height="fill")
r = Box(o, align="right", width="fill", height="fill")
welcometext = Text(l, "welcome to pudim-de-bacalhau", color="#000000", size=24)
tutorial = PushButton(o, text="Tutorial", command=tutorialpudding)



o.display()