import glob 
import string
import pandas as pd 
import spacy

def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
        text = text.replace("\n", '')
    return text

def return_sentences(poem): 
    with open(poem,'r') as poem:
        sentences = poem.readlines() #Adds lines from poem to list 
        poem_data = pd.DataFrame(sentences, columns= ['unclean_sentences']) #Converts list to data frame 
        
        poem_data['sentences'] = poem_data['unclean_sentences'].apply(remove_punctuations)
        poem_data = poem_data.drop(columns = ['unclean_sentences'])

        return poem_data

def create_data(folder): 
    poem_data = pd.DataFrame(columns = ['sentences', 'poem_ID'])

    path = folder
    poems = glob.glob(path + "/*.csv")

    poem_ID = 0 
    for poem in poems: 
        current_poem = return_sentences(poem) #temp dataframe that holds the current poem lines
        rows = current_poem.shape[0]
        total_rows = poem_data.shape[0]
        new_num_rows = total_rows + rows
        
        poem_data = pd.concat([poem_data, current_poem])

        poem_data['poem_ID'].iloc[total_rows: new_num_rows] = poem_ID
        poem_ID += 1 

        column_names = ["poem_ID","sentences"]
        poem_data = poem_data.reindex(columns=column_names)
        poem_data.reset_index(drop=True, inplace=True) 

        poem_data.to_csv("sentences_" + folder)

poem_data = create_data(folder = 'poem_database')

def write_poem(file, word, num_lines = 10): 
    # Load the English model from SpaCy
    nlp = spacy.load("en_core_web_lg")
    starter = nlp(word)
    
 