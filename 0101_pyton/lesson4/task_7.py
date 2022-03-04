#7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
#Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(n):
    count = 1
    while count <= n:
        yield count
        count += 1
i = 1
my_fifteen = []
for el in fact(4):
    if i > 24:
        break
    else:
        my_fifteen.append(el)
        i += 1
print(my_fifteen)