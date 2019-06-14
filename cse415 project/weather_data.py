''' 
All the weather raw data is from the weather channel webset 
https://weather.com/weather/monthly/l/Seattle+WA+USWA0395:1:US
the weather data is from the 5.27.2018 to 10.11.2018
Seattle, WA Monthly Weather
'''
#step0:gather the raw data
states = ('Rainy','Sunny','Cloudy','Partly Cloudy','Smoke')
weather ={'5.27':'Sunny',
'5.28':'Cloudy',
'5.29':'Cloudy',
'5.30':'Cloudy',
'5.31':'Cloudy',
'6.1':'Cloudy',
'6.2':'Partly Cloudy',
'6.3':'Partly Cloudy',
'6.4':'Cloudy',
'6.5':'Partly Cloudy',
'6.6':'Sunny',
'6.7':'Cloudy',
'6.8':'Cloudy',
'6.9':'Cloudy',
'6.10':'Partly Cloudy',
'6.11':'Partly Cloudy',
'6.12':'Partly Cloudy',
'6.13':'Cloudy',
'6.14':'Cloudy',
'6.15':'Partly Cloudy',
'6.16':'Partly Cloudy',
'6.17':'Sunny',
'6.18':'Sunny',
'6.19':'Sunny',
'6.20':'Partly Cloudy',
'6.21':'Cloudy',
'6.22':'Cloudy',
'6.23':'Cloudy',
'6.24':'Cloudy',
'6.25':'Cloudy',
'6.26':'Cloudy',
'6.27':'Partly Cloudy',
'6.28':'Cloudy',
'6.29':'Partly Cloudy',
'6.30':'Cloudy',
'7.1':'Cloudy',
'7.2':'Partly Cloudy',
'7.3':'Sunny',
'7.4':'Cloudy',
'7.5':'Sunny',
'7.6':'Partly Cloudy',
'7.7':'Cloudy',
'7.8':'Sunny',
'7.9':'Cloudy',
'7.10':'Cloudy',
'7.11':'Sunny',
'7.12':'Sunny',
'7.13':'Sunny',
'7.14':'Sunny',
'7.15':'Sunny',
'7.16':'Sunny',
'7.17':'Sunny',
'7.18':'Cloudy',
'7.19':'Cloudy',
'7.20':'Cloudy',
'7.21':'Sunny',
'7.22':'Sunny',
'7.23':'Sunny',
'7.24':'Sunny',
'7.25':'Sunny',
'7.26':'Sunny',
'7.27':'Sunny',
'7.28':'Partly Cloudy',
'7.29':'Sunny',
'7.30':'Sunny',
'7.31':'Sunny',
'8.1':'Cloudy',
'8.2':'Cloudy',
'8.3':'Cloudy',
'8.4':'Partly Cloudy',
'8.5':'Partly Cloudy',
'8.6':'Partly Cloudy',
'8.7':'Sunny',
'8.8':'Sunny',
'8.9':'Sunny',
'8.10':'Sunny',
'8.11':'Cloudy',
'8.12':'Cloudy',
'8.13':'Partly Cloudy',
'8.14':'Partly Cloudy',
'8.15':'Sunny',
'8.16':'Cloudy',
'8.17':'Cloudy',
'8.18':'Sunny',
'8.19':'Sunny',
'8.20':'Smoke',
'8.21':'Smoke',
'8.22':'Smoke',
'8.23':'Cloudy',
'8.24':'Cloudy',
'8.25':'Cloudy',
'8.26':'Cloudy',
'8.27':'Cloudy',
'8.28':'Sunny',
'8.29':'Partly Cloudy',
'8.30':'Cloudy',
'8.31':'Partly Cloudy',
'9.1':'Cloudy',
'9.2':'Sunny',
'9.3':'Partly Cloudy',
'9.4':'Sunny',
'9.5':'Sunny',
'9.6':'Sunny',
'9.7':'Partly Cloudy',
'9.8':'Cloudy',
'9.9':'Partly Cloudy',
'9.10':'Cloudy',
'9.11':'Partly Cloudy',
'9.12':'Cloudy',
'9.13':'Cloudy',
'9.14':'Cloudy',
'9.15':'Cloudy',
'9.16':'Cloudy',
'9.17':'Cloudy',
'9.18':'Partly Cloudy',
'9.19':'Partly Cloudy',
'9.20':'Cloudy',
'9.21':'Cloudy',
'9.22':'Partly Cloudy',
'9.23':'Partly Cloudy',
'9.24':'Sunny',
'9.25':'Sunny',
'9.26':'Cloudy',
'9.27':'Partly Cloudy',
'9.28':'Sunny',
'9.29':'Partly Cloudy',
'9.30':'Cloudy',
'10.1':'Rainy',
'10.2':'Partly Cloudy',
'10.3':'Partly Cloudy',
'10.4':'Partly Cloudy',
'10.5':'Rainy',
'10.6':'Cloudy',
'10.7':'Cloudy',
'10.8':'Rainy',
'10.9':'Cloudy',
'10.10':'Partly Cloudy',
'10.11':'Smoke',
}
lst=[]
for value in weather.values():
    lst.append(value)
#step 1: build the start_probability
Rainy,Sunny,Cloudy,Partly_Cloudy,Smoke=0,0,0,0,0
for i in lst:
    if i == states[0]:
        Rainy+=1
    elif i == states[1]:
        Sunny+=1
    elif i == states[2]:
        Cloudy+=1
    elif i == states[3]:
        Partly_Cloudy+=1
    elif i == states[4]:
        Smoke+=1
start_probability = {'Rainy': Rainy/len(lst),
'Sunny': Sunny/len(lst),
'Cloudy':Cloudy/len(lst),
'Partly Cloudy':Partly_Cloudy/len(lst),
'Smoke':Smoke/len(lst)}
# print(start_probability)
# sum_v=0
# for value in start_probability.values():
#     sum_v += value
# print(sum_v)

# step2:build the transition_probability
transition_probability = {
    'Rainy' : {'Rainy': 0, 'Sunny': 0,'Cloudy':0,'Partly Cloudy':0,'Smoke':0},
    'Sunny' : {'Rainy': 0, 'Sunny': 0,'Cloudy':0,'Partly Cloudy':0,'Smoke':0},
    'Cloudy': {'Rainy': 0, 'Sunny': 0,'Cloudy':0,'Partly Cloudy':0,'Smoke':0},
    'Partly Cloudy':{'Rainy': 0, 'Sunny': 0,'Cloudy':0,'Partly Cloudy':0,'Smoke':0},
    'Smoke':{'Rainy': 0, 'Sunny': 0,'Cloudy':0,'Partly Cloudy':0,'Smoke':0},
    }
for i in range(1,len(lst)):
    transition_probability[lst[i-1]][lst[i]]+=1
lst_value=[]
for i in states:
        lst_value+=[sum(transition_probability[i][j] for j in states)]
for i in range(len(states)):
    for j in states:
        transition_probability[states[i]][j]=transition_probability[states[i]][j]/lst_value[i]
#print(transition_probability)