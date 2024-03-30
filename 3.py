n, m = map(int, input('Введите размер района в формате NxM: ').split('x'))
k = int(input('Сколько кварталов нужно отделить?: '))
if (n * m) % 2 == 0:
    if ((n * m) - k) % 2 == 0:
        print('успешно')
    else:
        print('неосуществимо')
elif (((n * m) - k) % n == 0) or (((n * m) - k) % m == 0):
    print('успешно')
else:
    print('неосуществимо')



