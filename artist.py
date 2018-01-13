"""
Program: artist.py

This creates the artist class that inherits the person class from person.py with additional attributes such as
starting year, active status, and genre

"""
from person import Person

class Artist(object):

    def __init__(self):
        self.startingYear = ''
        self.status = False
        self.genre = ''

    def getStartingYear(self):
        """returns the starting year of artist"""
        return self.startingYear

    def getStatus(self):
        """returns whether the artist is still active or not"""
        if self.status:
            return "This person still has an active career"
        else:
            return "This person no longer is active in his career"

    def getGenre(self):
        """returns the genre the artist"""
        return self.genre

    def setStartingYear(self, year):
        """sets when the artist started"""
        self.startingYear = year

    def setStatus(self, status):
        """sets the status of the artist as a boolean"""
        self.status = status

    def setGenre(self,genre):
        """sets the genre of the artist"""
        self.genre = genre
