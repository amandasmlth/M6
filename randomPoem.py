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
    words = []
    
    #change word bank list of lists into one flat, condensed list that contains all the words 
    for sublist in word_bank: 
        for word in sublist: 
            words.append(word)

    lines = 10 
    words_per_line = 6
    line = ""
    for i in range(lines): 
        line = ""
        for j in range(words_per_line): 
            line += random.choice(words) + " "
        print(line)

write_poem()


 