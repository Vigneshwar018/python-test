from bs4 import BeautifulSoup as bs
import requests
import re 

# url = requests.get('https://webscraper.io/test-sites/e-commerce/allinone').text

agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


url2 = requests.get('https://www.cricketcountry.com/players/', headers=agent).text


scr2 = bs(url2, 'lxml')


# all player scraping

player_link = scr2.select('#tabcontent_796 > div > ul > li:nth-of-type(1) > a[href^="https://www.cricketcountry.com/players/"]')

a =[]
for i in player_link:
    b = i.get_attribute_list('href')
    a.append(b[0])

# url = requests.get('https://www.cricketcountry.com/players/datta-gaekwad/', headers=agent).text

# scr = bs(url, 'lxml')


# odi = scr.select('div:nth-of-type(2) > aside:nth-of-type(1) > p:nth-of-type(2)')

# print(odi == [])


#playre profile
for i in a:
    url = requests.get(i, headers=agent).text

    scr = bs(url, 'lxml')

    odi = scr.select('div:nth-of-type(2) > aside:nth-of-type(1) > p:nth-of-type(2)')

    if odi != [] :
        name = scr.find(class_="ply-info-dis", itemprop="name").get_text().strip()

        # name = name.strip()

        dob = scr.find(itemprop="birthDate").get_text().strip()

        team = scr.select_one('div > aside > section:nth-of-type(4)> aside > a').get_text().upper().strip()
        try:
            batting_style = scr.select_one('div > aside > section:nth-of-type(5)> aside:nth-of-type(2)').get_text().strip()
        except AttributeError as e:
            
            batting_style = 'NaN'

        try:    
            bowling_style = scr.select_one('div > aside > section:nth-of-type(6)> aside:nth-of-type(2)').get_text().strip()
        except AttributeError as e:
            
            bowling_style = None

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

        frist_match = scr.select('div:nth-of-type(2) > aside:nth-of-type(1) > p:nth-of-type(2)')[0].get_text()


        frist_match = str(frist_match).split(',')

        match_date = frist_match[-2]+ ',' +frist_match[-1]

        frist_team = frist_match[0].split(' v')[0]

        print([name, dob, team, batting_style, bowling_style, match_date, frist_team, batting_list, bowling_list])
    



