x = 4
y = 11

#operator bitwise OR (|)
z = x|y
print('a.')
print('Nilai : ',x, ', Binary : ', format(x,'08b'))
print('Nilai : ',y, ', Binary : ', format(y,'08b'))
print('----------------------------------------------------(|)')
print('Hasil dari 4|11 : ',z, ', dalam biner : ', format(z,'08b'),'\n')

#operator bitwise right shift (>>)
z = x>>y
print('b.')
print('Nilai : ',x, ', Binary : ', format(x,'08b'))
print('Nilai : ',y, ', Binary : ', format(y,'08b'))
print('----------------------------------------------------(>>)')
print('Hasil dari 4>>11 : ',z, ', dalam biner : ', format(z,'08b'),'\n')

#operator bitwise XOR (^)
z = x^y
print('c.')
print('Nilai : ',x, ', Binary : ', format(x,'08b'))
print('Nilai : ',y, ', Binary : ', format(y,'08b'))
print('----------------------------------------------------(^)')
print('Hasil dari 4^11 : ',z, ', dalam biner : ', format(z,'08b'),'\n')

#operator bitwise NOT (~)
z = ~x
print('d.')
print('Nilai : ',x, ', Binary : ', format(x,'08b'))
print('----------------------------------------------------(~)')
print('Hasil dari ~4 : ',z, ', dalam biner : ', format(z,'08b'),'\n')

#operator bitwise AND (&)
z = y&x
print('e.')
print('Nilai : ',x, ', Binary : ', format(x,'08b'))
print('Nilai : ',y, ', Binary : ', format(y,'08b'))
print('----------------------------------------------------(&)')
print('Hasil dari 11&4 : ',z, ', dalam biner : ', format(z,'08b'))