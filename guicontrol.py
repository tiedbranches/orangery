import serial
from tkinter import *
import time

serPort = "COM4"
baudRate = 115200
ser = serial.Serial(serPort, baudRate)
print("Serial port " + serPort + " opened  Baudrate " + str(baudRate))

def inputkey(event):

    print ("pressed", event.char)

    char=(event.char) #assigning pressed character to char variable
    sorter(char)


    charvariable.set(char) #assigning char to StringVar to be displayed

    stepperposition = "<" + char + "."
    print("Sending to stepper: ", stepperposition)
    ser.write(stepperposition.encode('utf-8'))

def gotozero():
    global vm1pos, vm2pos, vm3pos, hm1pos, hm2pos
    zero = "<0,0,0,0,0>"
    ser.write(zero.encode("utf-8"))
    vm1pos=vm2pos=vm3pos=hm1pos=hm2pos=0
    vmotor1.set("Vmotor1: " + str(vm1pos))
    vmotor2.set("Vmotor2: " + str(vm2pos))
    vmotor3.set("Vmotor3: " + str(vm3pos))
    hmotor1.set("Hmotor1: " + str(hm1pos))
    hmotor2.set("Hmotor2: " + str(hm2pos))


def zeroing():
    global vm1pos, vm2pos, vm3pos, hm1pos, hm2pos

    zeroMarker = "<0)"
    ser.write(zeroMarker.encode("utf-8"))
    time.sleep(0.5)
    vm1pos = vm2pos = vm3pos = hm1pos = hm2pos = 0
    position0 = "<0,0,0,0,0>"
    #ser.write(position0.encode("utf-8"))

    vmotor1.set("Vmotor1: " + str(vm1pos))
    vmotor2.set("Vmotor2: " + str(vm2pos))
    vmotor3.set("Vmotor3: " + str(vm3pos))
    hmotor1.set("Hmotor1: " + str(hm1pos))
    hmotor2.set("Hmotor2: " + str(hm2pos))

def poscaller(whichpos):
    global vm1pos, vm2pos, vm3pos, hm1pos, hm2pos
    pos = posrep(whichpos)

    position = "<" + str(pos[0]) + "," + str(pos[1]) + "," + str(pos[2]) + "," + str(pos[3]) + "," + str(pos[4]) + ">"
    print(position)
    ser.write(position.encode("utf-8"))

    vm1pos = pos[0]; vm2pos = pos[1]; vm3pos = pos[2]; hm1pos = pos[3]; hm2pos = pos[4]

    vmotor1.set("Vmotor1: " + str(vm1pos))
    vmotor2.set("Vmotor2: " + str(vm2pos))
    vmotor3.set("Vmotor3: " + str(vm3pos))
    hmotor1.set("Hmotor1: " + str(hm1pos))
    hmotor2.set("Hmotor2: " + str(hm2pos))



def sorter(inchar):
    global vm1pos, vm2pos, vm3pos, hm1pos, hm2pos

    if inchar == "7":
        vm1pos -= 100
        vmotor1.set("Vmotor1: " + str(vm1pos))

    elif inchar == "4":
        vm1pos += 100
        vmotor1.set("Vmotor1: " + str(vm1pos))

    elif inchar == "8":
        vm2pos += 100
        vmotor2.set("Vmotor2: " + str(vm2pos))

    elif inchar == "5":
        vm2pos -= 100
        vmotor2.set("Vmotor2: " + str(vm2pos))

    elif inchar == "9":
        vm3pos += 100
        vmotor3.set("Vmotor3: " + str(vm3pos))

    elif inchar == "6":
        vm3pos -= 100
        vmotor3.set("Vmotor3: " + str(vm3pos))

    elif inchar == "2":
        hm1pos += 100
        hmotor1.set("Hmotor1: " + str(hm1pos))

    elif inchar == "3":
        hm1pos -= 100
        hmotor1.set("Hmotor1: " + str(hm1pos))

    elif inchar == "1":
        hm2pos += 100
        hmotor2.set("Hmotor2: " + str(hm2pos))

    elif inchar == "0":
        hm2pos -= 100
        hmotor2.set("Hmotor2: " + str(hm2pos))

def possetter(whichpos):
    global pos1,pos2,pos3,pos4

    pos = posrep(whichpos)
    pos[0] = vm1pos; pos[1] = vm2pos; pos[2] = vm3pos; pos[3] = hm1pos ; pos[4] = hm2pos


###############################################################

pos1 = [-4100,3000,-4900,0,0]
pos2 = [-700,3700,-3400,0,0]
pos3 = [6400,3000,1300,0,0]
pos4 = [4400,100,1300,0,0]
###############################################################

def posrep(pos):
    if pos == 1:
        return pos1
    elif pos == 2:
        return pos2
    elif pos == 3:
        return pos3
    elif pos == 4:
        return pos4


def mover():
    pos1 = posrep(1)
    position1 = "<" + str(pos1[0]) + "," + str(pos1[1]) + "," + str(pos1[2]) + "," + str(pos1[3]) + "," + str(pos1[4]) + ">"
    pos2 = posrep(2)
    position2 = "<" + str(pos2[0]) + "," + str(pos2[1]) + "," + str(pos2[2]) + "," + str(pos2[3]) + "," + str(pos2[4]) + ">"
    pos3 = posrep(3)
    position3 = "<" + str(pos3[0]) + "," + str(pos3[1]) + "," + str(pos3[2]) + "," + str(pos3[3]) + "," + str(pos3[4]) + ">"
    pos4 = posrep(4)
    position4 = "<" + str(pos4[0]) + "," + str(pos4[1]) + "," + str(pos4[2]) + "," + str(pos4[3]) + "," + str(pos4[4]) + ">"

    position0 = "<0,0,0,0,0>"
    """
    position1 = "<0, 0, 500, 0, -0>"
    position2 = "<0, 0, -0, 0, -0>"
    """
    for i in range(3):
        stepperposition = position1
        ser.write(stepperposition.encode('utf-8'))

        time.sleep(7)

        stepperposition = position2
        ser.write(stepperposition.encode('utf-8'))

        time.sleep(4)

        stepperposition = position3
        ser.write(stepperposition.encode('utf-8'))

        time.sleep(6)

        stepperposition = position4
        ser.write(stepperposition.encode('utf-8'))

        time.sleep(3)


    ser.write(position0.encode('utf-8'))





root = Tk()
canvas = Canvas(root)
#canvas.grid()
canvas.focus_set()
canvas.bind("<Key>", inputkey)

#Zero variables Button
b = Button(root, bg = "#fc6949", text="zero variables", command=zeroing)
b.grid(row=0,column=0, sticky=W+E)

b.focus_set()
b.bind("<Key>",inputkey)

#Going to zero Button
b0 = Button(root, bg = "#fc6949", text="go to zero", command=gotozero)
b0.grid(row=0,column=1, sticky=W+E)

#pos1 Button
b1 = Button(root, bg = "#a04836", text="Position 1", command = lambda: poscaller(1))
b1.grid(row=1,column=0)

b1s=Button(root, bg = "#de5c5c", text="Set Position 1", command= lambda:possetter(1)).grid(row=2,column=0)

#pos2 Button
b2 = Button(root, bg = "#a04836", text="Position 2", command= lambda:poscaller(2))
b2.grid(row=1,column=1)

b2s=Button(root, bg = "#de5c5c", text="Set Position 2", command= lambda:possetter(2)).grid(row=2,column=1)

#pos3 Button
b3 = Button(root, bg = "#a04836", text="Position 3", command= lambda:poscaller(3))
b3.grid(row=1,column=2)

b3s=Button(root, bg = "#de5c5c", text="Set Position 3", command= lambda : possetter(3)).grid(row=2,column=2)

#pos4 Button
b4 = Button(root, bg = "#a04836", text="Position 4", command= lambda : poscaller(4))
b4.grid(row=1,column=3)

b4s=Button(root, bg = "#de5c5c", text="Set Position 4", command= lambda : possetter(4)).grid(row=2,column=3)



#Mover Button
m = Button(root, bg = "#cff93e", text="move back and forth", command=mover)
m.grid(row=0, column=2, sticky=W+E,columnspan=2)

"""JUST PRESSED"""
charvariable=StringVar()
charvariable.set("none")

"""Initialising motor position variables"""
vm1pos = vm2pos = vm3pos = hm1pos = hm2pos = 0

vmotor1 = StringVar()
vmotor1.set("Vmotor1: " + str(vm1pos))
vmotor2 = StringVar()
vmotor2.set("Vmotor2: " + str(vm2pos))
vmotor3 = StringVar()
vmotor3.set("Vmotor3: " + str(vm3pos))
hmotor1 = StringVar()
hmotor1.set("Hmotor1: " + str(hm1pos))
hmotor2 = StringVar()
hmotor2.set("Hmotor2: " + str(hm2pos))

justpressed = Label(root, textvariable = charvariable,font=("Courier",14))
justpressed.grid()

"""LABELS FOR MOTOR POSITIONS"""

vmotor1_l = Label(root, text = "vmotor1", textvariable = vmotor1,font=("Courier",14))
vmotor1_l.grid()
vmotor2_l = Label(root, text = "vmotor2", textvariable = vmotor2,font=("Courier",14))
vmotor2_l.grid()
vmotor3_l = Label(root, text = "vmotor3", textvariable = vmotor3,font=("Courier",14))
vmotor3_l.grid()
hmotor1_l = Label(root, text = "hmotor1", textvariable = hmotor1,font=("Courier",14))
hmotor1_l.grid()
hmotor2_l = Label(root, text = "hmotor2", textvariable = hmotor2,font=("Courier",14))
hmotor2_l.grid()





while True:


    root.update()


    #print("STEPPERPOSITION: ", stepperposition)
    #ser.write(stepperposition.encode('utf-8'))
