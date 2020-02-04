from bs4 import BeautifulSoup as bs
import requests

# url = requests.get('https://webscraper.io/test-sites/e-commerce/allinone').text

agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

url = requests.get('https://www.zomato.com/chennai/hotel-city-park-1-porur/order', headers=agent).text


# url2 = requests.get('https://www.amazon.in/dp/B07HGMQX6N?pf_rd_p=fa25496c-7d42-4f20-a958-cce32020b23e&pf_rd_r=35W3QDYGFHDVK1D4QZWD').text

scr = bs(url, 'lxml')


for pro in scr.find_all(class_="thumbnail"):

    pros = pro.find(class_="title")

    print(pros.text)
    
    dis = pro.find(class_="description")

    print(dis.text)

    price = pro.find(class_="pull-right price")

    print(price.text)

# print(scr)

