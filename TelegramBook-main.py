import nltk
import numpy as np
import random
from nltk.tokenize import word_tokenize as tok
import string

import re
import emoji
import sys


''' Set Input Text '''
# set text length
gen_text_lenght = 50000
# set input chat
input_Chat = 'data/Input_all.txt'


''' Remove Emojis '''

def strip_emoji(text):
    #print(emoji.emoji_count(text))
    new_text = re.sub(emoji.get_emoji_regexp(), r'', text)
    return  new_text

with open(input_Chat, 'r') as infile:
    old_text = None
    old_text = infile.read()
no_emoji = None
no_emoji = strip_emoji(old_text)

with open('data/cleanedInput.txt', 'w') as outfile:
    outfile.write(no_emoji)


# take text without emojis and remove special chars
with open('data/cleanedInput.txt', 'r') as f:
    text = f.read()
    # Text reinigen
    text = re.sub(r'http\S+', '', text) # Links
    text = re.sub('OneLove', '', text) # Schlachtruf Xavier
    text = re.sub('@xavier_naidoo', '', text) # Verlinkung Xavier Naidoo
    text = re.sub(r'[^\w\s]', '', text) # Sonderzeichen entferne


''' tokenize Input '''

token = tok(text)
print('Number of tokens:',len(token), '\n')
#print(token[:10])


''' get Vocabulary for generated text '''
vocabulary = {}

# Loop through all tokens (except the last one).
u = 0
for i in range(len(token) - 1):
    # The current token is key
    key = token[i]
    # The next token is the assigned value.
    value = token[i + 1]

    # Check if the key is already included into the dictionary.
    if key in vocabulary.keys():
        # If yes, append the value to this entry.
        vocabulary[key].append(value)
    else:
        # Otherwise create a new entry with the key.
        vocabulary[key] = [value]


''' Function to generate n next token. '''

def generate_text(input_, n_token=1):
    # input_ = string of text. Arbitrary length, but only the last token is used for the prediction.
    # n_token = number of tokens that the function generates.

    # tokenize input and store it in a list called gentext
    gentext = tok(input_)

    # predict n_token new tokens
    for i in range(n_token):
        # token_inp = last token of gentext
        token_inp = gentext[-1]
        # check if token is included into the dictionary
        if not token_inp in vocabulary.keys():
            # pick a random choice if not included
            token_inp = random.choice(list(vocabulary.keys()))
        # get all options for the last token of gentext
        options = vocabulary[token_inp]
        # choose one of this options
        choice = np.random.choice(options)
        # append it to the generated text
        gentext.append(choice)

        '''
        # add line break in random range(100, 400)
        for line in np.arange(100, gen_text_lenght, random.randrange(100, 300)):
            #print('linebreaks:', num, end= ' ')
            if i == line:
                gentext += '.\n' + '\n'
        '''

        # add .,!:
        for punc in np.arange(50, gen_text_lenght, random.randrange(10, 20)):
            if i == punc:
                gentext += [random.choice('.,!:')]

    # create output
    output = ''

    # loop through all predicted tokens
    for token in gentext:
        # if token is a punctuation:
        if token in string.punctuation:
            # append it without a whitespace
            output += token
        else:
            # else add a whitespace before the token
            output += ' ' + token


    return output


''' Find most common words in input Data set '''
# remove all tokens that are not alphabetic
words = [word for word in token if word.isalpha()]

#filter Stopwords
from nltk.corpus import stopwords
stop_words = set(stopwords.words('german'))
words = [w for w in words if not w in stop_words]

# filter more Words
excludingWords = ['Die', 'Das', 'mehr', 'Sie', 'Der', 'DIE', 'es', 'UND', 'Es', 'In', 'wurde', 'DER', 'Und', 'Ich', 'immer', 'Kanal', 'gibt', 'Bitte', 'schon', 'wurden', 'Video', 'IN', 'Uhr', 'ab', 'lassen', 'IST', 'geht', 'Ein', 'müssen', 'USA', 'bereits', 'sagte', 'SIE', 'ES', 'DAS', 'Telegram', 'abonnieren', 'neue', 'Wenn', 'abonniert', 'seit', 'sei', 'Auch', 'Jahren', 'Schuberts', 'heute', 'mal', 'Wie', 'Hier', 'Er', 'Ihr', 'viele', 'Was', 'wegen', 'Wer', 'sagt', 'Jahr', 'MIT', 'Eine', 'So', 'Diese', 'Im', 'Bei', 'neuen', 'DEN', 'kommen', 'ganz', 'gehen', 'macht', 'ZU', 'beim', 'einfach', 'AUF', 'VON', 'SICH', 'Aber', 'geben', 'zwei', 'the', 'Deine', 'WERDEN', 'gab', 'Mit', 'Für', 'WIRD', 'wäre', 'dafür', 'AN', 'Nach', 'sehen', 'Am', 'heißt', 'of', 'gar', 'gerade', 'Vielen', 'tun', 'davon', 'SIND', 'AUCH', 'lässt', 'worden', 'seien']
words = [w for w in words if not w in excludingWords]

# get most common words
fd = nltk.FreqDist(words)
#sys.stdout = open('data/Common_Words.txt', 'w')
print(fd.most_common(100))
#sys.stdout.close()


''' Generate text '''

# Pick a random input
key = token[random.randint(0, len(token))]
# Or use a string as input
#key = 'Querdenker sind:'


''' Safe Text as .txt '''
generated_text = generate_text(key, gen_text_lenght)

sys.stdout = open('_Telegram_04.txt', 'w')
print(generated_text)
sys.stdout.close()
