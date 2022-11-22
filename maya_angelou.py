import glob 
import string
from wordcloud import WordCloud
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import pyttsx3
from collections import Counter
import math

def return_words(poem): 
    poem_words = []
    words = []
    with open(poem,'r') as poem:
        poem_words = poem.read().split()
        tokens = [word for word in poem_words if not word.lower() in stopwords.words()] #removes stop words from word bank  
        for word in tokens: 
            for character in string.punctuation:
                word = word.replace(character, '')  
            words.append(word.lower())
    return words

def read_poems(folder): 
    #returns word bank from all the poems in our database 
    word_bank = []
    path = folder
    poems = glob.glob(path + "/*.csv")
    for poem in poems: 
        word_bank.append(return_words(poem))

    return word_bank

def flatten_word_bank(folder):
    word_bank = read_poems(folder) 
    return [word for sublist in word_bank for word in sublist]

def word_cloud(folder, word_count): 
    words = ""
    word_bank = flatten_word_bank(folder)
    
    for word in word_bank: 
        words = words + ' ' + word.replace("’", "")

    wordcloud = WordCloud(width=3000, height=2000,
                            colormap = 'Set2',
                            max_words=word_count, 
                            background_color="black").generate(words)
    return wordcloud

def create_cloud(folder, word_count): 
    wordcloud = word_cloud(folder, word_count)

    common_words = wordcloud.words_.keys()
    poem = ""
    for word in common_words:
        poem += word + "," 
    
    converter = pyttsx3.init()
    converter.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    converter.say(poem)
    converter.runAndWait()

    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()
    wordcloud.to_file('word_cloud.png')

def evaluate_poem(folder, word_count): 
    poem_words = Counter(word_cloud(folder, word_count).words_.keys())
    themes = Counter(['love', 'gender', 'black', 'rise', 'today', 'sing', 'freedom', 'race', 'loss', 'struggle'])
    all_words = set(poem_words).union(themes)
    
    # adapted from: https://stackoverflow.com/questions/55162668/calculate-similarity-between-list-of-words
    dotprod = sum(poem_words.get(value, 0) * themes.get(value, 0) for value in all_words)
    magA = math.sqrt(sum(poem_words.get(value, 0)**2 for value in all_words))
    magB = math.sqrt(sum(themes.get(value, 0)**2 for value in all_words))
    return round((dotprod / (magA * magB)) * 100)

def main(folder = "poem_database"): 
    num_words = int(input("How many words do you want shown in the world cloud? "))
    cosine_similarity = evaluate_poem(folder, num_words)
    print("The word cloud has", cosine_similarity, "cosine similarity with the themes of Maya Angelou's poems.")
    create_cloud(folder, num_words)

if __name__ == "__main__":
    main()