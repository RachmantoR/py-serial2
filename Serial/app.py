import tkinter as gui
import time as clock
import serial as port
import threading as worker

msg = ""
buttonflash = False
firstInit = False
indicator = "OFF"
alert = "Penyusup"
usb = port.Serial("COM6", baudrate=38400)

colorGreen = "#81cf09"

def INIT():
    global firstInit
    welcome1.place_forget()
    welcome2.place_forget()
    firstInit = True
    pageLoop()

def scaning():
    global indicator
    if usb.in_waiting > 0:
        stringdata = usb.read(usb.in_waiting)
        if stringdata == b'INIT':
            INIT()
        elif stringdata == b'ON':
            indicator = "ON  "
        elif stringdata == b'OFF':
            indicator = "OFF"
        print(stringdata)
    app.after(500, scaning)

try:
    def check():
        if firstInit:
            usb.write("check".encode())
        app.after(1000, check)

except buttonflash == True:
    while True:
        usb.write(msg.encode())
        clock.sleep(1)
        buttonflash = False

def On():
    global buttonflash, msg
    buttonflash = True
    msg = "ON-IN"

def Off():
    global buttonflash, msg
    buttonflash = True
    msg = "OFF-IN"

app = gui.Tk()
app.resizable(False,False)

photo1 = gui.PhotoImage(file="./asset/img/lcd_screen.png")
photo2 = gui.PhotoImage(file="./asset/img/panel.png")

#init

lcd = gui.Label(app, image=photo1, width=photo1.width() ,height=photo1.height())
lcd.grid(row=0, column=0)

panel = gui.Label(app, image=photo2, width=photo1.width() ,height=120)
panel.grid(row=1, column=0)

#button

buttonOn = gui.Button(panel, text="ON", font=("robot", 25), width=5, height=2, command=On)
buttonOn.place(x=10, y=10)

buttonOff = gui.Button(panel, text="OFF", font=("robot", 25), width=5, height=2, command=Off)
buttonOff.place(x=150, y=10)

#text indicator introduction

welcome1 = gui.Label(app, text="WELCOME", font=("robot", 25) ,bg=colorGreen ,fg="black")
welcome1.place(x=230, y=100)

welcome2 = gui.Label(app, text="USER", font=("robot", 25) ,bg=colorGreen ,fg="black")
welcome2.place(x=270, y=160)

def pageLoop():
    if firstInit :
        alertIn = gui.Label(app, text=alert, font=("robot", 25) ,bg=colorGreen ,fg="black")
        alertIn.place(x=100, y=100)

        info = gui.Label(app, text="Status :", font=("robot", 25) ,bg=colorGreen ,fg="black")
        info.place(x=100, y=160)

        indiIn = gui.Label(app, text=indicator, font=("robot", 25) ,bg=colorGreen ,fg="black")
        indiIn.place(x=270, y=160)
    app.after(500, pageLoop)

scaning()
check()

app.mainloop()