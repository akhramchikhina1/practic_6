counter_1, counter_2 = map(str,input().split('-'))
x=counter_1[0]
y=counter_2[0]
if x == a:
    a=str(1)
b=str(2)
c=str(3)
d=4
e=5
f=6
g=7
h=8
if (abs(int(counter_1[0])-int(counter_2[0]))==2 and abs(int(counter_1[0])-int(counter_2[0]))==1) or (abs(int(counter_1[0])-int(counter_2[0]))==1 and abs(int(counter_1[0])-int(counter_2[0]))==2):
    if (abs(int(counter_1[1]) - int(counter_2[1])) == 2 or abs(int(counter_1[1]) - int(counter_2[1])) == 1) or (abs(int(counter_1[1]) - int(counter_2[1])) == 1 or abs(int(counter_1[1]) - int(counter_2[1])) == 2):
        print('верно')
    else:
        print('ошибка')
else:
    print('ошибка')
