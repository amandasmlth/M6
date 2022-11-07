import glob 
import string
import random 

def return_words(poem): 
    poem_words = []
    words = []
    with open(poem,'r') as poem:
        poem_words = poem.read().split() #adds all individual words into one list per poem 
        for word in poem_words: 
            for character in string.punctuation:
                word = word.replace(character, '')  
            words.append(word)
    return words

def read_poems(folder): 
    #returns word bank from all the poems in our database 
    word_bank = []
    path = folder
    poems = glob.glob(path + "/*.csv")
    for poem in poems: 
        word_bank.append(return_words(poem))

    return word_bank

def write_poem(): 
    word_bank = read_poems('poem_database')
    print(word_bank)

    lines = 10 
    words_per_line = 6
    for i in range(lines): 
        for j in range(words_per_line): 
            random.choice(word_bank)


write_poem()


 