import glob 
import string
from wordcloud import WordCloud
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import pyttsx3
from collections import Counter
import math

def return_words(poem): 
    """
    Returns cleaned word list for an individual poem (csv file). 
    """
    poem_words = []
    words = []
    with open(poem,'r') as poem:
        poem_words = poem.read().split()
        # removes stop words (for example: and, then, or) from the word bank 
        # because they are not meaningful for the word cloud 
        tokens = [word for word in poem_words if not word.lower() in stopwords.words()]  
        for word in tokens: 
            for character in string.punctuation:
                # removes punctuation (for example: !, \, ., %) from each word
                word = word.replace(character, '')  
            words.append(word.lower())
    return words

def read_poems(folder): 
    """
    Returns word bank list containing all the words from our inspiring set 
    poems and calls the return_words method.  
    """
    word_bank = []
    path = folder
    # read all the files from the folder that are .csv 
    poems = glob.glob(path + "/*.csv")
    for poem in poems: 
        word_bank.append(return_words(poem))

    return word_bank

def flatten_word_bank(folder):
    """
    Creates one list from list of lists and returns the flattened list. 
    """
    word_bank = read_poems(folder) 
    return [word for sublist in word_bank for word in sublist]

def word_cloud(folder, word_count): 
    """
    Returns the wordcloud from the WordCloub Python library based on the word bank 
    which has been converted to one, long string. 
    """
    words = ""
    word_bank = flatten_word_bank(folder)
    
    # remove apostrophes from words like it's because the word cloud thought 
    # the "s" was an individual, frequent word and showed that much larger than other texts
    for word in word_bank: 
        words = words + ' ' + word.replace("’", "")

    # create word cloud - opportunity to change parameters here 
    wordcloud = WordCloud(width=3000, height=2000,
                            colormap = 'Set2',
                            max_words=word_count, 
                            background_color="black").generate(words)
    return wordcloud

def create_cloud(folder, word_count): 
    """
    Creates and saves the word cloud. Coverts text to speech using female
    narration through the pyttsx3 module. 
    """
    wordcloud = word_cloud(folder, word_count)

    common_words = wordcloud.words_.keys()
    poem = ""
    # word cloud takes in one long string containing all words seperated by spaces
    # added commas between words because that slowed down the narrator for text to speech 
    for word in common_words:
        poem += word + "," 
    
    # create text to speech converter 
    converter = pyttsx3.init()
    # can add any voice, chose Samantha because hers was most similiar to Maya Angelou 
    converter.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    converter.say(poem)
    converter.runAndWait()

    # shows the word cloud
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()

    # saves word cloud to .png file 
    wordcloud.to_file('word_cloud.png')

def evaluate_poem(folder, word_count):
    """
    Evaluates how similar the word cloud words are to the themes across Maya Angelou's 
    poetry by computing cosine similiarity.  
    """
    # gathers the words from the word cloud 
    poem_words = Counter(word_cloud(folder, word_count).words_.keys())
    # common themes across the poem data base 
    themes = Counter(['love', 'gender', 'black', 'rise', 'today', 'sing', 'freedom', 'race', 'loss', 'struggle'])
    # set that contains all unique words from both lists 
    all_words = set(poem_words).union(themes)
    
    # code adapated from: https://stackoverflow.com/questions/55162668/calculate-similarity-between-list-of-words
    dotprod = sum(poem_words.get(value, 0) * themes.get(value, 0) for value in all_words)
    vector_a = math.sqrt(sum(poem_words.get(value, 0)**2 for value in all_words))
    vector_b = math.sqrt(sum(themes.get(value, 0)**2 for value in all_words))
    return round((dotprod / (vector_a * vector_b)) * 100)

def main(folder = "poem_database"): 
    """
    Prompts user for the number of words they want for the word cloud, 
    creates the cloud, and narrates the words represented.  
    """
    # good input range: 30 - 60 words 
    num_words = int(input("How many words do you want shown in the world cloud? "))
    cosine_similarity = evaluate_poem(folder, num_words)
    # measure for evaluating how similiar the themes and final word cloud are to each other 
    print("The word cloud has", cosine_similarity, "cosine similarity with the themes of Maya Angelou's poems.")
    create_cloud(folder, num_words)

if __name__ == "__main__":
    main()