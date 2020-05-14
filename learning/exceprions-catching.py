
try:
    num1 = int(input("ВВедите  первое число целое: "))
    num2 = int(input("ВВедите  второе число целое: "))
    print("Ваше число: ", num1/num2)
except ValueError as e:
    print("Вы ввели не корретное значение: ", e)
except ZeroDivisionError as e:
    print("Ошибка деления на 0: ", e)
finally:
    print('Завершение программы')
    