import glob 
import string
import random 
import pandas as pd 


def return_sentences(folder, split = "/n"): 
    path = folder
    poems = glob.glob(path + "/*.csv") #that gives you the name of all the poems within the data base 
    for poem in poems: 
        
    
return_sentences('poem_database')

# def read_poems(folder): 
#     #returns word bank from all the poems in our database 
#     word_bank = []
#     path = folder
#     poems = glob.glob(path + "/*.csv")
#     for poem in poems: 
#         word_bank.append(return_words(poem))

#     return word_bank

# def write_poem(): 
#     word_bank = read_poems('poem_database')
#     words = []
    
#     #change word bank list of lists into one flat, condensed list that contains all the words 
#     for sublist in word_bank: 
#         for word in sublist: 
#             words.append(word)

#     lines = 10 
#     words_per_line = 6
#     line = ""
#     for i in range(lines): 
#         line = ""
#         for j in range(words_per_line): 
#             line += random.choice(words) + " "
#         print(line)

# write_poem()


 