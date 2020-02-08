# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt


# fl1 = pd.read_csv('gdp_pc.csv')
# fl2 = pd.read_csv('mlb_salaries_2014.csv')
# fl3 = pd.read_csv('disease_democ.csv')

# class stu:

#     def __init__(self, name, age, mark):
#         self.name = name
#         self.age = age 
#         self.mark = mark
    
#     def result(self):
#         if self.mark == 100:
#             print('hi', self.name, 'your pass!!!!')
#         else:
#             print('hi', self.name, 'your fail ;-(')



# s1 = stu('vicky', 22, 100)
# s2 = stu('nik', 23, 99)


# print(fl2.head())



# def pat():
#     val = 'vicky'
#     l = len(val)
#     for r in range(l):
        
#         for c in range(r + 1):
#             print ( val, end="")
        
#         print()        

# pat()


# fl2 = pd.read_csv('mlb_salaries_2014.csv')

# fl2_team = fl2.groupby('teamName').sum()
# # a = fl2_team.loc[fl2_team['salary_mil'] > 100,'salary_mil']

# print(fl2_team.loc['teamName'])

# plt.bar( fl2['teamName'], fl2['salary'])

# plt.title('summa time pass')
# plt.xlabel('Team')
# plt.ylabel('Salary')
# plt.grid(True)
# plt.legend()
# plt.show()


v = 1


print(f'done : {v}')
