#Job Description Scraper

import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus

import string


from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords



#file_name = input("Enter data file")
file_name = "AA2020.txt"

#treats file as one string, named "data"
with open(file_name, encoding = "utf8") as file:
    data = file.read().replace('\n', ' ')

#tokenize
word_list = word_tokenize(data.lower())

#Filtering
sw = set(stopwords.words('english'))
p = ["·","’","–"]
word_list = [x for x in word_list if x not in sw and x not in string.punctuation and x not in p]

#frequency distribution
fdist = FreqDist(word_list)



#List of problems encountered

#installing packages "python -m pip install NAME"
#unicode decoding problems | open(file,encoding="utf8") (https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character)
#treat file as one string    

