from matplotlib.font_manager import list_fonts
from model.word import Word
import random

class WordList:
    def __init__(self, wl_filepath):
        self.fp = wl_filepath
        self.list_of_temp_words = []
        self.stripped_list = []
        self.list_of_words = []
        self.list_of_5 = []
        self.list_of_6 = []
        self.list_of_7 = []
        self.list_of_8 = []
        self.make_word_list(self.fp)

    def make_word_list(self, fp):
        #generates initial list of words and the number of words 
        #between 5 and 8 letters inclusive
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
                #print(word)
                self.list_of_words.append(word)
                
        print('There are {} words in list_of_words'.format(len(self.list_of_words)))
        

    def shuffle(self):
        for i in range(len(self.list_of_words) -1, 0, -1):
            r = random.randint(0,i)
            self.list_of_words[i], self.list_of_words[r] = self.list_of_words[r], self.list_of_words[i]

    #def draw_word(self):
    #    return self.list_of_words.pop()

    def sort_by_length(self):
        for word in self.list_of_words:
            #print(word)
            if len(word) == 5:
                self.list_of_5.append(Word(word, len(word)))
            elif len(word) == 6:
                self.list_of_6.append(Word(word, len(word)))
            elif len(word) == 7:
                self.list_of_7.append(Word(word, len(word)))
            elif len(word) == 8:
                self.list_of_8.append(Word(word, len(word)))
            else:
                raise Exception("Word should not be in list")


    def show(self, wrdlen):
        #Used to display the entire list of words within each of the lists
        if wrdlen == 5:
            for l in self.list_of_5:
                l.show()
        elif wrdlen == 6:
            for l in self.list_of_6:
                l.show()
        elif wrdlen == 7:
            for l in self.list_of_7:
                l.show()
        elif wrdlen == 8:
            for l in self.list_of_8:
                l.show()
        else:
            raise Exception("Sorry not a valid number")


    def draw_word(self, wrdlen):
        if wrdlen == 5:
            return self.list_of_5.pop()
        elif wrdlen == 6:
            return self.list_of_6.pop()
        elif wrdlen == 7:
            return self.list_of_7.pop()
        elif wrdlen == 8:
            return self.list_of_8.pop()
        else:
            raise Exception("Sorry not a valid number")



