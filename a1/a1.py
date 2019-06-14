# three_x_cubed_plus_7(2) -> 31
def three_x_cubed_plus_7(x):
        return (3*x*x*x)+7

# triple_up
def triple_up(nums):
    chunks = [nums[x:x+3] for x in range(0, len(nums),3)] 
    return chunks
    
# mystery_code
def mystery_code(text):
    code =""
    offset=13
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                CH = chr(97 + (ord(ch) -65 + offset)%26)
            else:
                CH = chr(65 + (ord(ch) -97 + offset)%26)
        else:
            CH = ch

        code = code + CH
    return code

#future_tense
def future_tense(array):
    array1 = list(array)
    init = 0
    
    for i in range(len(array)):
        if (array[i]=='is')|(array[i]=='was')|(array[i]=='are')|(array[i]=='were')|(array[i]=='am')|(array[i]=='be'):
            array[i+init] = 'be'
            array1.insert(i+init,'will')
            init = init+1
        elif (array[i]=='Is')|(array[i]=='Was')|(array[i]=='Are')|(array[i]=='Were')|(array[i]=='Am')|(array[i]=='Be'):
            array1[i+init] = 'be'
            array1.insert(i+init,'Will')
            init = init+1
        elif (array[i]=='dose')|(array[i]=='did')|(array[i]=='do'):
            array1[i+init] = 'do'
            array1.insert(i+init,'will')
            init = init+1
        elif (array[i]=='Dose')|(array[i]=='Did')|(array[i]=='Do'):
            array1[i+init] = 'do'
            array1.insert(i+init,'Will')
            init = init+1
        elif (array[i]=='eats')|(array[i]=='ate')|(array[i]=='eat'):
            array1[i+init] = 'eat'
            array1.insert(i+init,'will')
            init = init+1
        elif (array[i]=='Eats')|(array[i]=='Ate')|(array[i]=='Eat'):
            array1[i+init] = 'eat'
            array1.insert(i+init,'Will')
            init = init+1
        elif (array[i]=='goes')|(array[i]=='went')|(array[i]=='go'):
            array1[i+init] = 'go'
            array1.insert(i+init,'will')
            init = init+1
        elif (array[i]=='Goes')|(array[i]=='Went')|(array[i]=='Go'):
            array1[i+init] = 'go'
            array1.insert(i+init,'Will')
            init = init+1
        elif (array[i]=='have')|(array[i]=='has')|(array[i]=='had'):
            array1[i+init] = 'have'
            array1.insert(i+init,'will')
            init = init+1
        elif (array[i]=='Have')|(array[i]=='Has')|(array[i]=='Had'):
            array1[i+init] = 'have'
            array1.insert(i+init,'Will')
            init = init+1
        elif (array[i]=='yesterday')|(array[i]=='today')|(array[i]=='now'):
            array1[i+init] = 'tomorrow'
        elif (array[i]=='Yesterday')|(array[i]=='Today')|(array[i]=='Now'):
            array1[i+init] = 'Tomorrow'
    return(array1)

        
        





