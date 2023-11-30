# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
"""Para utilizar os metacaracteres dentro da expressão regular eu preciso utilizar a \, ou seja caso eu queira um ponto literal eu escrevo \."""
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
8aria 
'''

print(re.findall(r'João|Maria', texto)) # João ou Maria
"""['João', 'Maria', 'Maria']"""

print(re.findall(r'João|Maria|aqui', texto)) # João ou Maria ou aqui
"""['João', 'Maria', 'Maria', 'aqui']"""

"extra"
for indice, correspondencia in enumerate (re.finditer(r'João|Maria', texto)):
    inicio = correspondencia.start()
    fim = correspondencia.end()
    print(f"Correspondência {indice + 1}: Início={inicio}, Fim={fim}, Texto='{texto[inicio:fim]}'")

print(re.findall(r'João|Mar..|a.ui', texto)) # João ou Mar?? ou a?ui o . representa qualquer coisa exceto uma quebra de linha
"""['João', 'Maria', 'Maria', 'aqui']"""

print(re.findall(r'João|joão|Maria', texto))
"""['João', 'Maria', 'joão', 'Maria']"""

print(re.findall(r'[Jj]oão|Maria', texto)) # João ou Maria ou joão, [] conjunto de caracteres
"""['João', 'Maria', 'joão', 'Maria']"""

print(re.findall(r'[Jj]oão|[Mm]aria', texto)) # João ou Maria ou joão ou maria, [] conjunto de caracteres
"""['João', 'Maria', 'joão', 'maria', 'Maria']"""

print(re.findall(r'[a-zA-Z0-9]aria', texto))
"""['Maria', 'maria', 'Maria', '8aria']"""

print(re.findall(r'[a-zA-Z0-9]aria|[a-zA-Z0-9]oão', texto))
"""['João', 'Maria', 'joão', 'maria', 'Maria', 'ooão', '8aria']"""

# Flags mudam o comportamento das expressoes regulares

print(re.findall(r'jOÃo|mARia', texto, flags=re.IGNORECASE)) # Ignora case sensitive
"""['João', 'Maria', 'joão', 'maria', 'Maria']"""
print(re.findall(r'jOÃo|mARia', texto, flags=re.I)) # Ignora case sensitive
"""['João', 'Maria', 'joão', 'maria', 'Maria']"""
