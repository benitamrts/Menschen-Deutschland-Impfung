import re
from nltk.tokenize import sent_tokenize
import sys


''' Tokenize Sentences with most Common words '''

# search for sentences with most common words | mc = most common
with open('data/cleanedInput.txt', 'r') as f:
    tokSentence = f.read()
    # Text reinigen
    tokSentence = re.sub(r'http\S+', '', tokSentence)  # Links
    tokSentence = re.sub(r'@\S+', '', tokSentence)  # Links
    tokSentence = re.sub('OneLove', '', tokSentence)  # Schlachtruf Xavier
    tokSentence = re.sub('@xavier_naidoo', '', tokSentence)  # Verlinkung Xavier Naidoo
    tokSentence = re.sub('[!@#$%^&*()[]{};:,/<>?\|`~-=_+]', '', tokSentence) # Sonderzeichen entfernen

tokSentence = re.sub('\n', '', tokSentence)
#print(sent_tokenize(tokSentence))
#sentences = test.split(".")
test = "Freiheit ist geil. Coronaleugner nicht."
sentences = sent_tokenize(tokSentence)
#print(sentences)

# MOST COMMON WORDS
# ('Deutschland', 383) ('Dr', 305) ('Regierung', 304) ('Kinder', 277) ('Quelle', 258) ('Medien', 256) ('Corona', 228) ('Ungeimpfte', 214) ('JETZT', 211) ('NICHT', 209) ('Lagemeldung', 196) ('Lockdown', 178) ('Impfpflicht', 176) ('Pandemie', 168) ('Millionen', 166) ('UNABHÄNGIGKEIT', 165) ('Freiheit', 153) ('Geimpfte', 146) ('Wahrheit', 145) ('Impfungen', 141) ('Polizei', 134), ('Impfstoff', 133) ('einfach', 132) ('Maßnahmen', 132) ('Bürger', 128) ('Bevölkerung', 127) ('Leben', 122) ('TRINKWASSER', 119) ('Informationen', 117) ('Dank', 116) ('Ärzte', 115) ('Geimpften', 114) ('Spahn', 114) ('ALLE', 112) ('Kostenlos', 111) ('Todesfälle', 109) ('Politik', 108) ('Bundesregierung', 104) ('Merkel', 101) ('Lage', 100)
# find selected keywords (over 100 matches)
search_keywords = ['Deutschland', 'Dr', 'Regierung', 'Kinder', 'Quelle', 'Medien', 'Corona', 'Ungeimpfte', 'JETZT', 'NICHT', 'Lagemeldung', 'Lockdown', 'Impfpflicht', 'Pandemie', 'Millionen', 'UNABHÄNGIGKEIT', 'Freiheit', 'Geimpfte', 'Wahrheit', 'Impfungen', 'Polizei', 'Impfstoff', 'einfach', 'Maßnahmen', 'Bürger', 'Bevölkerung', 'Leben', 'TRINKWASSER', 'Informationen', 'Dank', 'Ärzte', 'Geimpften', 'Spahn', 'ALLE', 'Kostenlos', 'Todesfälle', 'Politik', 'Bundesregierung', 'Merkel', 'Lage']
#search_keywords = ['Freiheit']

mc = {}
for sentence in sentences:
    mc[sentence] = sum(1 for word in search_keywords if word in sentence)
#best_sentences = [key for key,value in mc.items() if value == max(mc.values())]
best_sentences = [key for key, value in mc.items() if value == 1]

#print("\n".join(best_sentences))
#print('found senteces:', len(best_sentences))

#put sentences into .txt
sys.stdout = open('data/Sentences_With_Most_Common_Words.txt', 'w')
print(*best_sentences, sep = '\n\n')
sys.stdout.close()


'''
# merge different input texts once 
input_All = ['data/Xavier_10000.txt', 'data/Attila_10000.txt', 'data/Wendler_10000.txt']
with open('data/Input_all.txt', 'w') as outfile:
    for input in input_All:
        with open(input) as infile:
            contents = infile.read()
            outfile.write(contents)
'''