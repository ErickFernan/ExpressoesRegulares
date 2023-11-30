# Meta caracteres: ^ $ ( )

# Quantificadores:
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
# {n}
# {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+

# Os quantificadores podem ser aplicados em conjuntos

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
8aria 
jozoaosoasãoooooooooo
jsssssssssãoooooooooo
'''

print(re.findall(r'jOÃo', texto, flags=re.I))
"""['João', 'joão']"""

"""
Como mostrar para a expresão regular que Joooooooooãooooooo pode ser um tipo de joao?
"""

print(re.findall(r'jo+ão', texto, flags=re.I)) # neste exemplo o primeiro o deve existir de 1 a n vezes devido ao uso do quantificador +
"""['João', 'joão', 'Joooooooooão']"""

print(re.findall(r'jo+ão+', texto, flags=re.I))
"""['João', 'joão', 'Joooooooooãooooooo']"""

print(re.sub(r'jo+ão+', 'Erick', texto, flags=re.I))
"""
Erick trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de Erick. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Erick, o café tá prontinho aqui. Veeemm"!
8aria 
"""

print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I)) # 1 ou n, mesma função do +
"""['João', 'joão', 'Joooooooooãooooooo']"""

print(re.findall(r'jo+ão+', texto, flags=re.I))
"""['João', 'joão', 'Joooooooooãooooooo']"""

print(re.findall(r've{3}m{1,2}', texto, flags=re.I))
"""['Veeemm', 'veeem']"""

print(re.findall(r'j[a-zA-Z]+ão+', texto, flags=re.I))
"""['João', 'joão', 'Joooooooooãooooooo', 'jozoaosoasãoooooooooo', 'jsssssssssãoooooooooo']"""
