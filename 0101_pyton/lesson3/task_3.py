#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(n1 , n2, n3):
    if n1 >= n3 and n2 >= n3:
        return n1 + n2
    elif n1 > n2 and n1 < n3:
        return n1 + n3
    else:
        return n2 + n3

print(f'итог - {my_func(int(input("Введите первый аргумент ")), int(input("Введите второй аргумент ")), int(input("Введите третий аргумент ")))}')