from bs4 import BeautifulSoup as bs
import requests
import os
import pandas as pd
import glob
import json

agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

h = 0

dic = []
col = ['category', 'type', 'difficulty', 'question', 'correct_answer', 'in1', 'in2', 'in3' ] 
while h <= 75:
    url = requests.get('https://opentdb.com/api.php?amount=50', headers=agent).text
    
    scr = bs(url, 'lxml')
    
    api = scr.select_one('p').text
    
    api2 = api.replace('{', 'r~ ').replace('},', '').replace(']}]}', ']}').replace('":"',':').replace('":',':')#.replace('"','')
    
    api2 = api2.split('r~ ')
    
    
    di = {'category':[], 'type':[] } 
    k = 0
    for i in api2:
        
        if k > 1:
            i = i.replace('{','').replace('}','').replace('[', '').replace(']', '')#.replace('"','')
            i = i.split('","')
           # print(i) 
            if i in dic:
                pass
            else:
                dic.append(i)
        k += 1
    
    #dict['results'].append(di)
    print(h)
    h += 1

print(len(dic))    
    
df = pd.DataFrame(dic, columns=col)


#li = pd.concat(df, ignore_index=True)


#df.to_json('api-quiz.json', orient = 'records')

#df = df.replace('"','')

df['category'] = df['category'].str.replace('"', '')
df['in1'] = df['in1'].str.replace('"','') 
df['in3'] = df['in3'].str.replace('"', '')

deb = df['category'].apply(lambda x: x.split(':'))
deb2 = df['type'].apply(lambda x: x.split(':'))
deb3 = df['difficulty'].apply(lambda x: x.split(':'))
deb4 = df['question'].apply(lambda x: x.split(':'))
deb5 = df['correct_answer'].apply(lambda x: x.split(':'))
deb6 = df['in1'].apply(lambda x: x.split(':'))

def ch(x):
    if len(x) == 3:
        return f'{x[1]}:{x[2]}'
    else :
        return x[1]

df['category'] = deb.apply(ch)
df['type'] = deb2.apply(ch) 
df['difficulty'] = deb3.apply(ch) 
df['question'] = deb4.apply(ch) 
df['correct_answer'] = deb5.apply(ch) 
df['in1'] = deb6.apply(ch)


df['incorrect_answers'] = df[['in1', 'in2', 'in3']].values.tolist()
df['incorrect_answers'] = df['incorrect_answers'].apply(lambda x : [i for i in x if i]) 

df.drop(df.iloc[:, 5:8], inplace = True, axis = 1)

li2 = {'results' : [df]} 
df2 = pd.DataFrame(li2) 


df2.to_json('api-quiz-2.json', orient = 'records',force_ascii='False')



#deb = scr.select_one('div:nth-of-type(4) > aside:nth-of-type(2) > p:nth-of-type(1)')

#odi = scr.select_one('div:nth-of-type(2) > aside:nth-of-type(1) > p:nth-of-type(1)').text

# deb = scr.select_one('section.stat > div > aside:nth-child(1) > p.col-xs-12.col-sm-2').text
#name = scr.find(class_="ply-info-dis", itemprop="name").get_text().strip()

# a = 1
# b = 1

#path = 'icc'
#fl = glob.glob(os.path.join(path, '*.csv'))

#li =[]

#for f in fl:
#	df = pd.read_csv(f)
#	df['Team'] = df['Team'][0]
#	li.append(df)

#excfl = pd.concat(li, ignore_index=True)

#print(excfl)

#excfl.to_csv('all_player.csv', index=False)