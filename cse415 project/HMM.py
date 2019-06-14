import math
import weather_data
import GUI as gui

states = weather_data.states

observations = ('walk','shop','clean','boat')

start_probability = weather_data.start_probability

transition_probability = weather_data.transition_probability

 
emission_probability = {
    'Rainy' : {'walk': 0.19, 'shop': 0.15, 'clean': 0.5, 'boat':0.01},
    'Sunny' : {'walk': 0.5, 'shop': 0.15, 'clean': 0.05,'boat':0.3},
    'Cloudy' : {'walk': 0.3, 'shop': 0.3, 'clean': 0.2,'boat':0.2},
    'Partly Cloudy':{'walk': 0.2, 'shop': 0.2, 'clean': 0.3,'boat':0.3},
    'Smoke':{'walk': 0.01, 'shop': 0.05, 'clean': 0.93,'boat':0.01},
    }

def HMM_function(lst):
    day=[]
    day_dic={}
    for i in states:
        day+=[start_probability[i]*emission_probability[i][lst[0]]]
    day_dic[0]=day
    for i in range(1,len(lst)):
        temp=[]
        for k in range(5):
            temp1=0
            for m in range(5):
                temp_value= (day[m]*transition_probability[states[m]][states[k]])*emission_probability[states[k]][lst[i]]
                #print(temp_value)
                temp1 +=temp_value
            temp+=[temp1]
            #print(temp)
        day_dic[i]=temp
    return day_dic

def Viterbi(lst):
    HMM_List=[]
    Viterbi_dic=HMM_function(lst)
    for j in Viterbi_dic:
        i=Viterbi_dic[j]
        index_max=i.index(max(i))
        HMM_List+=[states[index_max]]
    return HMM_List

def probability(day_dic):
    for i in day_dic:
        pro=sum(day_dic[i])
    return pro

if __name__ == "__main__":
    print('Do your want to see defult test?')
    choose_input = input('Your input yes or no: ')
    if choose_input == 'yes':
        operation= ['walk','shop','boat','clean','walk','shop','boat','clean']
        probability = HMM_function(operation)
        viterbi = Viterbi(operation)
        print(viterbi)
        print(probability)
        gui.guiGenerate(operation, probability, viterbi)
    else:
        print('Please type your operation, use space as seperation')
        op_input = input('Your input operation: ')
        operation = op_input.split(' ')
        probability = HMM_function(operation)
        viterbi = Viterbi(operation)
        print(viterbi)
        print(probability)
        gui.guiGenerate(operation, probability, viterbi)