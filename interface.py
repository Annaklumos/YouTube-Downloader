import tkinter as tk
import sys
from pytube import YouTube
from os import startfile

def get_url(event):
    yt = YouTube(url.get())
    stream = yt.streams.filter(file_extension='mp4').all()[0]
    stream.download()
    startfile(f"{yt.title}.mp4")
    root.destroy()
    sys.exit()

root = tk.Tk()

message = tk.Label(root, text="Enter YouTube URL:")
message.pack() # pack() places the widget in the root window

# create a text entry box
# and bind it to the enter key
url = tk.Entry(root)
url.bind("<Return>", get_url)
url.pack()



root.mainloop()