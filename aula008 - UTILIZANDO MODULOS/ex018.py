'''
import math
an = float(input('Digite o ângulo que você deseja: '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
ta = math.tan(math.radians(an))
print('O ângulo de {}  tem o SENO de {:.2f}'.format(an, se))
print('O ângulo de {}  tem o COSSENO de {:.2f}'.format(an, co))
print('O ângulo de {}  tem a TANGENTE de {:.2f}'.format(an, ta))
'''

from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
se = sin(radians(an))
co = cos(radians(an))
ta = tan(radians(an))
print('O ângulo de {}  tem o SENO de {:.2f}'.format(an, se))
print('O ângulo de {}  tem o COSSENO de {:.2f}'.format(an, co))
print('O ângulo de {}  tem a TANGENTE de {:.2f}'.format(an, ta))
