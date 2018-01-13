import os
from tkinter import *

from model import Model

class Login(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Guess the Song")
        self.grid()
        self.grid(sticky=W + E + N + S)

        self._image = PhotoImage(file="music.png")

        self.model = Model()
        self.model.manipulateSong()
        self.model.model()

        # Data containers
        self._statusVar = StringVar()
        self._image = PhotoImage(file="music.png")
        self.title = StringVar()
        self.artist = StringVar()
        self.lyrics = StringVar()
        self.genre = StringVar()

        # Labels for entry fields
        self._imageLabel = Label(self, image=self._image)
        self._imageLabel.grid(row=0, column=0)

        self.nameLabel = Label(self,text = "Song Title")
        self.nameLabel.grid(row =1, column = 0)
        self.ArtistLabel = Label(self, text="Artist Name")
        self.ArtistLabel.grid(row=2, column=0)
        self.lyricLabel = Label(self, text="Lyrics")
        self.lyricLabel.grid(row=3, column=0)

        self.genreLabel = Label(self, text="Genre")
        self.genreLabel.grid(row=5, column=0)

        # entry fields
        self.nameEntry = Entry(self,textvariable = self.title)
        self.nameEntry.grid(row=1,column = 1)
        self.artistEntry = Entry(self, textvariable=self.artist)
        self.artistEntry.grid(row=2, column=1)
        self.lyricEntry = Entry(self, textvariable=self.lyrics)
        self.lyricEntry.grid(row=3, column=1)
        self.genreEntry = Entry(self, textvariable=self.genre)
        self.genreEntry.grid(row=5, column=1)

        # command buttons
        self._submit = Button(self,text = "Submit", command = self.runcommand)
        self._submit.grid(row = 4, column = 1)

        # Create the nested frame for the data pane
        self._dataPane = Frame(self)
        self._dataPane.grid(row=6, column=1)

        # Create and add buttons to button pane
        self.button1 = Button(self._dataPane, text="Correct", command=self.correct_button )
        self.button2 = Button(self._dataPane, text="Incorrect", command=self.incorrect_button )
        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)

    def runcommand(self):
        """This performs a a guess using the guess method from """
        lyrics =['']
        lyrics[0] = self.lyrics.get()
        self.genre.set(self.model.guess(lyrics))

    def correct_button(self):
        """Event handler for the correct button"""
        self.genre.set("Yay, it's correct!")

    def incorrect_button(self):
        """Event handler for the incorrect button"""
        self.genre.set("Sorry, it's incorrect.")


def main():
    Login().mainloop()
main()
