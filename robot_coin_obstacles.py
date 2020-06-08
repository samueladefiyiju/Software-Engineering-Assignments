#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Samuel Adefiyiju

x = "x"


def robot_coin_collection(C):
    rows = len(C)
    cols = len(C[0])
    if(C[0][0] == "x" or C[len(C)-1][len(C[0])-1] == "x"):
        return 0
    F = [[C[0][0]]]
    for j in range(1, cols):
        if C[0][j] == x:
            F[0].append(0)     
        elif x in C[0][:j]:      
            F[0].append(0) # fill in first row
        else:
            F[0].append(F[0][j-1] + C[0][j])
           
    for i in range(1, rows):
        if C[i][0] == x:
            F.append([0])
            for j  in range(i+1, rows):
                F.append([0])
            break
        else:
            F.append([F[i-1][0] + C[i][0]]) # fill in first col
        #  if (C[i][j] != x and not(C[i][j-1] == x and C[i-1][j]==0 or (C[i][j-1] == x and C[i-1][j]==x) or ((F[i][j-1] == 0 and F[i-1][j]==0)))):

    for i in range(1, rows):
        for j in range(1, cols):
            if (C[i][j] != x and not((C[i][j-1] == x and C[i-1][j]==x) or ((F[i][j-1] == 0 and F[i-1][j]==0)))):
                F[i].append(max(F[i-1][j], F[i][j-1]) + C[i][j]) #THIS LINE 
            elif(C[i][j-1] == x and C[i-1][j]==x):
               F[i].append(max(F[i-1][j], F[i][j-1]))
            else:
                F[i].append(0) # apply recursion
            
    for k in F:
        print(k)
    return F[rows-1][cols-1]





print("original test case: ")
C = [[0,x,0,1,0,0],

     [1,0,0,x,1,0],

     [0,1,0,x,1,0],

     [0,0,0,1,0,1],

     [x,x,x,0,1,0]]

for k in C:
        print(k)
print("\n")
print("Path for robot: ")
print(robot_coin_collection(C))




