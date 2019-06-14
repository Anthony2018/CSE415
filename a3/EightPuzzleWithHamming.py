'''
name:jinlin xiang

student number: 1869385

Assignment 3 Report -- Heuristic Search

CSE 415: Introduction to Artificial Intelligence
Spring, 2019
function EightPuzzleWithHamming
'''

import math
from EightPuzzle import *

def h(self):
    C = 0
    #goal = GOAL_STATE
    for i in range(1,9):
        index = self.b[i//3][i%3]
        print (index)
        if index !=i:
            C += 1
    return C