# arr = [234, 1234, 56, 2, 0, 76]
'''    0     1    2   3  4  5   6  7  8  9'''
''' Вам дан готовый список чисел:
    1.вывести первую половину списка
    2.вывести вторую половину списка
    3.Изменить все числа в массиве на + 1
    4.Выведите все числа, которые меньше 5
'''
# for i in range(len(arr)):
#     if arr[i] < 5:
#         print(arr[i])    








# print(len(arr))
# print(arr[:len(arr)])
# print(arr[:len(arr)//2])










'''  '''
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13]
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#             c.append(a[i])
# print(c)

'''
    Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
'''
# arr = [123, 345, 423, 678, 56, '345', '23']
# for i in range(len(arr)):
#     if type(arr[i]) == int:
#         arr[i] = str(arr[i])
#     elif type(arr[i]) == str:
#         arr[i] = int(arr[i])
# print(arr)
'''
    Напишите код, который переводит целое число в строку.
'''
# a = list(map(int, input().strip().split()))
# b = list(map(int, input().strip().split()))
'''
    Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.    
'''
text = input()
d = {}
'''
    Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
'''
for i in text.split():
    if len(i)>max_len:
        max_len = len(i)
        max_len_w = i
    if i not in d:
        d[i] = 0
    else:
        d[i] += 1
max_word = 0
for i in d.items():
    for j in d.items():
        if i != j:
            if i[1] > j[1]:
                max_word = i
print(max_len_w, max_word[0])
