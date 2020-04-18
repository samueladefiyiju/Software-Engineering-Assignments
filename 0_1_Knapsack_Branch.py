#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:03:40 2020

@author: samuel adefiyiju

The Following code uses a branch and bound algogrithm in order to compute the maximum profit for the 0-1 Knapsack Problem. 
"""
import copy 
class node:
    pass 




def knapsack2(n, p,w,W,maxprofit):
    
    v = node()
    u = node()
    u.level = 0 
    u.profit = 0 
    u.weight = 0
    v.level = 0; v.profit = 0; v.weight = 0;
    Q = []
    maxprofit = 0
    Q.append(copy.deepcopy(v))
    while (Q != []):
        v = Q.pop(0)
     
       
        u.level = v.level +1
        
        u.profit = v.profit + p[u.level-1]
        u.weight = v.weight + w[u.level-1]
        
        if (u.weight <= W and u.profit > maxprofit):
            maxprofit = u.profit
        bound_of_node = bound(u,n,p,w,W)
        if bound_of_node > maxprofit:
            Q.append(copy.deepcopy(u))
           
        
        u.profit = v.profit
        u.weight = v.weight
        
        bound_of_node = bound(u,n,p,w,W)  
        if (bound_of_node > maxprofit):
            Q.append(copy.deepcopy(u)); 
           
    return maxprofit
def bound(u, n, p, w, W):

   
    j= 0
    k= 0
    totweight= 0 
    result = 0 
    if (u.weight >=W):
        return 0
    else:
        result = float(u.profit)
        j = u.level 
        totweight = u.weight    
        while (j<n and totweight +w[j] <=W):
            totweight = totweight +w[j]
            result = result +p[j]
            j +=1    
        k=j
        if (k<n):
            result = result + (W- totweight) * int(p[k]/w[k])
        return float(result)
                
maxProfit = 0
n = 5
W = 13
p= [20,30,35,12,3]
w = [2,5,7,3,1]

print("Max Profit: ", knapsack2(n, p, w, W, maxProfit))


    