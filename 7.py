k= int(input())
'''if k<5:
    print('нет')
else:
    if (k%7)>0:
        if (k % 7) ==5:
            print('да')
        elif (k % 7) < 5:
            print('нет')'''

if k<5:
    print('нет')
elif k%5==0 or k%7==0:
    print('да')
elif k % 7 < 5:
    if (k % 7) % 5 == 0:
        print('да')
    else:
        print('нет')
else:
    if (k%5)%7==0:
        print('да')
    else:
        print('нет')

