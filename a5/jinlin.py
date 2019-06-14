'''PlayerSkeletonA.py
The beginnings of an agent that might someday play Baroque Chess.
'''
import time
from datetime import datetime, timedelta
import math
import heapq
import random
import BC_state_etc as BC

# GLOBAL VARIABLES
COUNT = 0 
CUTOFFS = 0 
alphaBeta1 = True
BEST_STATE = None
ZOBRIST_USE = True
TIME_LIMIT_OFFSET = 0.1
BLACK = BC.BLACK
WHITE = BC.WHITE
PIECE_VALS  = [0,0,-1,1,-2,2,-2,2,-3,3,-8,8,-100,100,-2,2]
PAST_MOVE = [-1, -1, -1] # Piece, x, y

def parameterized_minimax(currentState, alphaBeta=False, ply=3,\
    useBasicStaticEval=True, useZobristHashing=True):
    global alphaBeta1
    global CURRENT_STATE_STATIC_VAL
    global N_STATIC_EVALS
    global ZOBRIST_USE
    if (alphaBeta == False):
        alphaBeta1 = False
    if (useZobristHashing == False ):
        ZOBRIST_USE = False

    CURRENT_STATE_STATIC_VAL = basicStaticEval(currentState)
    #endTime = 10
    now = datetime.now()
    depth = 0
    best = None
    while datetime.now() < now + timedelta(0, 10) or depth <= ply:
            depth =depth + 1
            best_state = minimax_function(currentState, depth , 1 , now + timedelta(0, 10))
            if best_state != None:
                best = best_state
            else:
                break
    print(best)
    N_STATIC_EVALS= best.static_eval()
    return{'CURRENT_STATE_STATIC_VAL':CURRENT_STATE_STATIC_VAL,'N_STATES_EXPANDED':COUNT,'N_STATIC_EVALS':N_STATIC_EVALS,'N_CUTOFFS':CUTOFFS}
    

def nickname():
    return "Newman"

def introduce():
    return "I'm Newman Barry, a newbie Baroque Chess agent."

def prepare(player2Nickname):
    pass

def basicStaticEval(state):
    return sum([sum([PIECE_VALS [j] for j in i]) for i in state.board])

def staticEval(state):
    return sum([sum([PIECE_VALS [j] for j in i]) for i in state.board])
# initialize zobrist table
ZOBRIST_N = []
ZOBRIST_M = {}
random.seed(0)
for x in range(64):
    ZOBRIST_N.append([])
    for y in range(16):
        ZOBRIST_N[x].append(random.randint(0, 2**64))#64 for row and colomn 16 for cheese so hash 64 bit 

class z_node:
    def __init__(self, state):
        self.state = state
        self.children = []

def makeMove(currentState, currentRemark, timelimit):
    now = datetime.now()
    global BEST_STATE
    newRemark = "Your turn!"
    # search for 10 seconds
    c_state = State(currentState.board, currentState.whose_move)
    #$print('c_state & best')
    #print(c_state)
    best = IDDFS_function(c_state, now + timedelta(0,timelimit))
    #print('best')
    #print(best)
    tempa=()
    tempb=()
    for x in range (8):
        for y in range (8): 
            if(best.board[x][y] != c_state.board[x][y]):
                if(c_state.board[x][y] == 0):
                    tempa=(x,y)
                    tempx = x
                    tempy = y
                    #print('i am the first')
                    #print(tempa)
    for xi in range (8):
        for yi in range (8):
            if(best.board[xi][yi] !=c_state.board[xi][yi]):
                if(best.board[tempx][tempy] == c_state.board[xi][yi]):
                        tempb=(xi,yi)
                        #print('i am the second')
                        #print(tempb)
    move = ((tempb),(tempa))
    return [[move, best], newRemark]

def static_eval(state):
    return sum([sum([PIECE_VALS [j] for j in i]) for i in state.board])

def IDDFS_function(currentState, endTime):
    depth = 0
    best = None
    while datetime.now() < endTime:
        depth += 1
        operation = -1 if currentState.whose_move == BLACK else 1
        best_state = minimax_function(currentState, depth, operation, endTime)
        if best_state != None:
            best = best_state
        else:
            break
    return best

def is_over_time(endTime):
    global TIME_LIMIT_OFFSET
    now = datetime.now()
    return (now + timedelta(0, TIME_LIMIT_OFFSET)) >= endTime

def minimax_function_helper(state, depth, operation, endTime, alpha, beta):
    global ZOBRIST_M
    global COUNT
    global CUTOFFS
    global ZOBRIST_USE
    if is_over_time(endTime):
        return None
    if depth == 0:
        state.static_eval()
        return state
    state.static_eval()
    board = state.board
    child_states = []
    s = None
    h = hash_z(board)
    time.sleep(0.1)
    if(ZOBRIST_USE == True):
        try:
            s = ZOBRIST_M[h]
        except:
            s = z_node(state)
    else:
        s = z_node(state)

    if len(s.children) == 0:
        child_states = get_child_states(state, h)
        for c in child_states:
            h1 = hash_z(c.board)
            s.children.append(h1)
            ZOBRIST_M[h1] = z_node(c)
        ZOBRIST_M[h] = s
    else:
        for c in s.children:
            child_states.append(ZOBRIST_M[c].state)
    
    heapq.heapify(child_states)
    best = None
    best_eval = 0
    while len(child_states) != 0:
        c_state = heapq.heappop(child_states)
        # Time check
        if is_over_time(endTime):
            break
        # check alpha beta for invalid state
        if alpha >= beta:
            CUTOFFS = CUTOFFS + 1
            break
        new_state = minimax_function_helper(c_state, depth-1, -operation, endTime, alpha, beta)
        if new_state != None:
            new_eval = new_state.eval
            COUNT = COUNT + 1
        else:
            new_eval = 0
        if best == None:
            best = new_state
            best_eval = new_eval
        elif operation*new_eval >= operation*best_eval:
            best = new_state
            best_eval = new_eval
        if operation == 1:
            # set alpha
            if(alphaBeta1 == True):
                alpha = max(alpha, new_eval)
                #print('i am  the max')
                #print(alpha,beta)
                #if alpha >= beta:
                 #   CUTOFFS = CUTOFFS+1
        else:
            # set beta
            if(alphaBeta1 == True):
                beta = min(beta, new_eval)
                #print('i am  the minc')
                #print(alpha,beta)
                #if alpha >= beta:
                   # CUTOFFS = CUTOFFS+1
    return best

def minimax_function(state, depth, operation, endTime):
    global alphaBeta1
    global CUTOFFS
    global COUNT
    global ZOBRIST_USE
    
    h = hash_z(state.board)
    child_states = []
    s = None
    if(ZOBRIST_USE == True):
        try:
            s = ZOBRIST_M[h]
        except:
            s = z_node(state)
    else:
        s = z_node(state)
    
    if len(s.children) == 0:
        child_states = get_child_states(state, h)
        for c in child_states:
            h1 = hash_z(c.board)
            s.children.append(h1)
            c.static_eval()
            ZOBRIST_M[h1] = z_node(c)
        ZOBRIST_M[h] = s
    else:
        for c in s.children:
            child_states.append(ZOBRIST_M[c].state)
    heapq.heapify(child_states)
    best = None
    best_eval = 0
    alpha = -math.inf
    beta = math.inf
    while len(child_states) != 0:
        c_state = heapq.heappop(child_states)
        #check time
        if is_over_time(endTime):
            best = None
            break
        if alpha >= beta:
            CUTOFFS = CUTOFFS+1
            break
        new_state = minimax_function_helper(c_state, depth - 1, -operation, endTime,alpha, beta)
        if new_state != None:
            new_eval = new_state.eval
            COUNT = COUNT + 1
        else:
            new_eval = 0
        if operation == 1:
            # set alpha
            if (alphaBeta1 == True):
                alpha = max(alpha, new_eval)
                #print('i am  the max')
                #print(alpha,beta)
                #if alpha >= beta:
                    #CUTOFFS = CUTOFFS+1
        else:
            # set beta
            if (alphaBeta1 == True):
                beta = min(beta, new_eval)
                #print('i am mini')
                #print(alpha,beta)
                #if alpha >= beta:
                    #CUTOFFS = CUTOFFS+1
        if best == None or operation*new_eval >= operation*best_eval:
            best = c_state
            best_eval = new_eval
    return best


def get_child_states(state, h):
    board = state.board
    child_states = []
    for x in range(0, len(board)):
        for y in range(0, len(board[x])):
            # Get current piece number
            piece = board[x][y]
            # if current player is the same color as the piece get all child states
            if piece != 0 and BC.who(piece) == state.whose_move:
                child_states += moverule(state, h, x, y)

    return child_states

def king_search(board):
    wKingPiece = None
    bKingPiece = None
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == BC.INIT_TO_CODE['K']:
                wKingPiece = (i, j)
            elif board[i][j] == BC.INIT_TO_CODE['k']:
                bKingPiece = (i, j)
    return [wKingPiece, bKingPiece]

def freezer_search(board, whose_move):
    frozen = [[],[]]
    for x in range(0, len(board)):
        for y in range(0, len(board[x])):
            if board[x][y] - BC.who(board[x][y]) == BC.INIT_TO_CODE['f']:
                for i, j in value:
                    if x+i >= 0 and y+j >= 0 and x+i <= 7 and y+j <= 7:
                        frozen[BC.who(board[x][y])].append((x+i, y+j))
    return frozen

def hash_z(board):
    val = 0
    for x in range(8):
        for y in range(8):
            piece = board[x][y]
            if piece != 0:
                val ^= ZOBRIST_N[8*x+y][piece]
    return val

INITIAL = BC.parse('''
c l i w k i l f
p p p p p p p p
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
P P P P P P P P
F L I W K I L C
''')

INITIAL_2 = BC.parse('''
c l i w k i l f 
p p - p p p p p 
- - - - - - - - 
- - P - P - P - 
- - - - - - - - 
- - - - - - - - 
P P - P - P - P 
F L I W K I L C
''')

INITIAL_3 = BC.parse('''
c l - - k i - - 
p i - p - p - p 
- p p P - - f - 
- - P - - P w P 
- - - - - - - - 
- P - - - - - P 
- - P - K P - C 
F L I W - I - - 
''')

class State:
    def __init__(self, old_board=INITIAL, whose_move=WHITE, kingP=[], frozen=[]):
        self.whose_move = whose_move
        self.board = [r[:] for r in old_board]
        if len(kingP) == 0: self.kingP = king_search(old_board)
        else: self.kingP = [(k[0], k[1]) for k in kingP]
        if len(frozen) == 0: self.frozen = freezer_search(old_board, whose_move)
        else: self.frozen = [[(f[0], f[1]) for f in i] for i in frozen]

        self.eval = None

    def __repr__(self):
        s = ''
        for r in range(8):
            for c in range(8):
                s += BC.CODE_TO_INIT[self.board[r][c]] + " "
            s += "\n"
        if self.whose_move==WHITE: s += "WHITE's move"
        else: s += "BLACK's move"
        s += "\n"
        return s

    def __copy__(self):
        new_state = State(self.board, self.whose_move,
            self.kingP, self.frozen)
        return new_state

    def __eq__(self, other):
        if isinstance(other, State):
            for i in range(0, len(self.board)):
                if self.board[i] != other.board[i]: return False
            return True
        return False

    def __lt__(self, other):
        if self.whose_move == WHITE:
           lt = static_eval(self) > static_eval(other)
        else:
            lt = static_eval(self) < static_eval(other)
        return lt

    def static_eval(self):
        if self.eval == None:
            self.eval = static_eval(self)
        return self.eval

value = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

def moverule(state, zobrist_h, xDir, yDir):
    if (xDir, yDir) in state.frozen[1-state.whose_move]:
        return []
    child_states = []
    piece = state.board[xDir][yDir]
    piece_t = piece - BC.who(piece)
    # loop all 8 directions
    directions = value[0:4] if piece_t == BC.INIT_TO_CODE['p'] else value
    for i, j in directions:
        x = xDir
        y = yDir
        while x+i >= 0 and y+j >= 0 and x+i <= 7 and y+j <= 7 \
                and (state.board[x+i][y+j] == 0\
                or piece_t == BC.INIT_TO_CODE["k"]):
            if piece_t != BC.INIT_TO_CODE["k"]:
                x += i
                y += j
            if piece == PAST_MOVE[0] and x == PAST_MOVE[1] and y == PAST_MOVE[2] and piece_t != BC.INIT_TO_CODE["k"]:
                continue
            c_state = state.__copy__()
            c_state.whose_move = 1 - c_state.whose_move
            c_state.board[xDir][yDir] = 0
            c_state.board[x][y] = piece
            z_h = zobrist_h
            z_h ^= ZOBRIST_N[8*xDir+yDir][c_state.board[xDir][yDir]]
            z_h ^= ZOBRIST_N[8*x+y][c_state.board[x][y]]
            if piece_t == BC.INIT_TO_CODE['p']:
                child_states.append(pincher_function(c_state, x, y, z_h))
            elif piece_t == BC.INIT_TO_CODE['c']:
                child_states.append(coordinator_function(c_state, x, y, z_h))
            elif piece_t == BC.INIT_TO_CODE['f']:
                child_states.append(freezer_function(c_state, x, y, z_h))
            elif piece_t == BC.INIT_TO_CODE['l']:
                child_states.append(leaper_function(c_state, x, y, i, j, z_h))
            elif piece_t == BC.INIT_TO_CODE['i']:
                child_states.extend(imitator_function(c_state,x,y,xDir,yDir,i,j,z_h))
            elif piece_t == BC.INIT_TO_CODE['w']:
                child_states.append(withdrawer_function(c_state, xDir-i, yDir-j,z_h))
            elif piece_t == BC.INIT_TO_CODE['k']:
                child_states.append(king_function(c_state, x, y, x+i, y+j, z_h))
            if piece_t == BC.INIT_TO_CODE['k']: break

    return child_states

def pincher_function(state, x, y, z_h):
    global ZOBRIST_M
    piece = state.board[x][y]
    for i, j in value[0:4]:
        if on_board_or_not(x, y) and on_board_or_not(x+i, y+j) and on_board_or_not(x+2*i, y+2*j) and BC.who(state.board[x+i][y+j]) != BC.who(piece)  and state.board[x+2*i][y+2*j] == piece:
            z_h ^= ZOBRIST_N[8*(x+i)+y+j][state.board[x+i][y+j]]
            state.board[x+i][y+j] = 0
    state.static_eval()
    ZOBRIST_M[z_h] = z_node(state)
    return state

def coordinator_function(state, x, y, z_h):
    global ZOBRIST_M
    newx, newy = state.kingP[state.whose_move]
    if on_board_or_not(x,y) and on_board_or_not(x, newy) and BC.who(state.board[x][y]) != BC.who(state.board[x][newy]):
        z_h ^= ZOBRIST_N[8*x+newy][state.board[x][newy]]
        state.board[x][newy] = 0
    if on_board_or_not(x,y) and on_board_or_not(newx, y) and BC.who(state.board[x][y]) != BC.who(state.board[newx][y]):
        z_h ^= ZOBRIST_N[8*newx+y][state.board[newx][y]]
        state.board[newx][y] = 0
    state.static_eval()
    ZOBRIST_M[z_h] = z_node(state)
    return state

def freezer_function(state, x, y, z_h):
    global ZOBRIST_M
    state.frozen[state.whose_move] = []
    for i, j in value:
        if on_board_or_not(x+i, y+j):
            state.frozen[state.whose_move].append((x+i,y+j))
    state.static_eval()
    ZOBRIST_M[z_h] = z_node(state)
    return state

def leaper_function(state, x, y, i, j, z_h):
    global ZOBRIST_M
    if on_board_or_not(x,y) and on_board_or_not(x+i, y+j) and on_board_or_not(x+2*i,y+2*j) and BC.who(state.board[x+i][y+j]) != BC.who(state.board[x][y]) and state.board[x+i][y+j] != 0 and state.board[x+2*i][y+2*j] == 0:
        z_h ^= ZOBRIST_N[8*(x+2*i)+(y+2*j)][state.board[x][y]]
        z_h ^= ZOBRIST_N[8*x+y][state.board[x][y]]
        z_h ^= ZOBRIST_N[8*(x+i)+y+j][state.board[x+i][y+j]]
        state.board[x+2*i][y+2*j] = state.board[x][y]
        state.board[x][y] = 0
        state.board[x+i][y+j] = 0
    state.static_eval()
    ZOBRIST_M[z_h] = z_node(state)
    return state

def imitator_function(state, x, y, x0, y0, i, j, z_h):
    global ZOBRIST_M
    imitate = []
    if on_board_or_not(x,y):
        p_imit = state.__copy__()
        for i, j in value[0:4]:
            if on_board_or_not(x+i, y+j) and on_board_or_not(x+2*i, y+2*j)\
                    and state.board[x+i][y+j] - state.whose_move == BC.INIT_TO_CODE['p'] \
                    and state.board[x+2*i][y+2*j] + state.whose_move == BC.INIT_TO_CODE['P']:
                p_imit.board[x+i][y+j] = 0
                imitate.append(p_imit)
        newx, newy = state.kingP[state.whose_move]
        k_imit = state.__copy__()
        k_bool = False
        if on_board_or_not(x, newy) \
                and BC.who(state.board[x][y]) != BC.who(state.board[x][newy]) \
                and state.board[x][newy] - state.whose_move == BC.INIT_TO_CODE['c']:
            k_imit.board[x][newy] = 0
            k_bool = True
        if on_board_or_not(newx, y)\
                and BC.who(state.board[x][y]) != BC.who(state.board[newx][y]) \
                and state.board[newx][y] - state.whose_move == BC.INIT_TO_CODE['c']:
            k_imit.board[newx][y] = 0
            k_bool = True
        if k_bool:
            imitate.append(k_imit)
        f_imit = state.__copy__()
        f_bool = False
        for i, j in value:
            if on_board_or_not(x+i, y+j):
                if state.board[x+i][y+j] - state.whose_move == BC.INIT_TO_CODE['f']:
                    f_bool = True
                f_imit.frozen[state.whose_move].append((x + i,y + j))
        if f_bool:
            imitate.append(f_imit)
        w_imit = state.__copy__()
        if on_board_or_not(x0-i, y0-j)\
                and state.board[x0-i][y0-j] - state.whose_move == BC.INIT_TO_CODE['w']:
            w_imit.board[x0-i][y0-j] = 0
            imitate.append(w_imit)
    return imitate

def withdrawer_function(state, x, y, z_h):
    global ZOBRIST_M
    if on_board_or_not(x, y):
        z_h ^= ZOBRIST_N[8*x+y][state.board[x][y]]
        state.board[x][y] = 0
    state.static_eval()
    ZOBRIST_M[z_h] = z_node(state)
    return state

def king_function(state, x, y, x1, y1, z_h):
    global ZOBRIST_M
    if on_board_or_not(x,y) and on_board_or_not(x1, y1) and BC.who(state.board[x1][y1]) != BC.who(state.board[x][y]) or state.board[x1][y1] == 0:
        if state.board[x1][y1] != 0:
            z_h ^= ZOBRIST_N[8*x1+y1][state.board[x1][y1]]
        z_h ^= ZOBRIST_N[8*x1+y1][state.board[x][y]]
        z_h ^= ZOBRIST_N[8*x+y][state.board[x][y]]
        state.board[x1][y1] = state.board[x][y]
        state.board[x][y] = 0
        state.kingP[state.whose_move] = (x1, y1)
        state.static_eval()
        ZOBRIST_M[z_h] = z_node(state)
    return state

def on_board_or_not(x,y):
    return x >= 0 and y >= 0 and x <= 7 and y <= 7

if __name__ == "__main__":
    state = State(old_board=INITIAL_3, whose_move=WHITE)
    
    print(state)
    best_state=parameterized_minimax(state, False , 3 , False , True)
    print(best_state)
    '''
    now = datetime.now()
    new_state = IDDFS_function(state, now + timedelta(0, 10))
    print(new_state)
    
    tempa=()
    tempb=()
    for x in range (8):
        for y in range (8): 
            if(new_state.board[x][y] != state.board[x][y]):
                if(state.board[x][y] == 0):
                    tempa=(x,y)
                    tempx = x
                    tempy = y
                    #print('i am the first')
                    print(tempa)
    for xi in range (8):
        for yi in range (8):
            if(new_state.board[xi][yi] !=state.board[xi][yi]):
                if(new_state.board[tempx][tempy] == state.board[xi][yi]):
                        tempb=(xi,yi)
                        #print('i am the second')
                        print(tempb)
    print((tempb),(tempa))
   ''' 
                
