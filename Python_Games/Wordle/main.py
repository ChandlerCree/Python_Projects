from model.game import Game
from view.board_console_view import BoardConsoleView
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController

#filepath for list of initial words
word_list_filepath = 'c:/Users/chand/Documents/Python_Coding_Projects/Python_Games/Wordle/resources/words.txt'

game = Game(word_list_filepath)

board_view = BoardConsoleView(game)
game_view = GameConsoleView(board_view)

controller = GameController(game, game_view)
controller.run_game()
















































'''
#generates Word object
word = Word

#generates WordList object
wl1 = WordList(word_list_filepath)

#get input from console for desired word length
inp = input('Enter desired word length: ')

#shuffle the word list
wl1.shuffle()

#sort the word list by word length
wl1.sort_by_length()

#prints entire list of value (inp) to console
#wl1.show(int(inp))

#draws a word from the top of the list of words len(inp)
word = wl1.draw_word(int(inp))

#shows the word to console
word.show()

print('\n\n\n\n')
print('Game Starting!\n')
'''






'''
count = 0
list_of_temp_words = []
stripped_list = []
list_of_words = []

with open('c:/Users/chand/Documents/Python_Coding_Projects/Python_Games/Wordle/resources/temp_words.txt', 'r') as fh:
    #reads file line by line and appends words to list of temp words

    Lines = fh.readlines()
    for line in Lines:
        list_of_temp_words.append(line)
    print(list_of_temp_words)
    fh.close()

for word in list_of_temp_words:
    stripped_list.append(word.strip())

for word in stripped_list:
    count += 1
    #print(line)
    #print(len(line) - 1)

    if not (((len(word) - 1 ) < 5) or ((len(word) -1 ) > 8)):
        #removes all words that are not 5, 6, 7, or 8 letters long
        list_of_words.append(word)
    

print(list_of_words)

'''