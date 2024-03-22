kletka=input()
if kletka[0] == 'a' or  kletka[0] == 'c' or  kletka[0] == 'e' or  kletka[0] == 'g':
    if int(kletka[1])%2==0:
        print('белый')
    else:
        print('черный')
else:
    if int(kletka[1])%2==0:
        print('черный')
    else:
        print('белый')
