#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:17:37 2020

@author: samadefiyiju
"""




def printboard(board):
    for i in range(len(board)):
        for j in range (len(board[0])):
            print( board[i][j], end = " ")
        print("\n")




def is_promising(board, row, col):
    i = j = 0 

    for i in range (col):

        if (board[row][i]):

            return False

    i = row 
    j = col 
    while i >= 0 and j >=0:
        if (board[i][j]):   
            return False
        i -= 1 
        j -= 1 
    i = row 
    j = col 
    while i < len(board) and j >= 0:
        if (board[i][j]):
            return False
        i += 1 
        j -= 1 
    return True 
   
def Expand(board, col):
    
    if (col >= len(board)):
        return True

    for i in range (len(board)):
        if (is_promising(board, i, col) ):
            board[i][col] = 1

            if ( Expand(board, col + 1) == True ):
                return True


            board[i][col] = 0


    return False;






board8x8 = [[0, 0, 0, 0,0,0,0,0],
            [0, 0, 0,0,0,0,0,0],
            [0, 0, 0, 0,0,0,0,0],
            [0, 0, 0, 0,0,0,0,0],
            [0, 0, 0, 0,0,0,0,0],
            [0, 0, 0, 0,0,0,0,0],
             [0, 0, 0, 0,0,0,0,0],
             [0, 0, 0, 0,0,0,0,0]]

if ( Expand(board8x8, 0) == False ):
    print("No Solution")
else:
    printboard(board8x8);

    




