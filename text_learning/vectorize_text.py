#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""

from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
        if temp_counter < 20000000:
            path = os.path.join('..', path[:-1])
            print path
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            mail_content = parseOutText(email)

            ### use str.replace() to remove any instances of the words
            removals = ["sara", "shackleton", "chris", "germani", "sshacklensf", "cgermannsf", "houectect"]
            for removal in removals:
                mail_content = mail_content.replace(removal, '')
            #print mail_content

            ### append the text to word_data
            word_data.append(mail_content)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            if name == 'sara':
                from_data.append(0)
            elif name == 'chris':
                from_data.append(1)
            email.close()

print "word_data[152]: %s"%word_data[152]

print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )

### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer
#from nltk.corpus import stopwords
#stop_words = stopwords.words("english")

vectorizer = TfidfVectorizer(stop_words="english")
bag_of_words = vectorizer.fit(word_data)
print "unique word in Tfldf ", len(bag_of_words.vocabulary_)
print "idf_ ", len(bag_of_words.idf_)
print "stop words ", bag_of_words.stop_words_

sws = bag_of_words.get_feature_names()
print "sws[34597]: ", sws[34597]


