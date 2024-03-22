a, b= map(int, input().split('x'))
c, d, e= map(int, input().split('x'))
if min(a,b) >= min(c,d):
    if max(a,b) >= max(c,d):
        print('да')
    else:
        print('нет')
else:
    print('нет')