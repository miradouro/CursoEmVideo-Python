from utilidades import numeros
import aulaUteis

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {aulaUteis.dobro(num)}')
