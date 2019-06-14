def minimax_function_helper(state, depth, operation, endTime):
    if is_over_time(endTime):
        return None
    if depth == 0:
        state.static_eval()
        return state
    state.static_eval()
    board = state.board
    child_states = []
    s = None
    time.sleep(0.1)
    s = z_node(state)
    if len(s.children) == 0:
        child_states = get_child_states(state, h)
    heapq.heapify(child_states)
    best = None
    best_eval = 0
    while len(child_states) != 0:
        c_state = heapq.heappop(child_states)
        # Time check
        if is_over_time(endTime):
            break
        new_state = minimax_function_helper(c_state, depth-1, -operation, endTime, alpha, beta)
        if new_state != None:
            new_eval = new_state.eval
        else:
            new_eval = 0
        if best == None:
            best = new_state
            best_eval = new_eval
        elif operation*new_eval >= operation*best_eval:
            best = new_state
            best_eval = new_eval
    return best


    global alphaBeta
    if alphaBeta = True
    now = datetime.now()
    new_state = IDDFS_function(state, now + timedelta(0, 10))
    print(new_state)

    h = hash_z(state.board)
    child_states = []
    s = None
    try:
        s = ZOBRIST_M[h]
    except:
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
        if alpha > beta:
            break
        new_state = minimax_function_helper(c_state, depth - 1, -operation, endTime,alpha, beta)
        if new_state != None:
            new_eval = new_state.eval
        else:
            new_eval = 0
        if operation == 1:
            # set alpha
            alpha = max(alpha, new_eval)
        else:
            # set beta
            beta = min(beta, new_eval)
        if best == None or operation*new_eval >= operation*best_eval:
            best = c_state
            best_eval = new_eval
    return best
     
