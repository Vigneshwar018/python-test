from bs4 import BeautifulSoup as bs
import requests
import itertools
import pandas as pd
# import re 

# url = requests.get('https://webscraper.io/test-sites/e-commerce/allinone').text

agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


url2 = requests.get('https://www.cricketcountry.com/players/', headers=agent).text

scr2 = bs(url2, 'lxml')

# icc_file = pd.read_csv('icc-odi.csv')

# all player scraping

link_team = { 'ind':'796', 'nz':'992', 'sa':'1235', 'eng':'681', 'aus':'20', 'pak': '263', 'sl':'320', 'wi':'1356' ,'ban':'523', 'zim':'407', 'nel':'426', 'uae':'365', 'sct':'312', 'ire':'156' , 'hk':'145', 'afg':'1589' }

test_player =  pd.read_csv('icc/exc/exc_all_player.csv')

player_link = scr2.select(f'#tabcontent_{link_team["nz"]} > div > ul > li > a[href^="https://www.cricketcountry.com/players/"]')

a =[]
for i in player_link:
    b = i.get_attribute_list('href')
    if b[0] in test_player['Link'].values:
    	pass
    else:	
    	a.append(b[0])

# url = requests.get('https://www.cricketcountry.com/players/datta-gaekwad/', headers=agent).text

# scr = bs(url, 'lxml')


# odi = scr.select('div:nth-of-type(2) > aside:nth-of-type(1) > p:nth-of-type(2)')

# print(odi == [])
print (len(a))
icc = []

col = ['Name', 'Date of birth', 'Team', 'Batting Style', 'Bowling Style', 'ODI Debut', 'Debut Team', 'ODIs matach', 'Matches played', 'Innings', 'Total Run', 'Not Out', 'Highe Score', 'Batting Avg', 'Balls faced', 'Stick rate', '100s', '50s', '4s', '6s', 'Caught', 'Stumped', 'ODIs matach 2', 'Matches played 2','Balls', 'Runs', 'Wickets', 'Bowling Avg', 'Economy', 'Stick rate', '5WI', '10WM', 'BBI', 'BBM']

exclue_list = []
#lol = [1,2]
v = 0
s = 0
en = 150
#playre profile
for i in a:
    url = requests.get(i , headers=agent).text

    scr = bs(url, 'lxml')

    try:
        odi = scr.select_one('div:nth-of-type(2) > aside:nth-of-type(1) > p:nth-of-type(1)').text
    except AttributeError as e:
        odi = 'test'
    try:
    	deb = scr.select_one('section.stat > div > aside:nth-child(1) > p.col-xs-12.col-sm-2').text
    except AttributeError as e:
        deb = 'test'
        
    if deb == 'ODI Debut':
    	
        d = 1
    else:
        d = 2
     
    try:
        dob = scr.find(itemprop="birthDate").get_text().strip()
    except AttributeError as e:
        dob = None       

    if (deb == 'ODI Debut' or odi == 'ODI Debut') and (dob != None):
        name = scr.find(class_="ply-info-dis", itemprop="name").get_text().strip()
        
        	

        team = scr.select_one('div > aside > section:nth-of-type(4)> aside > a').get_text().upper().strip()
           
        try:
            batting_style = scr.select_one('div > aside > section:nth-of-type(5)> aside:nth-of-type(2)').get_text().strip()
        except AttributeError as e:
            
            batting_style = 'NaN'

        try:    
            bowling_style = scr.select_one('div > aside > section:nth-of-type(6)> aside:nth-of-type(2)').get_text().strip()
        except AttributeError as e:
            
            bowling_style = 'NaN'

        odi_batting = scr.select_one('tr:nth-of-type(2)').get_text()

        batting_list = str(odi_batting).split('\n')

        # using list comprehension to 
        # perform removal

        batting_list = [i for i in batting_list if i]



        odi_bowling = scr.select('tr:nth-of-type(3)')[1].get_text()

        bowling_list = str(odi_bowling).split('\n')

        # using list comprehension to 
        # perform removal

        bowling_list = [i for i in bowling_list if i]

        frist_match = scr.select(f'div:nth-of-type({d}) > aside:nth-of-type(1) > p:nth-of-type(2)')[0].get_text()


        frist_match = str(frist_match).split(',')

        match_date = frist_match[-2].strip()+ ',' +frist_match[-1].strip()

        frist_team = frist_match[0].split(' at')[0]

        full_list = [[name, dob, team, batting_style, bowling_style, match_date, frist_team], batting_list, bowling_list]

        full_list = list(itertools.chain(*full_list))

        icc.append(full_list)
        
        v += 1

        print(v, name)
    
    else:
    	try:
    		name = scr.find(class_="ply-info-dis", itemprop="name").get_text().strip()
    	except AttributeError:
    		name = None
    	exclue_list.append([name,i])
    	v += 1
    	#team = 'lol'
    	print(v,i)
df = pd.DataFrame(icc, columns = col)

df.drop(['ODIs matach','ODIs matach 2', 'Matches played 2'], axis=1, inplace = True)

df.to_csv(f'icc/{team.lower()}-player.csv', index=False)

df2 = pd.DataFrame(exclue_list, columns = ['Name' , 'Link'])

df2.to_csv(f'icc/exc/{team.lower()}-player-exc.csv', index=False)


print(f'done!: {v}')