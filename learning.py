# # def vic(a, b):
# #     return  type(a) is str and type(b) is str

# # print(vic('4', '8'))


# # def id(a):
# #     if type(a) is str:
# #         return int(a)
# #     elif type(a) is float:
# #         return int(a)
# #     else:
# #         return a

# # value = [1,1,72,3,4,5]

# # print(value[2])
# # print(value)


# k = 9
# b = []
# # k += 100
# # # k = k + 1
# # print(k)
# while k < 50:
#     b.append(k)
#     k += 9

# print(b)


# def prod(valA):
#     r = 1

#     for x in valA:
#         r = r * x
#     return r

# L = prod(b)/7

# print(L)
# # # def naturalNumbers(n):
# # #     return list(range(1, n + 1))

# # # print(naturalNumbers(100))

# b = 'a b a'

# # c = int(len(b)/2)

# # print(b[:c])
# # print(b[::-1])

# def isPalindrome(S):
#     c = int(len(S)/2)
#     d = S[::-1]
#     if S[:c] == d[:c]:
#         return True
#     else:
#         return False


# def concat(valA, valB):
#     if type(valA) is str and type(valB) is int:
#         return valA + str(valB)
#     elif type(valA) is int and type(valB) is str:
#         return str(valA) + valB
#     elif type(valA) is float and type(valB) is str:
#         return str(valA) + valB
#     elif type(valA) is str and type(valB) is float:
#         return valA + str(valB)
#     else:
#         return valA + valB

# print(concat('abc', 5.5))


stl = ['bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn', 'Solarize_Light2', 'tableau-colorblind10', '_classic_test']


print(stl.index('seaborn-colorblind'))





# from matplotlib import pyplot as plt

# import numpy as np

stl = ['bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn', 'Solarize_Light2', 'tableau-colorblind10', '_classic_test']




# plt.style.use(stl[4])

a = [6, 12, 15, 24, 28, 35, 37, 42, 54, 60, 62, 72, 75, 84, 90, 96]

c = list(range(4, 67, 4))

d = list(range(5, 85, 5))

b = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

a.reverse()


plt.plot(b, a, '--', marker= 'o', label ='6 table')
plt.plot(b, c, label ='4 table')
plt.plot(b, d, label ='5 table')

plt.title('summa time pass')
plt.xlabel('Years')
plt.ylabel('Table')
plt.grid(True)
plt.legend()
plt.show()

# print(len(c))
# print(len(b))

