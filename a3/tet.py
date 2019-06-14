'''Name: Freddie He   UWID:heyingge
heyingge_AStar.py
Assignment 3, in CSE 415, Winter 2018.
This file contains the problem formulation for the problem of
the Eight Puzzle. In addition, 4 heuristics calculations are provided.
'''

import sys
import simplePriorityQ

if sys.argv == [''] or len(sys.argv) < 2:
    import TowersOfHanoi as Problem
else:
    import importlib

    Problem = importlib.import_module(sys.argv[1])
function = sys.argv[2]

print("\nWelcome to ItrDFS")
COUNT = None
BACKLINKS = {}
a = 0


def runAStar():
    initial_state = Problem.CREATE_INITIAL_STATE()
    print("Initial State:")
    print(initial_state)
    global COUNT, BACKLINKS, MAX_OPEN_LENGTH
    COUNT = 0
    BACKLINKS = {}
    MAX_OPEN_LENGTH = 0
    AStar(initial_state)
    print(str(COUNT) + " states expanded.")
    print('MAX_OPEN_LENGTH = ' + str(MAX_OPEN_LENGTH))


def AStar(initial_state):
    global COUNT, BACKLINKS, MAX_OPEN_LENGTH

    # STEP 1. Put the start state on a list OPEN
    OPEN = simplePriorityQ.PriorityQ()
    CLOSED = []
    BACKLINKS[initial_state] = None
    OPEN.insert(initial_state, find_h(initial_state))

    # STEP 2. If OPEN is empty, output “DONE” and stop.
    while OPEN != []:
        report(OPEN, CLOSED, COUNT)
        if len(OPEN) > MAX_OPEN_LENGTH: MAX_OPEN_LENGTH = len(OPEN)

        # STEP 3. Select the first state on OPEN and call it S.
        #         Delete S from OPEN.
        #         Put S on CLOSED.
        #         If S is a goal state, output its description
        KVPair = OPEN.deletemin()
        S = KVPair[0]
        CLOSED.append(S)

        if Problem.GOAL_TEST(S):
            print(Problem.GOAL_MESSAGE_FUNCTION(S))
            path = backtrace(S, True)
            print('Length of solution path found: '
                  + str(len(path) - 1) + ' edges')
            return
        COUNT += 1

        # STEP 4. Generate the list L of successors of S and delete
        #         from L those states already appearing on CLOSED.
        L = []
        for op in Problem.OPERATORS:
            if op.precond(S):
                new_state = op.state_transf(S)
                if not (new_state in CLOSED):
                    L.append(new_state)

        # STEP 5. Delete from OPEN any members of OPEN that occur on L.
        #         Insert all members of L at the front of OPEN.
        for s2 in L:
            new_g = KVPair[1] - find_h(S) + 1
            new_f = find_h(s2) + new_g
            try:
                OPEN.getEnqueuedElement(s2)
                old_g = len(backtrace(s2, False)) - 1
                if new_g < old_g:
                    OPEN.remove(s2)
                    OPEN.insert(s2, new_f)
                    BACKLINKS[s2] = S
            except:
                BACKLINKS[s2] = S
                OPEN.insert(s2, new_f)
            print_state_list("OPEN", OPEN)


# STEP 6. Go to Step 2.

def print_state_list(name, queue):
    print(name + " is now: ", end='')
    print(queue)


def backtrace(S, bool):
    global BACKLINKS
    path = []
    while S:
        path.append(S)
        S = BACKLINKS[S]
    path.reverse()
    if bool:
        print("Solution path: ")
        for s in path:
            print(s)
    return path


def find_h(s):
    return eval('s.' + function + '()')


def find_g(s):
    return len(backtrace(s, False)) - 1


def report(open, closed, count):
    print("len(OPEN)=" + str(len(open)), end='; ')
    print("len(CLOSED)=" + str(len(closed)), end='; ')
    print("COUNT = " + str(count))


if __name__ == '__main__':
    runAStar()