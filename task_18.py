"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""
import random
N = int(input("Введите количество элементов массива: "))
A = []
for i in range(N):
    A.append(random.randint(1, 101))  #диапазон взят для примера
print(*A)
X = random.randint(1, 101)  #диапазон взят для примера
print(X)
Y = X
for i in range(N):
    if A[i] == X:
        print(f"-> {X}")
        break
while X!=A[i] or Y!=A[i]:
    X+=1
    Y-=1
    for i in range(N):
        if A[i] == X:
            print(f"-> {X}")
            break
        if A[i] == Y:
            print(f"-> {Y}")
            break
    if A[i] == X or A[i] == Y:
        break




 

