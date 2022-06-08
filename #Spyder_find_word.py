# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:03:21 2022

@author: Proger
"""


from uzwords import words
import random

def get_word(words):
    word=random.choice(words)
    while "-" in word or ' in word':
        word=random.choice(words)
    return word
get_word(words)

def play():
    word=get_word(words)
    display_letter=set(word)    
    user_letter=""
    while display_letter:
        letter=input(">>>")
        if letter in display_letter:
            print('Bu harf bor')
        user_letter+=letter
        print(user_letter)
play()
