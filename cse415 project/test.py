import math
import weather_data
import GUI as gui

states = weather_data.states

observations = ('walk','shop','clean','boat')

start_probability = weather_data.start_probability
print(start_probability)
 
transition_probability = weather_data.transition_probability
 
emission_probability = {
    'Rainy' : {'walk': 0.19, 'shop': 0.15, 'clean': 0.5, 'boat':0.01},
    'Sunny' : {'walk': 0.5, 'shop': 0.15, 'clean': 0.05,'boat':0.3},
    'Cloudy' : {'walk': 0.3, 'shop': 0.3, 'clean': 0.2,'boat':0.2},
    'Partly Cloudy':{'walk': 0.2, 'shop': 0.2, 'clean': 0.3,'boat':0.3},
    'Smoke':{'walk': 0.01, 'shop': 0.05, 'clean': 0.93,'boat':0.01}
    }

def HMM_function(lst):
    day=[]
    for i in states:
        day+=[start_probability[i]*emission_probability[i][lst[0]]]
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
        day=temp
    return day

def Viterbi(lst):
    HMM_List=[]
    day=HMM_function([lst[0]])
    HMM_List+=[states[day.index(max(day))]]
    for i in range(1,len(lst)):
        temp=[]
        last_best_opinion=HMM_List[len(HMM_List)-1]
        index=states.index(last_best_opinion)
        for k in range(5):
            temp_value= transition_probability[states[index]][states[k]]*emission_probability[states[k]][lst[i]]
            temp+=[temp_value]
        #print(temp)
        HMM_List+=[states[temp.index(max(temp))]]
    return HMM_List

if __name__ == "__main__":
    print(HMM_function(['walk','shop']))