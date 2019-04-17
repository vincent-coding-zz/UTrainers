#UTrainers
#Created by vincent-coding
#Gbatemp : https://gbatemp.net/members/vincent-coding.484105/
#Github  : https://github.com/vincent-coding
#
#License : Apache License 2.0
#
#!usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox
import os
from tcpgecko import *
import sys

#Variables
version = "Alpha"

#DarkU

def DarkUStart():
    def checkinject():
        ip = darkuwiiuip.get()
        colors = darklistecouleur.get()
        if ip != "":
            if colors=="Reset":
                wtcp = TCPGecko(ip)
                wtcp.pokemem(0x105DD0A8, 0x3F800000)
                wtcp.s.close()
                tkinter.messagebox.showinfo("UTrainers/DarkU - "+version, "Injection successful!")
            elif colors=="White":
                wtcp = TCPGecko(ip)
                wtcp.pokemem(0x105DD0A8, 0x40000000)
                wtcp.s.close()
                tkinter.messagebox.showinfo("UTrainers/DarkU - "+version, "Injection successful!")            
            elif colors=="Black":
                btcp = TCPGecko(ip)
                btcp.pokemem(0x105DD0A8, 0x00000000)
                btcp.s.close()
                tkinter.messagebox.showinfo("UTrainers/DarkU - "+version, "Injection successful!")
            elif colors=="Light grey":
                lgtcp = TCPGecko(ip)
                lgtcp.pokemem(0x105DD0A8, 0x3E800000)
                lgtcp.s.close()
                tkinter.messagebox.showinfo("UTrainers/DarkU - "+version, "Injection successful!")  
            elif colors=="Grey":
                gtcp = TCPGecko(ip)
                gtcp.pokemem(0x105DD0A8, 0x3D800000)
                gtcp.s.close()
                tkinter.messagebox.showinfo("UTrainers/DarkU - "+version, "Injection successful!")
            elif colors=="Dark grey":
                dgtcp = TCPGecko(ip)
                dgtcp.pokemem(0x105DD0A8, 0x3C800000)
                dgtcp.s.close()
                tkinter.messagebox.showinfo("UTrainers/DarkU- "+version, "Injection successful!")   
            elif colors=="Very dark grey":
                vdgtcp = TCPGecko(ip)
                vdgtcp.pokemem(0x105DD0A8, 0x3B800000)
                vdgtcp.s.close()
                tkinter.messagebox.showinfo("UTrainers/DarkU - "+version, "Injection successful!")            
        else:
            tkinter.messagebox.showerror("UTrainers/DarkU - "+version, "Please fill in the \"wiiu ip\" field")
    
    
    start.destroy()
    DarkU = Tk()
    
    #DarkU Variable
    darkuwiiuip = StringVar()
    darklistecouleur = StringVar()
    darklistecouleur.set("Reset")    
    
    # DarkU Information
    DarkU.title('UTrainers/DarkU - '+version)
    largeur      = 400
    hauteur      = 175
    largeurEcran = DarkU.winfo_screenwidth()
    hauteurEcran = DarkU.winfo_screenheight()
    x            = (largeurEcran / 2) - (largeur / 2)
    y            = (hauteurEcran / 2) - (hauteur /2)
    DarkU.geometry('%dx%d+%d+%d' % (largeur, hauteur, x, y))
    DarkU.resizable(width = False, height = False)    
    
    # DarkU Component
    darkcontent = Frame(DarkU,width=250, height=15).pack()
    darkiplabel = Label(darkcontent, text="WiiU ip").pack()
    darkipentry = Entry(darkcontent, textvariable=darkuwiiuip, justify=CENTER).pack()
    darklistecolorsmenu = OptionMenu(darkcontent, darklistecouleur, "Reset","White","Light grey", "Grey", "Dark grey", "Very dark grey", "Black").pack(pady=5)
    darkinject = Button(darkcontent, text="Inject", command=checkinject).pack(pady=5)
    
    darkinfo = Label(DarkU, text="Created by vincent-coding").pack(side=BOTTOM)    
    
    DarkU.mainloop()

#MK8
def Mk8Start():
    def mk8injectcommand():
        mk8ip = mk8wiiuip.get()
        mk8c1 = mk8checkbox1.get()
        mk8c2 = mk8checkbox2.get()
        mk8c3 = mk8checkbox3.get()
        mk8c4 = mk8checkbox4.get()
        mk8c5 = mk8checkbox5.get()
        mk8c6 = mk8checkbox6.get()
        mk8c7 = mk8checkbox7.get()
        mk8c8 = mk8checkbox8.get()
        mk8c9 = mk8checkbox9.get()
        mk8c10 = mk8checkbox10.get()
        mk8c11 = mk8checkbox11.get()
        mk8c12 = mk8checkbox12.get()
        mk8c13 = mk8checkbox13.get()
        mk8c14 = mk8checkbox14.get()
        mk8c15 = mk8checkbox15.get()
        
        mk8injectsucces = 0
        
        if mk8ip != "":
            if mk8c1 == 1:
                mk8c1tcp = TCPGecko(mk8ip)
                mk8c1tcp.pokemem(0x10517B8C, 0x80800000)
                mk8c1tcp.s.close()
                mk8injectsucces = 1
            if mk8c2 == 1:
                mk8c2tcp = TCPGecko(mk8ip)
                mk8c2tcp.pokemem(0x10517B0C, 0x3FC00000)
                mk8c2tcp.s.close()
                mk8injectsucces = 1
            if mk8c3 == 1:
                mk8c3tcp = TCPGecko(mk8ip)
                mk8c3tcp.pokemem(0x10517B90, 0x00000000)
                mk8c3tcp.s.close()
                mk8injectsucces = 1
            if mk8c4 == 1:
                mk8c4tcp = TCPGecko(mk8ip)
                mk8c4tcp.pokemem(0x105F6AE4, 0x3FE00000)
                mk8c4tcp.s.close()
                mk8injectsucces = 1
            if mk8c5 == 1:
                mk8c5tcp = TCPGecko(mk8ip)
                mk8c5tcp.pokemem(0x105B9038, 0x3FC00000)
                mk8c5tcp.s.close()
                mk8injectsucces = 1                
            if mk8c6 == 1:
                mk8c6tcp = TCPGecko(mk8ip)
                mk8c6tcp.pokemem(0x105F3310, 0x42000000)
                mk8c6tcp.s.close()
                mk8injectsucces = 1 
            if mk8c7 == 1:
                mk8c7tcp = TCPGecko(mk8ip)
                mk8c7tcp.pokemem(0x1051A248, 0x00000000)
                mk8c7tcp.s.close()
                mk8injectsucces = 1 
            if mk8c8 == 1:
                mk8c8tcp = TCPGecko(mk8ip)
                mk8c8tcp.pokemem(0x1051E724, 0x80800000)
                mk8c8tcp.s.close()
                mk8injectsucces = 1  
            if mk8c9 == 1:
                mk8c9tcp = TCPGecko(mk8ip)
                mk8c9tcp.pokemem(0x10519B74, 0x40000000)
                mk8c9tcp.s.close()
                mk8injectsucces = 1 
            if mk8c10 == 1:
                mk8c10tcp = TCPGecko(mk8ip)
                mk8c10tcp.pokemem(0x1050F024, 0x00000000)
                mk8c10tcp.s.close()
                mk8injectsucces = 1  
            if mk8c11 == 1:
                mk8c11tcp = TCPGecko(mk8ip)
                mk8c11tcp.pokemem(0x105232D0, 0x3C000000)
                mk8c11tcp.s.close()
                mk8injectsucces = 1 
            if mk8c12 == 1:
                mk8c12tcp = TCPGecko(mk8ip)
                mk8c12tcp.pokemem(0x105182DC, 0x43000000)
                mk8c12tcp.s.close()
                mk8injectsucces = 1 
            if mk8c13 == 1:
                mk8c13tcp = TCPGecko(mk8ip)
                mk8c13tcp.pokemem(0x105E9334, 0x00000000)
                mk8c13tcp.s.close()
                mk8injectsucces = 1 
            if mk8c14 == 1:
                mk8c14tcp = TCPGecko(mk8ip)
                mk8c14tcp.pokemem(0x10522D28, 0x3F810000)
                mk8c14tcp.s.close()
                mk8injectsucces = 1                  
            if mk8c15 == 1:
                mk8c15tcp = TCPGecko(mk8ip)
                mk8c15tcp.pokemem(0x10522D28, 0x3F810000)
                mk8c15tcp.s.close()
                mk8injectsucces = 1
            if mk8c13 == 1:
                tkinter.messagebox.showinfo("UTrainers/MK8 - "+version, "No idem indicator + position freeze.")
            if mk8c14 == 1 and mk8c15 == 1:
                tkinter.messagebox.showwarning("UTrainers/MK8 - "+version, "Warning, you have selected to enable and disable the speed hack at the same time. To avoid errors, the speed hack has been disabled.")
            if mk8injectsucces == 1:
                tkinter.messagebox.showinfo("UTrainers/MK8 - "+version,"Successful injection")
            elif mk8c1 == 0 and mk8c2 == 0 and mk8c3 == 0 and mk8c4 == 0 and mk8c5 == 0 and mk8c6 == 0 and mk8c7 == 0 and mk8c8 == 0 and mk8c9 == 0 and mk8c10 == 0 and mk8c11 == 0 and mk8c12 == 0 and mk8c13 == 0 and mk8c14 == 0 and mk8c15 == 0:
                tkinter.messagebox.showerror("UTrainers/MK8 - "+version,"Please select cheat codes to inject!")
        else:
            tkinter.messagebox.showerror("UTrainers/MK8 - "+version, "Please fill in the \"wiiu ip\" field")
    
    start.destroy()
    #MK8 Window
    mk8 = Tk()
    
    #MK8 Variable
    mk8wiiuip = StringVar()
    
    mk8checkbox1 = IntVar()
    mk8checkbox2 = IntVar()
    mk8checkbox3 = IntVar()
    
    mk8checkbox4 = IntVar()
    mk8checkbox5 = IntVar()
    mk8checkbox6 = IntVar()
    
    mk8checkbox7 = IntVar()
    mk8checkbox8 = IntVar()
    mk8checkbox9 = IntVar()
    
    mk8checkbox10 = IntVar()
    mk8checkbox11 = IntVar()
    mk8checkbox12 = IntVar()    
    
    mk8checkbox13 = IntVar()
    mk8checkbox14 = IntVar()
    mk8checkbox15 = IntVar()    
    
    #MK8 Information
    mk8.title('UTrainers/MK8 - '+version)
    largeur      = 565
    hauteur      = 250
    largeurEcran = mk8.winfo_screenwidth()
    hauteurEcran = mk8.winfo_screenheight()
    x            = (largeurEcran / 2) - (largeur / 2)
    y            = (hauteurEcran / 2) - (hauteur /2)
    mk8.geometry('%dx%d+%d+%d' % (largeur, hauteur, x, y))
    mk8.resizable(width = False, height = False)    

#MK8 Component
    
    #IP
    mk8wiiuiplabel = Label(mk8, text="WiiU Ip", width=25).grid(row=0, column=1)
    mk8wiiuipentry = Entry(mk8, textvariable=mk8wiiuip, width=25, justify=CENTER).grid(row=1, column=1)
    
    mk8separipcheat = Label(mk8, text="").grid(row=2, column=0)
    
    #First cheats lines
    mk8cheat1 = Checkbutton(mk8, text="Bob-omb No Damage", width=20, onvalue=1, offvalue=0, variable=mk8checkbox1).grid(row=3, column=0)
    mk8cheat2 = Checkbutton(mk8, text="Jumping Bombs", width=20, onvalue=1, offvalue=0, variable=mk8checkbox2).grid(row=3, column=1)
    mk8cheat3 = Checkbutton(mk8, text="Invisible Bob-omb", width=20, onvalue=1, offvalue=0, variable=mk8checkbox3).grid(row=3, column=2)
    
    #2 cheats lines
    mk8cheat4 = Checkbutton(mk8, text="No Music", width=20, onvalue=1, offvalue=0, variable=mk8checkbox4).grid(row=4, column=0)
    mk8cheat5 = Checkbutton(mk8, text="Kill Lakitu", width=20, onvalue=1, offvalue=0, variable=mk8checkbox5).grid(row=4, column=1)
    mk8cheat6 = Checkbutton(mk8, text="Weird Animations", width=20, onvalue=1, offvalue=0, variable=mk8checkbox6).grid(row=4, column=2)
    
    #3 cheats lines
    mk8cheat7 = Checkbutton(mk8, text="No Blooper Ink on Screen", width=20, onvalue=1, offvalue=0, variable=mk8checkbox7).grid(row=5, column=0)
    mk8cheat8 = Checkbutton(mk8, text="No Lightningbolt Flash", width=20, onvalue=1, offvalue=0, variable=mk8checkbox8).grid(row=5, column=1)
    mk8cheat9 = Checkbutton(mk8, text="Jumping Fire Ball", width=20, onvalue=1, offvalue=0, variable=mk8checkbox9).grid(row=5, column=2)
    
    #4 cheats lines
    mk8cheat10 = Checkbutton(mk8, text="No Object Collision", width=20, onvalue=1, offvalue=0, variable=mk8checkbox10).grid(row=6, column=0)
    mk8cheat11 = Checkbutton(mk8, text="No-Kart", width=20, onvalue=1, offvalue=0, variable=mk8checkbox11).grid(row=6, column=1)
    mk8cheat12 = Checkbutton(mk8, text="Boomerang Deleter", width=20, onvalue=1, offvalue=0, variable=mk8checkbox12).grid(row=6, column=2)    
    
    #5 cheats lines
    mk8cheat13 = Checkbutton(mk8, text="No Item Indicator", width=20, onvalue=1, offvalue=0, variable=mk8checkbox13).grid(row=7, column=0)
    mk8cheat14 = Checkbutton(mk8, text="Speed Hack", width=20, onvalue=1, offvalue=0, variable=mk8checkbox14).grid(row=7, column=1)
    mk8cheat15 = Checkbutton(mk8, text="Disable speedhack", width=20, onvalue=1, offvalue=0, variable=mk8checkbox15).grid(row=7, column=2)        
    
    mk8separcheatinject = Label(mk8, text="").grid(row=8, column=0)
    
    mk8injectbtn = Button(mk8, text="Inject", command=mk8injectcommand).grid(row=9, column=1)
    
    copy = Label(mk8, text="Created by vincent-coding", width=25).grid(row=10, column=1)
    
    #End of MK8 Window
    mk8.mainloop()

#BOTW
def BOTWStart():
    tkinter.messagebox.showerror('UTrainers - '+version, 'Sorry but this trainers is not available yet.')

#SMMT
def SSMTStart():
    tkinter.messagebox.showerror('UTrainers - '+version, 'Sorry but this trainers is not available yet.')



# Start window
start = Tk()

#Window information
start.title("UTrainers - "+version)
largeur      = 300
hauteur      = 200
largeurEcran = start.winfo_screenwidth()
hauteurEcran = start.winfo_screenheight()
x            = (largeurEcran / 2) - (largeur / 2)
y            = (hauteurEcran / 2) - (hauteur /2)
start.geometry('%dx%d+%d+%d' % (largeur, hauteur, x, y))
start.resizable(width = False, height = False)

#Pop-up
tkinter.messagebox.showinfo("UTrainers - "+version, "Hey, welcome to UTrainers.\nThis software is created by vincent-coding.\n\nThis software is in alpha. It may have bugs. If you find any, you can contact me on Gbatemps.\n\nThis software aims to gather a lot of Trainers created in python by vincent-coding.\n\nHere is the list of trainers available.\nDarkU\nMarioKart8\nThe Legend Of Zelda BOTW\nSuper Mario Maker\nMore are to come.")

#Component
startDarkUbtn = Button(start, text="DarkU", width=25, command=DarkUStart).pack(pady=5)
startMK8btn = Button(start, text="MarioKart8 Trainers", width=25, command=Mk8Start).pack()
startBOTWbtn = Button(start, text="BOTW Trainers", width=25, command=BOTWStart).pack(pady=5)
startSMMTbtn = Button(start, text="Super Mario Maker Trainers", width=25, command=SSMTStart).pack()

copy = Label(start, text="Created by vincent-coding").pack(side=BOTTOM)

# End of the start window
start.mainloop()