### CSE 415 - SPRING 2019 
### Assianment 1
### JINLIN XIANG
###### MIAN FUNCTION ##############
""" main funciton
- function introduce(to dialog function)
- function agentname(to dialog function)
- function mian--jinlin
- fucniton response 
"""
from random import choice
from re import *

all_res = 0 #total_responses
GREATING =False
defaulted = False
random_responded =False
this_is_single_world=False
MEMORY=False
cycle_counter = 0
cyc=0
# def the name of agent
def agentName():
    return "jinlin"

# def the introduce function
def introduce():
    return ("Hi! I am jinlin xiang , I want to buy sometings. ." +\
            "\n I was programmed by jinlin xiang. If you don't like" +\
            "\nthe way I deal, contact her at jinlinx@uw.edu"+\
            "\nHow can I help you?")

# main function
def jinlin():
    introduce()
    while True:
        this_input = input('TYPE HERE:>> ')
        print(respond(this_input))  #

def respond(this_input):
    global GREATING
    global defaulted 
    global random_responded
    global this_is_single_world
    global all_res
    global MEMORY
    all_res += 1


    # wordlist, mapped_wordlist
    wordlist, mapped_wordlist = process(this_input)
    # r1 : greeting
    if GREATING == False and all_res <= 2:
        if wordlist in GREETING:
            GREATING = True
            return "HI! Nice to meet you！"
    # try the remember for futurn use 
    memory_remember_mark(mapped_wordlist)
    # r2: empty input
    res = empty_word(wordlist, mapped_wordlist)
    if res != False:
        return res
    # r3: sigle input
    if this_is_single_world == False:
        res = single_word_rule(wordlist, mapped_wordlist)
        if res != False:
            this_is_single_world = True
            return res

    # r4: answer the where/ why/ when ... question
    res = w_rule(wordlist, mapped_wordlist)
    if res!=False:
        return res
    # r5: if have the word i am return you are
    if wordlist[0:2] == ['i','am']:
        res="Please tell me why you are " +\
              stringify(mapped_wordlist[2:]) + '.'
        return res
    # r6: if have i have return you had
    if wordlist[0:2] == ['i','have']:
        res="How long have you had " +\
              stringify(mapped_wordlist[2:]) + '.'
        return res
    # r7: if have i fell return same way
    if wordlist[0:2] == ['i','feel']:
        res="I sometimes feel the same way."
        return res
    # r8: if have becuase return reason
    if 'because' in wordlist:
        res = "Is that really the reason?"
        return res
    #r9：options keywords
    res = keyword(wordlist, mapped_wordlist)
    if res!=False:
        return res
    # r10: answer the question (to a new dialog)
    if wordlist[0] in ['okay', 'ok']:
        res=("would you like " + choice(DRINKS))
        return res
    #r11: memory recall
    if MEMORY == False and all_res > 4:
        res = recall_memory_remember_mark()
        if res != False:
            MEMORY = True
            return res
    # r11:try to be plite
    if 'please' in wordlist:
        res=("You are so nice.")
        return res
    # r12 ： answer the question
    if 'see' in wordlist:
        res=("Would you want to konw more about it?")
        return res
    # r12 ： answer the question
    if 'maggie' in wordlist:
        res=("hello Maggie, would like -"+(DRINKS)+'?')
        return res
    
    # r14:defult test
    defaulted = True
    return default_response()
    # r15: random test
    if random_responded == False and defaulted == True:
        random_responded = True
        return random_response()

## words collection
GOODBYE = ['Bye', 'Goodbye','bye']
GREETING = ['hey', 'hi', 'hello']
DRINKS = ['Coke Cola', 'Pepsi', 'Spite', 'Fanta', 'MiRiNDA','7 UP', 'Mountain Dew', 'Minute Maid']
Vegetables = ['potato','tomato','broadbeans','broccoli','cabbage',\
          'carrot','cauliflower','cucumber','garlic','ginger','roots',\
          'kale']

# r1 function: greeting function
def greeting_rules(wordlist, mapped_wordlist):
    if wordlist in GREETING:
        greet = choice(GREETING).capitalize()  + "! "
        return greet

# r2 function: empty input
def empty_word(wordlist, mapped_wordlist):
    if wordlist[0] == '':
        return "Please say something?"
    else:
        return False

#r3 function: answer the where/ why/ when ... question
def w_rule(wordlist, mapped_wordlist):
    w = wordlist[0]
    global cyc
    if wpred(w):  # Why, Where, How, When
        options = [" indeed.. ",
                 "could you repeat your queation?",
                "I don't know the answer, please ask jinlinx@uw.edu for more information.",
                "could recommend anything?",
                "pick "+choice(Vegetables) ]
        cyc=cyc+1
        return options[cyc%5]
    return False

# read the w
def wpred(w):
    'if queation, return ture '
    return (w in ['when', 'why', 'where', 'how', 'what'])
 # SINGLE WORD
def single_word_rule(wordlist, mapped_wordlist):
        if len(wordlist) == 1:
            return "just a signgle word, what do you mean" + wordlist[0] + " ?"
        return False
def keyword(wordlist, mapped_wordlist):
    options = []
    #option 1
    if 'like' in wordlist:
        options.append(" wow, you like it, would you like to talk more about it?.")

    #option 2
    if 'dislike' in wordlist or 'hate' in wordlist:
        options.append(" can we have a cup of  " + choice(DRINKS) )

    #option 3
    if 'yes' in wordlist:
        options.append("let us do it")

    #option 4
    if 'idea' in wordlist:
        options.append("wolud you like to talk to jinlin")
    #option 5
    if 'sure' in wordlist:
        options.append("why? please give me some reasons")
    if 'Today' in wordlist:
        options.append("What you want to do today?")
    if 'yeseterday' in wordlist:
        options.append("What did you do yesterday?")
    if 'feel' in wordlist:
        temp=["i am happy right now!","you are so nice if you do it!"]
        options.append(choice(temp))
    if 'indicate' in wordlist:
        options.append("i need more information. ")

    # just selcet one
    if len(options) > 0:
        return choice(options)

    return False


# r15 : if repeat reponse 
def default_response():
    global cycle_counter
    attitude = choice(['like', 'love','want to buy','would like some'])
    Vegetables = ['potato','tomato','broadbeans','broccoli','cabbage',\
          'carrot','cauliflower','cucumber','garlic','ginger','roots',\
          'kale']
    response = "I "+attitude+" "+ Vegetables[cycle_counter%12]+"."
    cycle_counter =cycle_counter +1
    return response


def stringify(wordlist):
    'Create a string from wordlist, but with spaces between words.'
    return ' '.join(wordlist)
# r16 : random test 
def random_response():
        ans= ["I'm trying to recall your name.. could you say it again",
                      "Could you say it anagin?",
                      "I missed your point,colud you say it angin!",
                      "would you want a cup of-"+choice(DRINKS) ]
        return choice(ans)
'''
build the memor for the funciton
'''
# build a momerry_space
momerry_space = []

def  memory_remember_mark(mapped_wordlist):
    momerry_space.append(stringify(mapped_wordlist))

"""reshow the stored things afer several turns """
#recall
def recall_memory_remember_mark():
    if len(momerry_space) < 1:
        return "You have not say things that is worth remembering"

    formerremark = choice(momerry_space[:-1])
    retrunmark = ("You earlier said " + formerremark+". Would you like talk it right now?")
    return retrunmark

'''
## other funciton use
# fucntion process
# function remove_punctuation
# you_me_map
# you_me

'''

# fucntion process
def process(this_input):
    for g in GOODBYE:
        if match(g, this_input):
            print('See you! GoodBye.')

    wordlist = split(' ', remove_punctuation(this_input))


    # undo any initial capitalization:
    wordlist[0] = wordlist[0].lower()
    mapped_wordlist = you_me_map(wordlist)

    mapped_wordlist[0] = mapped_wordlist[0].capitalize()

    return (wordlist, mapped_wordlist)

    
punctuation_pattern = compile(r"\,|\.|\?|\!|\;|\:")

def remove_punctuation(text):
    'Returns a string without any punctuation.'
    return sub(punctuation_pattern, '', text)

def you_me_map(wordlist):
    'Applies YOU-ME to a whole sentence or phrase.'
    return [you_me(w) for w in wordlist]
def you_me(w):
    ##'Changes a word from 1st to 2nd person or vice-versa.'
    try:
        result = CASE_MAP[w]
    except KeyError:
        result = w
    return result
CASE_MAP = {'i': 'you', 'I': 'you',
            'me': 'you', 'you': 'me',
            'my': 'your', 'your': 'my',
            'yours': 'mine', 'mine': 'yours',
            'am': 'are',
            'myself': 'yourself',
            'yourself': 'myself'}

######################################################
# launch the program
if __name__ == "__main__":
    jinlin()
###########################################################