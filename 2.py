a, b= map(int, input().split('x'))
c, d, e= map(int, input().split('x'))
if min(a,b) >= min(c,d,e):
    if max(a,b) >= max(c,d,e):
        print('да')
    else:
        print('нет')
else:
    print('нет')