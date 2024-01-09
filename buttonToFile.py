import tkinter
import os
screen = tkinter.Tk()

def runThis():
    # os.system("forgotpage-01.png")
    os.system("C:\Users\CS12\Downloads\TeamsSetup_c_w_.exe")
    # 

buttonFile = tkinter.Button(text = "Press here", command = runThis)
buttonFile.pack()

screen.mainloop()