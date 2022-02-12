from model.word import Word
import random

class WordList:
    def __init__(self, wl_filepath):
        self.fp = wl_filepath
        self.list_of_temp_words = []
        self.stripped_list = []
        self.list_of_words = []
        self.make_word_list(self.fp)

    def make_word_list(self, fp):
        with open(fp, 'r') as fh:
            Lines = fh.readlines()
            for line in Lines:
                self.list_of_temp_words.append(line)
            #print(self.list_of_temp_words)
            fh.close()
    
        for word in self.list_of_temp_words:
            self.stripped_list.append(word.strip())

        for word in self.stripped_list:
            if not ((len(word) < 5) or (len(word) > 8)):
                #removes all words that are not 5, 6, 7, or 8 letters long
                self.list_of_words.append(Word(word, len(word)))
        
    def show(self):
        for l in self.list_of_words:
            l.show()

    def shuffle(self):
        for i in range(len(self.list_of_words) -1, 0, -1):
            r = random.randint(0,i)
            self.list_of_words[i], self.list_of_words[r] = self.list_of_words[r], self.list_of_words[i]

    def drawWord(self):
        return self.list_of_words.pop()