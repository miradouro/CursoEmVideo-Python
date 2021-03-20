primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = primeiro + razao * 10
while primeiro != decimo:
    print(' {} →'.format(primeiro), end='')
    primeiro = primeiro + razao
print(' FIM')