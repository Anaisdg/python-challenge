# i-*- coding: UTF-8 -*-

# mport correct readers
import os
import re

# Assign the text file to a variable for ease
pyparagraph="Pyparagraph.txt"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test 1

# Open the textfile
#with open(pyparagraph, 'r') as text:
    # Parse the text into words by splitting text at every space
    #words = pyparagraph.split()

    # Set total and then use for loop to count the words in each line
    #totalwords = 0 
    # In comprehensions would look like: wordcount = [ line.len(), (total + line.len() for line in words]

    #for line in words:
       #number = len(line)
       #totalwords = totalwords + number

# Total is currently printing 15 which is incorrect
#print(f'Approximate Word Count: {totalwords}')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Test 2
#wordtest = len(pyparagraph)
# Wordtest is also printing 15 which is incorrect but test shows that above code is functional
#print(f'Approximate Word Count 2: {wordtest}')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test 3

# Open the textfile
with open(pyparagraph, 'r') as text:
    file_contents = text.read()

# Parse the text into senetences by splitting text at every space and print
word_count = len(file_contents.split())
print('Approximate word count: ', word_count)

# Count the sentences by counting the . in the text and print
sentence_count = file_contents.count('.')
print('Approximate sentence count: ', file_contents.count('.'))

# Find total characters in text and print for test
characters = len(file_contents)
#print('Total characters in text: ', characters))

# Fine total number of spaces in text and print for test
spaces = file_contents.count(' ')
#print('Total spaces in text: ', spaces)

# Take total characters subtract the spaces and divide by approximate average word length
word_length = (characters-spaces)/word_count
print('Approximate average word length: ', int(word_length))

# Take total word count and divide by sentences for approximate average sentence length
sentence_length = word_count/sentence_count
print('Approximate average sentence length: ', int(sentence_length))

