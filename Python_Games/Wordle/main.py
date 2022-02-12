from model.word_list import WordList
from model.word import Word

word_list_filepath = 'c:/Users/chand/Documents/Python_Coding_Projects/Python_Games/Wordle/resources/words.txt'
wl1 = []
word = Word

wl1 = WordList(word_list_filepath)
#wl1.make_word_list()

wl1.shuffle()
word = wl1.drawWord()
word.show()


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