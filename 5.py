klet = input() 
alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8} 
if (abs(alphabet[klet[0]] - alphabet[klet[3]]) + abs(alphabet[klet[1]] - alphabet[klet[4]])) == 3: 
    print('верно') 
else: 
    print('неверно')
