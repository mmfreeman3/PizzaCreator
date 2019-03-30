'''
Created on Mar 30, 2019

@author: ITAUser
'''
#random topping selector

import random
f = open("toppings.txt", "r") #open file and read
words = f.readlines() #allows python to read each word in the list
index = random.randint(0, len(words) - 1) # selects a random index for a word
word = words[index].split() #seperates the words
print(random.choice(word)) #prints a random word 