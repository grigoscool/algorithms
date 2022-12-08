from random import * 

n = randint(1,100)
count = 0
print('Добро пожаловать в числовую угадайку')

def is_valid(x):

    if x.isdigit() and 0 <= int(x) <= 100:
        return True
    else:
        return False
  
flag = True
while flag:
    y = input('Введите число от 0 до 100')

    if is_valid(y):
        y = int(y)
        if y < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
        elif y > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
        elif y == n:
            print('Вы угадали, поздравляем!')
            count += 1
            flag = False
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        
print(F'За {count} попыток Вы угадали число. \nСпасибо, что играли в числовую угадайку. Еще увидимся...')
