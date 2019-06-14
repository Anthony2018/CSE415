'''

name:jinlin xiang

student number: 1869385

Assignment 3 Report -- Heuristic Search

CSE 415: Introduction to Artificial Intelligence
Spring, 2019
function EightPuzzleWithManhattan
'''

import math
from EightPuzzle import *

def h(self):
    m_distance = 0
    for i in range(0,9):
        index = self.b[(i)//3][(i)%3]
        if(index !=0):
            (vi, vj) = (index // 3, index % 3)
            (wi, wj) = (i // 3, i % 3)
            m_distance += abs(vi - wi) + abs(vj - wj)
    return m_distance
