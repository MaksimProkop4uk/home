from random import randint
lst = [randint(0, 100) for i in range(100)]
#print(lst)
n = int(input('введите число из диапазона (0-100): '))
print(lst, lst.count(n), sep = '\n')