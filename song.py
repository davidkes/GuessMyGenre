"""
Program: song.py

This creates the Song class with attributes of Song title, lyric, genre, published date, and song length
"""
from artist import Artist

class Song(object):

    def __init__(self):
        self.title = ''
        self.lyric = ''
        self.genre = ''
        self.published = ''
        self.length = ''

    def getTitle(self):
        """ returns title of song"""
        return self.title

    def getLyric(self):
        """returns the lyric of the song"""
        return self.lyric

    def getGenre(self):
        """returns the genre of the song"""
        return self.genre

    def getPublished(self):
        """returns the pubslished date of the song"""
        return self.published

    def setTitle(self, title):
        """sets the song title"""
        self.title = title

    def setLyric(self, lyric):
        """sets the song lyric"""
        self.lyric = lyric

    def setGenre(self, genre):
        """sets the genre of the song"""
        self.genre = genre

    def setPublished(self, date):
        """sets the published date of the song"""
        self.published = date

    def set(self, length):
        """sets the length of the song"""
        self.length = length
