# Visual Representation of Maya Angelou's Powerful Language - Amanda Smith  
# DESCRIPTION: 
Maya Angelou served our world as an acclaimed poet and story teller from 1928 - 2014, but the meaning behind her words and the strength of her actions have continued beyond her lifetime. Maya's poems have always moved me, especially lines from "The Human Family" and "I Know Why the Caged Bird Sings". When Professor Harmon and I talked several weeks ago about how to approach M6, we discussed two routes: the machine learning/AI one or deep diving into Maya Angelou as an author. Given my previous courses in the computer science department, namely FML and AI, the former path would have been the more comfortable option. However, since our course centers around creativity, the second option was more appealing. When researching Maya Angelou, I discovered that after being raped by her mother's boyfriend when she was only seven years old, her uncle killed him. Maya felt responsible for those events and became purposefully mute for the next five years, but fell in love with poetry. Second, her poems are not celebrated for their poetic virtue or artistic prose, but rather the words and language that have such power and tie into greater themes like Black beauty, women empowerment, and human strength and resiliency. Given Maya chose not to speak for five years, it was important to me that my poem generator spoke in the voice of a woman (although apple has not added Black female voices yet), have some visual component, and focus on the words she chooses rather than the poems themselves. That made me think about how to display her words visually, find the most relevant and meaningful words, and research word clouds and frequency maps. 

The system currently reads in 23 Maya Angelou poems from the insprining set, creates one word bank that contains all the lowercase and semantically significant words, constructs and outputs the word cloud, prompts the user for how many words they want the cloud to contain, evaluates the cloud for similiarity to her overarching themes, and saves the word cloud to .png file. 

# SET UP AND RUN: 
Changes you may need to make ahead of time: the themes you believe are evident within Maya's poems (you can find that list in the evaluate_poem method), the folder/data base the system pull poems from (you can also web scrape or add more poems there), and then be aware that when prompted for the number of words you want in the word cloud - that should be between 0 - 100. Run the program using the "compile button" on the top right-hand corner for the VS Code IDE. Then enter the number of words you want represented in the word cloud. Then listen for the words the cloud chooses are most frequent and therefore valuable. The choice to have the woman read out the words before the word cloud poped up was deliberate because I wanted the audiance to consider for themselves which words they felt were most relevant, powerful, or frequent before the word cloud was generated. Make sure you consider the themes that we know Maya Angelou cared to express within her poetry before seeing the word cloud and comparing those expectations to the final result. Word clouds lended themselves so well to my goals because they show the words and phrases that mattered enough to Maya Angelou she weaved them through many of her poems.  
 
# CHALLENGE: 
Have done very little work with computer graphics, text to speech converters, and matching similarities between lists of words; M6 taught me that you have to know what problem you want to solve before you start writing code. That was crucial to my creativity and eventual success. Over the last couple weeks, I learned how to use spaCy, NLTK, and other natural language processors in Python and was experimenting with how to link words and sentences together based on grammar and parts of speech, but because Maya Angelou had such free form poetry style and cared about broad themes and specific words, realized the program should represent the things that mattered to her. The words should be celebrated as individuals that have stand alone meaning. As my progress continued, more ideas came up but were hard to implement. For example, word clouds allow you to add "masks" which means the words can take on shapes that you enter to the program. I expeimented with alligning the words in her silhouette, her name in large block letters, and based on the word that had the most frequency and with more time maybe that would have been possible. M6 also challenged me because we had so much freedom especially in terms of what defines an actual poem, but the final result feels unique and captures Maya Angelou's essense. 

# NOTE: 
In your rubric, you mention "the system must: save its work so that it can re-perform any previously-generated pieces you found particularly interesting". Whenever you run the main method for my system, despite my attempts, the word cloud will override the png file and refresh word count selections from the user instead of saving them. However, the system always creates the same word cloud for the same input (with different artistic configurations) so whenever you want the same words generated, type the same word count. For example, the word cloud will generate the same list of 50 words whenever 50 is the input. 

# RESEARCH PAPERS: 
(1) Development of Word Cloud Generator Software Based on Python by Yuping Jin
Found this paper when scrolling through journal articles and this served as the inspiration for my entire poem generator system. Jin argued that word clouds allow people to understand the most essential words within some data set and are weighted visual representations of those intentions. 
https://www.sciencedirect.com/science/article/pii/S1877705817302230

(2) A Speech Recognized Dynamic Word Cloud Visualization for Text Summarization by Kayal Padmanandam, Sai Priya V D S Bheri, LaxmiHarshika Vegesna, and Kalakuntla Sruthi
Paper talked about how word clouds are graphic representations of the words within some bank that have the highest frequency. Stopwords/filled words should be removed from your text corpus before creating the frequency map for the word cloud. 
https://ieeexplore.ieee.org/abstract/document/9358693

(3) Semantic Cosine Similarity by Faisal Rahutomo, Teruaki Kitasuka, and Masayoshi Aritsugi from the Graduate School of Science and Technology, Kumamoto University
Taught me about semantic similarity between words and how you could then compute cosine similiarity between two word banks/lists which ended up being how my program evaluated itself. 
https://www.researchgate.net/profile/Faisal-Rahutomo/publication/262525676_Semantic_Cosine_Similarity/links/0a85e537ee3b675c1e000000/Semantic-Cosine-Similarity.pdf

# WORKS CITED
https://www.datacamp.com/tutorial/wordcloud-python

https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/voiceattributekey

https://techtutorialsx.com/2017/05/06/python-pyttsx-changing-speech-rate-and-volume/

https://realpython.com/nltk-nlp-python/

https://mypoeticside.com/poets/maya-angelou-poems
(pulled inspiring set poems from here)

https://www.poetryfoundation.org/poets/maya-angelou







