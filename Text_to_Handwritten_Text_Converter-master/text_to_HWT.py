from PIL import ImageTk
import PIL.Image
import tkinter as tk
import pywhatkit as kit
from tkinter import *
from tkinter import colorchooser
from tkinter.ttk import Progressbar
import time
import datetime
from threading import *
from pathlib import Path
import os

## To create 'results' directory if not exist
repn = Path('results')
if repn.is_dir():
    pass
else:
    os.mkdir('results')

windo = Tk()
windo.configure(background='black')
windo.title("Text to Handwritten Text Converter App")
width  = windo.winfo_screenwidth()
height = windo.winfo_screenheight()
windo.geometry(f'{width}x{height}')
windo.iconbitmap('./meta/app.ico')
# windo.resizable(0,0)
color_result_rgb = [0,0,0]

def threading():
    # Call work function
    t1=Thread(target=convert_txt_to_HW)
    t1.start()

def convert_txt_to_HW():
    text = txt2.get("1.0",END)
    ts = time.time()
    dat = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStam = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStam.split(":")
    fileN = "./results/" + dat + "_" + Hour + "-" + Minute + "-" + Second + ".png"
    img_txt = kit.text_to_handwriting(text,fileN,rgb = color_result_rgb)

    def bar():
        progress['value'] = 20
        windo.update_idletasks()
        time.sleep(1)
        progress['value'] = 40
        windo.update_idletasks()
        time.sleep(1)
        progress['value'] = 60
        windo.update_idletasks()
        time.sleep(1)
        progress['value'] = 80
        windo.update_idletasks()
        time.sleep(1)
        progress['value'] = 100
        windo.update_idletasks()
        progress.destroy()

    progress = Progressbar(windo, orient=HORIZONTAL, length=100, mode='determinate')
    progress.place(x=770, y=652)
    bar()

    conv_text_lbl.config(text="Handwritten Text", width=15, height=2, fg="#00FF89", bg="blue",
                             font=('segou UI', 16, ' bold'))
    conv_text_lbl.place(x=990, y=157)

    im2 = PIL.Image.open(fileN)
    im2 = im2.resize((887, 402), PIL.Image.ANTIALIAS)
    sp_img2 = ImageTk.PhotoImage(im2)
    panel6.config(image=sp_img2)
    panel6.image = sp_img2
    panel6.pack()
    panel6.place(x=1005, y=237)

def destroy_widget(widget):
    widget.destroy()

def clear_txt():
    txt2.delete("1.0",END)

def color_choose():
    global color_result_rgb
    color_code = colorchooser.askcolor(title ="Choose color")
    color_result_rgb = ' '.join(str(int(x)) for x in color_code[0])
    color_result_rgb = color_result_rgb.split(' ')
    # color_tup = tuple(color_result_rgb)

    color_tup = [int(item) for item in color_result_rgb]
    color_tup = tuple(color_tup)
    print(color_tup)
    colordis_lbl.configure(bg = _from_rgb(color_tup))
    colordis_lbl.place(x=680, y=652)

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

title = tk.Label(windo, text="Text to Handwritten Text Converter", width=56, height=2, fg="#00FF89",bg="#8B13F3",
                font=('segou UI', 28, ' bold italic'))
title.place(x=0, y=20)

enter_text_lbl = tk.Label(windo, text="Enter your text", width=15, height=2, fg="#00FF89",bg="blue",
                font=('segou UI', 16, ' bold'))
enter_text_lbl.place(x=10, y=170)

im1 = PIL.Image.open('./meta/writing.png')
im1 =im1.resize((150,110), PIL.Image.ANTIALIAS)
sp_img = ImageTk.PhotoImage(im1)
panel5 = Label(windo,borderwidth=0, image=sp_img,bg = '#8B13F3')
panel5.pack()
panel5.place(x=315, y=30)

txt2_border = Frame(windo,borderwidth = 3, background="#8B13F3")
txt2 = tk.Text(txt2_border,borderwidth = 1, width=70,height=13, bg='black', fg="white", font=('times', 13, ' bold '))
txt2.pack(padx=1, pady=1)
txt2_border.place(x=30, y=235)

conv_border = Frame(windo,borderwidth = 2, background="#8B13F3")
conv= Button(conv_border,text='Convert Text',command = threading, bg='black', fg="#00FF89", font=('times', 15, ' bold '),activebackground = "#00FF89")
conv.pack(padx=1, pady=1)
conv_border.place(x=30, y=650)

clear_border = Frame(windo,borderwidth = 2, background="#8B13F3")
clear = Button(clear_border,text='Clear Text',command = clear_txt, bg='black', fg="#00FF89", font=('times', 15, ' bold '),activebackground = "#00FF89")
clear.pack(padx=1, pady=1)
clear_border.place(x=255, y=650)

color_border = Frame(windo,borderwidth = 2, background="#8B13F3")
color = Button(color_border,text='Choose Color',command = color_choose, bg='black', fg="#00FF89", font=('times', 15, ' bold '),activebackground = "#00FF89")
color.pack(padx=1, pady=1)
color_border.place(x=445, y=650)

colordis_lbl = tk.Label(windo, width=6, height=2, fg="#00FF89",bg="green")

panel6 = Label(windo,borderwidth=0)

conv_text_lbl = tk.Label(windo, text="Enter your text", width=15, height=2, fg="#00FF89",bg="blue",
                font=('segou UI', 16, ' bold'))

windo.mainloop()