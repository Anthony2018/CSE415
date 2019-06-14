'''farmer Fox problem.py
by jinlin xiang
2019-04-16
cse 415 spring
assignment 2
BFS FUNCTION
'''

import sys

if sys.argv==[''] or len(sys.argv) < 2:
  import jinlinx_Farmer_Fox as Problem
  #import TowersOfHanoi as Problem
  #import Missionaries as Problem
else:
  import importlib
  Problem = importlib.import_module(sys.argv[1])

print("\nWelcome to BFS")
COUNT = None
BACKLINKS = {}

def runBFS():
  initial_state = Problem.CREATE_INITIAL_STATE()
  print("Initial State:")
  print(initial_state)
  global COUNT, BACKLINKS, MAX_OPEN_LENGTH
  COUNT = 0
  BACKLINKS = {}
  MAX_OPEN_LENGTH = 0
  IterativeBFS(initial_state) # issue here
  print(str(COUNT)+" states examined.")
  print('MAX_OPEN_LENGTH = '+str(MAX_OPEN_LENGTH))

def IterativeBFS(initial_state):
  global COUNT, BACKLINKS, MAX_OPEN_LENGTH

# STEP 1. Put the start state on a list OPEN
  OPEN = [initial_state]
  CLOSED = []
  BACKLINKS[initial_state] = None

# STEP 2. If OPEN is empty, output “DONE” and stop.
  while OPEN != []:
    report(OPEN, CLOSED, COUNT)
    if len(OPEN)>MAX_OPEN_LENGTH: MAX_OPEN_LENGTH = len(OPEN)
    S = OPEN.pop(0)
    CLOSED.append(S)
    # prints start of solution given pegs 1 & 2 are empty
    if Problem.GOAL_TEST(S):
      print(Problem.GOAL_MESSAGE_FUNCTION(S))
      path = backtrace(S)
      print('Length of solution path found: '+str(len(path)-1)+' edges')
      return
    COUNT += 1

    L = []
    for op in Problem.OPERATORS:
      if op.precond(S):
        new_state = op.state_transf(S)
        if not (new_state in CLOSED):
            BACKLINKS[new_state] = S
            L.append(new_state)

# STEP 5. Delete from OPEN any members of OPEN that occur on L.
#         Insert all members of L at the front of OPEN.
    for s2 in OPEN:
      for i in range(len(L)):
        if (s2 == L[i]):
          del L[i]; break

    OPEN = OPEN + L
    print_state_list("OPEN",OPEN)
# STEP 6. Go to Step 2.

def print_state_list(name, lst):
  print(name+" is now: ",end='')
  for s in lst[:-1]:
    print(str(s),end=', ')
  print(str(lst[-1]))

# backtrace the goal and prints it out
def backtrace(S):
  global BACKLINKS
  path = []
  while S:
    path.append(S)
    S = BACKLINKS[S]
  path.reverse()
  print("Solution path: ")
  for s in path:
    print(s)
  return path    

def report(open, closed, count):
  print("len(OPEN)="+str(len(open)), end='; ')
  print("len(CLOSED)="+str(len(closed)), end='; ')
  print("COUNT = "+str(count))

if __name__=='__main__':
  runBFS()