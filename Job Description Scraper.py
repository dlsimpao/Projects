#Resume Parsing

import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus

from nltk.tokenize import word_tokenize

#file_name = input("Enter data file")
file_name = "AA2020.txt"


fHandle = open(file_name)

##for line in fHandle:
##    line = word_tokenize(line)
##    print(line)
##fHandle.close()

test = "The work:\
Participate in our ten week summer Technology Development Program to learn the latest technical skills.\
Learn first-hand how we help many of the world's top companies develop their tech strategy.\
Work with a diverse group of people and clients during your summer project.\
·      Bridge the gap between technology and business by using your technical and analytical expertise\
·      Develop front end solutions and design, develop and implement software."

#tokenize
test = word_tokenize(test)
print(test)

