
class Word:
    def __init__(self, word, length):
        self.leng = length
        self.word = word

    def show(self):
        print("{} : {} letters".format(self.word, self.leng))

    def get_word(self):
        return self.word
