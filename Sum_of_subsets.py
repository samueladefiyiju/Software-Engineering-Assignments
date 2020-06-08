#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 19:12:22 2020

@author: samadefiyiju
"""
#The Sum of Subsets problem 

W = 52
w = [2, 10, 13, 17, 22, 42]
include =["No"] * len(w)
index = []

def sum_of_subsets(i,weight,total): 
    
    if (promising(i,weight,total)):
        if weight == W:
            print("Using numbers at index: " )
            for j in range(0,len(w)):
                if include[j] == "Yes":
                    print(j+1)
            
        else:
            include[i+1] = "Yes"
            index.append(w[i+1])
            sum_of_subsets(i+1, weight + w[i+1], total- w[i+1])
            include[i+1] = "No"
            sum_of_subsets(i+1, weight, total - w[i+1])
            
def promising(i, weight, total):

    return(weight + total >= W) and (weight == W or weight + w[i+1] <= W)
            
            
    
sum_of_subsets(-1,0,sum(w))

