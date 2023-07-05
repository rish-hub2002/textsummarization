# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 20:40:49 2022

@author: naikr
"""
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
   
# Input text - to summarize 
text = "An artificially intelligent computer system makes predictions or takes actions based on patterns in existing data and can then learn from its errors to increase its accuracy. A mature AI processes new information extremely quickly and accurately, which makes it useful for complex scenarios such as self-driving cars, image recognition programmes, and virtual assistants.AI software allows users to implement general machine learning, or more specific deep learning capabilities, such as natural language processing, computer vision, and speech recognition."
   
# Tokenizing the text
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)
   
# Creating a frequency table to keep the 
# score of each word
   
freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1
   
# Creating a dictionary to keep the score
# of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()
   
for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq
   
   
   
sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]
   
# Average value of a sentence from the original text
   
average = int(sumValues / len(sentenceValue))
   
# Storing sentences into our summary.
summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence
print(summary)
