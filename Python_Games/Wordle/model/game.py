from model.word_list import WordList

class Game:
    def __init__(self, fp):
        self.filepath = fp
        self.alphabet = ['a','b','c','d','e','f','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.curr_guess_counter = 0
        self.target_word = ''
        self.target_word_list = []
        self.curr_guess = ''
        self.curr_guess_list = []
        self.return_list = []
        self.guess_holder = []
        self.return_holder = []

    def get_word(self):
        wl1 = WordList(self.filepath)
        inp = input('Enter desired word length: ')
        wl1.shuffle()
        wl1.sort_by_length()
        word = wl1.draw_word(int(inp))
        word.show()
        self.target_word = word.get_word()

    def split_word_list(self):
        for each in self.target_word:
            self.target_word_list.append(each)
        print(self.target_word_list)

    def get_guess(self, guess):
        for each in guess:
            self.curr_guess_list.append(each)
        #print(self.curr_guess_list)

    def compare_guess(self):
        x = 0
        y = 0
        for _ in self.target_word_list:
            self.return_list.append('-')

        #print(self.return_list)

        for i in self.curr_guess_list:
            if i in self.target_word_list:
                #print('\nThe letter {} is in the word.'.format(i))
                self.return_list[y] = self.curr_guess_list[y]

            y += 1

        for i in self.curr_guess_list:
            if self.curr_guess_list[x] == self.target_word_list[x]:
                #print('\nMatch at letter: {}.'.format(x + 1))
                self.return_list[x] = self.target_word_list[x].upper()
            
            x += 1

        print('\n{}'.format(self.return_list))

        self.guess_holder = self.curr_guess_list
        self.return_holder = self.return_list

        self.return_list = []
        self.curr_guess_list = []

    def is_game_terminated(self):
        game_status = False
        z = 0
        for _ in self.guess_holder:
            self.guess_holder[z] = self.guess_holder[z].upper()
            z += 1
        #print('{} : {}'.format(self.guess_holder, self.return_holder))
        if self.guess_holder == self.return_holder:
            game_status = True
        return game_status




        
