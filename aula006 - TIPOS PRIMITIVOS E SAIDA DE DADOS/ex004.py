e = input('Digite algo: ')
print('O tipo primitivo desse numero é', type(e))
print('Só tem espaços?', e.isspace())
print('É um numero?', e.isnumeric())
print('É alfabetico?', e.isalpha())
print('É alfanumerico?', e.isalpha() | e.isnumeric())
print('Está em maiusculas?', e.isupper())
print('Está em minusculas', e.islower())
print('Está capitalizada?', e.istitle())
