from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import os

class Model(object):

    def __init__(self):
        #  initiate feature variables
        self.X = []
        self.y = []
        self.genre = {}
        self.X_dtm = ''
        self.vect = CountVectorizer()
        self.nb = MultinomialNB()


    def manipulateSong(self):
        """This manipulates the Songs in the lyric directory and creates a documated term matrix"""
        lyric_folder = 'lyrics'
        os.chdir(lyric_folder)
        self.X = []
        self.y = []
        self.genre = {}
        num = 0
        list_of_genre = os.listdir(os.getcwd())  # lists all the genres in the directories
        for folders in list_of_genre:
            self.genre[str(num)] = folders
            os.chdir(folders)
            list_files = os.listdir(os.getcwd())
            for files in list_files:
                f = open(files, 'r')
                data = f.read().replace('\n', ' ')
                self.X.append(data)
                self.y.append(num)
                f.close()
            num += 1
            os.chdir("..")
        os.chdir("..")
        self.vect.fit(self.X)
        self.X_dtm = self.vect.transform(self.X)

    def model(self):
        """This creates the naive bayse model from the doccument term matrix"""
        self.nb.fit(self.X_dtm, self.y)

    def guess(self,X_test):
        """Takes input of a string of lyrics and transforms the data into a document term matrix. Then it predicts
        what genre the song is."""
        X_test = self.vect.transform(X_test)
        result = self.nb.predict(X_test)

        index = result.item(0)
        genre = self.genre.get(str(index))
        return genre




