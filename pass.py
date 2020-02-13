import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv


fl1 = pd.read_csv('passwords.csv')
# fl2 = pd.read_csv('mlb_salaries_2014.csv')
# fl3 = pd.read_csv('disease_democ.csv')

revF = fl1['name']

csv_file = open('scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name','count'])


a = []
c = 0
for i in revF:
    b= str(i)[::-1]
    b= b.split('.')
    b=str(b[1])[::-1]
    c+=1
    # a.append(b)
    csv_writer.writerow([b, c])    
    
csv_file.close()

print('don')
# print(len(a))
