import tkinter as tk
from tkinter import *
from lyrics_extractor import SongLyrics

window = Tk()
window.geometry('600x600')
window.title('PythonGeeks')
head=Label(window, text="Enter the song you want Lyrics for", font=('Calibri 15'))
head.pack(pady=20)
result =tk.StringVar()
song=tk.StringVar()
def get_lyrics():
    song_name=song.get()
    api_key = "AIzaSyAcZ6KgA7pCIa_uf8-bYdWR85vx6-dWqDg"
    engine_id = "aa2313d6c88d1bf22"
    extract_lyrics = SongLyrics(api_key, engine_id)
    song_lyrics = extract_lyrics.get_lyrics(song_name)
    result.set(song_lyrics)

Entry(window, textvariable=song).pack()
Message(window,textvariable=result, bg="light grey").pack(side=TOP,anchor=W,fill=BOTH, expand=1)
Button(window, text="GO",command=get_lyrics).pack()

window.mainloop()