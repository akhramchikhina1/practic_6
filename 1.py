a, b= map(int, input().split('x'))
diagonal_s=(a**2+b**2)**0.5
diametr=6.5+6.5
if diametr>diagonal_s:
    print('да')
else:
    print('нет')