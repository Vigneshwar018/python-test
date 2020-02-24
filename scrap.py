from bs4 import BeautifulSoup as bs
import requests
import os
import pandas as pd
import glob

#agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


#url = requests.get('https://www.cricketcountry.com/players/shaheedur-rahman/', headers=agent).text

#scr = bs(url, 'lxml')
a=[1,2,3,6,7,8,9,1,2,3,4,5,6,7]
b=[22,33,44,1,2,55,6,77]
c =2
#deb = scr.select_one('div:nth-of-type(4) > aside:nth-of-type(2) > p:nth-of-type(1)')

#odi = scr.select_one('div:nth-of-type(2) > aside:nth-of-type(1) > p:nth-of-type(1)').text

# deb = scr.select_one('section.stat > div > aside:nth-child(1) > p.col-xs-12.col-sm-2').text
#name = scr.find(class_="ply-info-dis", itemprop="name").get_text().strip()

# a = 1
# b = 1

path = 'icc'
fl = glob.glob(os.path.join(path, '*.csv'))

li =[]

for f in fl:
	df = pd.read_csv(f)
	df['Team'] = df['Team'][0]
	li.append(df)

excfl = pd.concat(li, ignore_index=True)

excfl.to_csv('all_player.csv', index=False)