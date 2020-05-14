'''Типы операций над файлами
Открыть для чтения r  --Read
Открыть для записи w  --Write
Открыть для дозаписи a  --Append
Откыть бинарный файл b  --Binary
'''
from os import path
'''try:
    test_file = open('learning/file.txt', 'a')
    try:
        test_file.write('\nasbdkjbaksd')
    except Exception as e:
        print(e)
    finally: 
        test_file.close()
        
except PermissionError:
        print("Ошибка доступа")'''

try:
    test_file = open('learning/file.txt', 'r')
    #Считывание в консоль
    '''for line in test_file:
        print(line, end="")'''
    '''line = test_file.readline()
    while line:
        print(line, end='')
        line = test_file.readline()'''
    '''content = test_file.read()
    print(content)'''
    content = test_file.readlines()
    print(content)
    
except Exception as e:
    print(e)



    

