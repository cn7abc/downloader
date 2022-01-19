# gui to use yt-dl & ffmpeg
# Jacob Rogers
# 12-4-21

from ast import arg
from tkinter import *
import tkinter as tk
import os
from os import path, stat
from tkinter.font import BOLD
import threading

def runYTDL_audio(url, mode, start_time, end_time):
    dir = os.getcwd()

    if(path.exists("audio_files") == FALSE):
        os.system("mkdir audio_files")
    os.chdir("audio_files")

    if(mode == 'Turn Off'):
        os.system("youtube-dl --external-downloader ffmpeg --external-downloader-args \"-ss " + start_time + ".00 -to " + end_time + ".00\" " + "-f best -x --audio-format wav \"" + url + "\"")
    else:
        os.system("youtube-dl -x --audio-format wav " + url)

    os.chdir(dir)

def runYTDL_video(url, mode, start_time, end_time):
    dir = os.getcwd()

    if(path.exists("video_files") == FALSE):
        os.system("mkdir video_files")
    os.chdir("video_files")

    if(mode == 'Turn Off'):
        os.system("youtube-dl --external-downloader ffmpeg --external-downloader-args \"-ss " + start_time + ".00 -to " + end_time + ".00\" " + "-f best \"" + url + "\"")

    else:
        os.system("youtube-dl " + url)

    os.chdir(dir)

def toggle_time_mode():
    if(time_mode_button.cget('text') == 'Turn On'):
        time_mode_button.config(text='Turn Off')
        time_start_text.config(state=NORMAL)
        time_end_text.config(state=NORMAL)
        time_end_text.config(bg='white')
        time_start_text.config(bg='white')
    else:
        time_mode_button.config(text='Turn On')
        time_start_text.config(state=DISABLED)
        time_end_text.config(state=DISABLED)
        time_end_text.config(bg='grey')
        time_start_text.config(bg='grey')
        time_start_text.insert("1.0","00:00:00")
        time_end_text.insert("1.0","00:00:00")

def loading(state):
    if(state == True):
        urlText.delete("1.0","end")
        urlText.insert("1.0","LOADING, please wait...")
        time_mode_button["state"] = DISABLED
        process_audio["state"] = DISABLED
        process_video["state"] = DISABLED
        urlText.config(state=DISABLED)
        urlText.config(bg='grey')
    else:
        urlText.delete("1.0","end")
        time_mode_button["state"] = NORMAL
        process_audio["state"] = NORMAL
        process_video["state"] = NORMAL
        urlText.config(state=NORMAL)
        urlText.config(bg='white')
        


if __name__ == "__main__":
    
    root = Tk()

    root.configure(background='pink')
 
    root.title("Downloader")
 
    root.geometry("400x175")
 
    urlLabel = Label(root, text="URL", font=BOLD, bg="pink")
    time_start_label = Label(root, text="Start Time",bg='pink')
    time_end_label = Label(root, text="End Time",bg='pink')
    time_mode_text = Label(root,text="Toggle Time Mode",bg='pink')

    urlLabel.grid(row=1, column=1)
    time_start_label.grid(row=6, column=1)
    time_end_label.grid(row=7,column=1)
    time_mode_text.grid(row=8,column=1)

    urlText = Text(root,height=1,width=10)
    time_start_text = Text(root,height=1,width=8,bg="grey")
    time_start_text.insert("1.0","00:00:00")
    time_start_text.config(state=DISABLED)
    time_end_text = Text(root,height=1,width=8,bg="grey")
    time_end_text.insert("1.0","00:00:00")
    time_end_text.config(state=DISABLED)
    

    urlText.grid(row=1, column=2, ipadx="100")
    time_start_text.grid(row=6,column=2)
    time_end_text.grid(row=7,column=2)

    time_mode_button = Button(root, text='Turn On',fg="Black",bg="light Blue", command=toggle_time_mode)
    time_mode_button.grid(row=8,column=2,pady=10)
    
    process_audio = Button(
        root, 
        text="Get Audio", 
        fg="Black",
        bg="light Blue", 
        command= lambda :  runYTDL_audio(urlText.get("1.0","end-1c"), time_mode_button.cget('text'), time_start_text.get("1.0","end-1c"), time_end_text.get("1.0","end-1c"))
    )

    process_audio.grid(row=4, column=2)

    process_video = Button(
        root, 
        text="Get Video", 
        fg="Black",bg="light Blue", 
        command= lambda :  runYTDL_video(urlText.get("1.0","end-1c"), time_mode_button.cget('text'), time_start_text.get("1.0","end-1c"), time_end_text.get("1.0","end-1c"))
    )

    process_video.grid(row=5,column=2,pady=5)

    root.mainloop()
    
