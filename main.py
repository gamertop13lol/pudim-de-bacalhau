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
def makefreq12tet(notefromc0: int):
    twelfthRootOf2 = 1.0594630943593
    change = notefromc0-57
    a4 = 440
    return a4 * twelfthRootOf2**change
# UI is not so hell in guizero, I say that because I don't know how to use tkinter. oops
o = App("pudim-de-bacalhau", width=800, height=600)
l = Box(o, align="left", width="fill", height="fill")
r = Box(o, align="right", width="fill", height="fill")
welcometext = Text(l, "welcome to pudim-de-bacalhau", color="#000000", size=18)
tutorial = PushButton(o, text="Tutorial", command=tutorialpudding)
addnote = 



o.display()