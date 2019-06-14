'''farmer Fox problem.py
by jinlin xiang
2019-04-16
cse 415 spring
assignment 2
the object to move are farmer, fox, chicken, and grain
'''
PROBLEM_NAME ="farmerFox"
PROBLEM_VERSION="1.0"

#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>
# 0 IS THE STATE AT THE LEFT SIDE OF RIVER
# 1 IS THE STATE AT THE RIGHT SIDE OF RIVER
left = 0
right = 1
# all passenger are in an array
farmer = 0
fox = 1 
chicken = 2
grain = 3

class State():

  def __init__(self, d=None):
    if d == None:
       d = {'passenger':[[0,0],[0,0],[0,0],[0,0]],
           'boat':left}
    self.d = d

  def __eq__(self,s2):
    for prop in ['passenger', 'boat']:
      if self.d[prop] != s2.d[prop]: return False
    return True

  def __str__(self):
    # Produces a textual description of a state.
    p = self.d['passenger']
    txt = "\n Farmer on left:"+str(p[farmer][left])+"\n"
    txt += " Fox on left:"+str(p[fox][left])+"\n"
    txt += " Chicken on left:"+str(p[chicken][left])+"\n"
    txt += " Grain on left:"+str(p[grain][left])+"\n"
    txt += "   Farmer on right:"+str(p[farmer][right])+"\n"
    txt += "   Fox on right:"+str(p[fox][right])+"\n"
    txt += "   Chicken on right:"+str(p[chicken][right])+"\n"
    txt += "   Grain on right:"+str(p[grain][right])+"\n"
    side='left'
    if self.d['boat']==1: side='right'
    txt += " boat is on the "+side+".\n"
    return txt

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = State({})
    news.d['passenger']=[self.d['passenger'][ffcg][:] for ffcg in [farmer,fox,chicken,grain]]
    news.d['boat'] = self.d['boat']
    return news 

  def can_move(self,f1,f2,c,g):
    '''Tests whether it's legal to move .'''
    side = self.d['boat'] # Where the boat is.
    p = self.d['passenger']
    if(p[farmer][side] == 0): 
      return False 
    can_fox_move = p[fox][side]
    if can_fox_move < f2: 
      return False 
    can_chicken_move = p[chicken][side]
    if can_chicken_move < c: 
      return False 
    can_grian_move = p[grain][side]
    if can_grian_move < g: 
      return False
    if(f2==1): 
      if(p[fox][1-left] == p[chicken][left] and p[fox][1-left] != p[grain][left] and p[farmer][left] == p[fox][1-left]):
        return False
      if(p[chicken][left] == p[grain][left] and p[chicken][left] != p[fox][1-left]  and p[farmer][left] == p[chicken][left]):
        return False
    elif(c==1): 
      if(p[fox][left] == p[chicken][1-left]  and p[fox][left] != p[grain][left]  and p[fox][left] == p[farmer][left]):
        return False
      if(p[chicken][1-left] == p[grain][left] and p[chicken][1-left] != p[fox][left]  and p[chicken][1-left] == p[farmer][left]):
        return False
    elif(g==1):
      if(p[chicken][left] == p[grain][1-left] and p[chicken][left] != p[fox][left]   and p[chicken][left] == p[farmer][left]):
        return False
      if(p[fox][left] == p[chicken][left]  and p[fox][left] != p[grain][1-left] and p[fox][left] == p[farmer][left]):
        return False
    return True

  def move(self,f1,f2,c,g):
    '''Assuming it's legal to make the move, this computes
     the new state '''
    news = self.copy()      # start with a deep copy.
    side = self.d['boat']         # where is the boat?
    p = news.d['passenger']          # get the array of arrays of people.
    p[farmer][side] = p[farmer][side]-f1     # Remove people from the current side.
    p[fox][side] = p[fox][side]-f2
    p[chicken][side] = p[chicken][side]-c
    p[grain][side] = p[grain][side]-g

    p[farmer][1-side] = p[farmer][1-side]+f1 # Add them at the other side.
    p[fox][1-side] = p[fox][1-side]+f2
    p[chicken][1-side] = p[chicken][1-side]+c
    p[grain][1-side] = p[grain][1-side]+g
    news.d['boat'] = 1-side       # Move the boat itself.
    return news

    
def goal_test(s):
  '''If all are on the right, then s is a goal state.'''
  p=s.d['passenger']
  return (p[fox][right]==1 and p[chicken][right]==1 and p[grain][right]==1 and p[farmer][right]==1)

def goal_message(s):
  return "Congratulations on successfully guiding all across the river!"

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
CREATE_INITIAL_STATE =lambda: State(d={'passenger':[[1,0],[1,0],[1,0],[1,0]],'boat':left})
#</INITIAL_STATE>

#<OPERATORS>
ffgc_combinations =  [(1,0,0,0),(1,1,0,0),(1,0,1,0),(1,0,0,1)]
OPERATORS = [Operator(
  "Cross the river with "+str(fa)+" farmers, "+str(f)+" fox, "+str(c)+" chicken, and "+str(g)+" grain",
  lambda s, f1=fa, f2=f, c1=c, g1=g: s.can_move(f1,f2,c1,g1),
  lambda s, f1=fa, f2=f, c1=c, g1=g: s.move(f1,f2,c1,g1) ) 
  for (fa,f,c,g) in ffgc_combinations]
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>