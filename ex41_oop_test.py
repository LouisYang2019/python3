#ex41 Learning to Speak Object-Oriented
import random
from urllib.request import urlopen
import sys

WORD_URL = 'http://learncodethehardway.org/word.txt'
WORDS = []

PHRASES = {
    'class %%%(%%%):':
        'Make a class named %%% that is-a %%%.',
    'class %%%(object):\n\tdef __init__(self, ***)':
        'class %%% has-a __init__ that takes self and *** params.',
    'class %%%(object):\n\tdef ***(self, @@@)':
        'class %%% has-a function *** that takes self and @@@ params.',
    '*** = %%%()':
        'Set *** to an instance of class %%%.',
    '***.***(@@@)':
        'From *** get the *** function, call it with params self, @@@.',
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
    }

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding='utf-8'))

def convert(snippet, phrase):
    class_names = [w.capitlize() for w in
        random.sample(WORDS, snippet.count('%%%'))]
