#  Grupos e retrovisores
# 
# Meta caracteres: ^ $
# grupos:       retrovisor:
# ()            \1
# () ()         \1 \2
# (())          \1 \2
# (())()        \1 \2 \3
#
# (abc) -> deve encontrar especificamente abc
# (abc|def) -> deve encontrar especificamente abc ou def
# pode ser utilizado quantificadores
# os grupos são salvos em memória, então é possível acessa-lo

import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> <div></div> 
'''

print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto))
# ['<p>Frase 1</p>', '<p>Eita</p>', '<p>Qualquer frase</p>', '<div>1</div>']

print(re.findall(r'<([dpiv]{1,3})>.+?<\/\1>', texto)) # Foi criado um grupo que contem um conjunto e no \1 foi acessado sua posição em memória
# ['p', 'p', 'p', 'div']
# o findall junto com o grupo, retorna apenas somente o que está em grupo

# Para resolver vc pode envolver tudo em um grupo porém o modo de acesso será alterado e deverá ser utilizado o chamado retrovisor
# Um modo de facilitar a contagem do retrovisor é contar a abertura de parenteses (
print(re.findall(r'(<([dpiv]{1,3})>.+?<\/\2>)', texto))
# [('<p>Frase 1</p>', 'p'), ('<p>Eita</p>', 'p'), ('<p>Qualquer frase</p>', 'p'), ('<div>1</div>', 'div')]
# Observe que é retonado de forma diferente, sendo em tuplas, onde a primeira resposta é o primeiro grupo e a segunda o segundo grupo

tags = re.findall(r'(<([dpiv]{1,3})>.+?<\/\2>)', texto)

for tag in tags:
    print(tag)
"""
('<p>Frase 1</p>', 'p')
('<p>Eita</p>', 'p')
('<p>Qualquer frase</p>', 'p')
('<div>1</div>', 'div')
"""

for tag in tags:
    um, dois = tag
    print(um)

# Caso eu queria apenas pegar o valor dentro da tag, eu posso criar outro grupo:
tags = re.findall(r'(<([dpiv]{1,3})>(.+?)<\/\2>)', texto)

for tag in tags:
    um, dois, tres = tag
    print(tres)

"""
Frase 1
Eita
Qualquer frase
1
"""

# Caso eu queria criar um grupo, mas os valores deles não importam e eu não desejo salvar seus valores: '?:'

tags = re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto)
print(tags)
# [('p', 'Frase 1'), ('p', 'Eita'), ('p', 'Qualquer frase'), ('div', '1')]

tags = re.findall(r'<([dpiv]{1,3})>(?:.+?)<\/\1>', texto)
print(tags)
# ['p', 'p', 'p', 'div']

cpf = '121.346.916-38'
print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))
# ['121.346.916-38']

cpf = '121.346.916-38'
print(re.findall(r'([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}', cpf))
# ['346.']

cpf = '121.346.916-38'
print(re.findall(r'(([0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
# [('121.346.916-38', '346.')]

cpf = '121.346.916-38'
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
# ['121.346.916-38']


# Em Python pode-se nomear o grupo:

tags = re.findall(r'<(?P<nometag>[dpiv]{1,3})>(.+?)<\/\1>', texto)
print(tags)
# [('p', 'Frase 1'), ('p', 'Eita'), ('p', 'Qualquer frase'), ('div', '1')]

tags = re.findall(r'<(?P<nometag>[dpiv]{1,3})>(.+?)<\/(?P=nometag)>', texto)
print(tags)
# [('p', 'Frase 1'), ('p', 'Eita'), ('p', 'Qualquer frase'), ('div', '1')]


print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"\3"\4', texto))
# <p>"Frase 1"</p> <p>"Eita"</p> <p>"Qualquer frase"</p> <div>"1"</div> <div></div> 
