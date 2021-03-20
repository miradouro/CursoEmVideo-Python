n1 = float(input('Qual a largura da parede?\n'))
n2 = float(input('Qual a altura da parede?\n'))
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m².'.format(n1, n2, n1*n2))
print('Para pintar sua parede, você precisará de {}l de tinta.'.format((n1*n2)/2))
