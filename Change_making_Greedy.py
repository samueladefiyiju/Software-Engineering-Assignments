#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:48:15 2020

@author: samadefiyiju
"""


#Making change- a greedy approach

amount_owed = 36 
coins = [1,5,10,25]

current_amount = 0 
solved = False 

change = {} 

while not solved:
    choice_valid = False 
    coins_left = coins
    while not choice_valid: 
        #selection 
        choice = max(coins_left)
        
        #feasibility check 
        if current_amount + choice  <= amount_owed:
            choice_valid= True 
        else:
            coins_left.remove(choice) #sometimes you might not want a remove
            
    current_amount += choice
        
    if choice not in change:
        change[choice] = 1 
    else:
        change[choice] +=1
            
    if current_amount == amount_owed:
        solved = True
        


print(change)
            
#IF we had a 12 cent coin and changed amount owed to 16, this wouldnt work, 
#this only works for American currncy and highlights the downside of greedy algorithms

amount_owed = 16
coins = [1,5,10,25,12]

current_amount = 0 
solved = False 

change = {} 

while not solved:
    choice_valid = False 
    coins_left = coins
    while not choice_valid: 
        #selection 
        choice = max(coins_left)
        
        #feasibility check 
        if current_amount + choice  <= amount_owed:
            choice_valid= True 
        else:
            coins_left.remove(choice) #sometimes you might not want a remove
            
    current_amount += choice
        
    if choice not in change:
        change[choice] = 1 
    else:
        change[choice] +=1
            
    if current_amount == amount_owed:
        solved = True
        


print(change)
