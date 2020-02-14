from bs4 import BeautifulSoup as bs
import requests


agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


url = requests.get('https://www.cricketcountry.com/players/faizan-asif/', headers=agent).text

scr = bs(url, 'lxml')

deb = scr.select_one('div:nth-of-type(4) > aside:nth-of-type(2) > p:nth-of-type(1)')

#odi = scr.select_one('div:nth-of-type(2) > aside:nth-of-type(1) > p:nth-of-type(1)').text

# deb = scr.select_one('section.stat > div > aside:nth-child(1) > p.col-xs-12.col-sm-2').text


# a = 1
# b = 1

# if a == 1 or b == 0:
#     print('done')
# else:
#     print('fail')

print(deb)
