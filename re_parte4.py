# Meta caracteres: ^ $ ( )
# quantificadores Greedy e Non Greedy(lazy)
# Gredy(Gulosos):
# * 0 ou n
# + 1 ou n
# ? 0 ou 1

import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> <div></div> 
'''

print(re.findall(r'<[dpiv]{1,3}>.+<\/[dpiv]{1,3}>', texto))
print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto))
"""
['<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>'] # Comportamendo greedy
['<p>Frase 1</p>', '<p>Eita</p>', '<p>Qualquer frase</p>', '<div>1</div>'] # Comportamendo non greedy (?)

.*? (ponto asterisco de não-greedy):

? após o * torna o quantificador * "não-greedy" ou "relutante". Isso significa que tentará corresponder ao mínimo possível de caracteres.
Portanto, .*? corresponde à menor sequência possível de caracteres (também incluindo nenhuma sequência).

A diferença principal entre .* e .*? surge quando há várias correspondências possíveis na string de entrada. O .* tentará corresponder o máximo possível de caracteres, 
enquanto .*? tentará corresponder o mínimo possível.
"""

print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto))
print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto))
"""
['<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> <div></div>']
['<p>Frase 1</p>', '<p>Eita</p>', '<p>Qualquer frase</p>', '<div>1</div>', '<div></div>'] # Com o * é encontrado a div vazia
"""
# Outro exemplo:

"""
>>> texto= 'abcdeabeabcde'
>>> re.findall(r'a.*e',texto)
['abcdeabeabcde']
>>> re.findall(r'a.*?e',texto)
['abcde', 'abe', 'abcde']



o caractere ? possui uso independente em expressões regulares, além de sua função em quantificadores "não-greedy" (relutantes), como discutido anteriormente.

1. Correspondência Opcional:

Você pode usar o ? para indicar que o caractere ou grupo anterior é opcional, o que significa que ele pode aparecer zero ou uma vez na string de entrada. Por exemplo:

A expressão regular colou?r corresponderá tanto a "color" quanto a "colour", pois o u é opcional.
2. Quantificador de Negação:

O ? também pode ser usado como um quantificador de negação em algumas implementações de expressões regulares. Nesse contexto, [^...] corresponde a qualquer caractere 
que não esteja na lista dentro dos colchetes. O ? pode aparecer imediatamente após o ^ para indicar negação. Por exemplo:

A expressão regular [^0-9]? corresponde a qualquer caractere que não seja um dígito.
Estes são apenas alguns exemplos do uso independente do caractere ? em expressões regulares. A versatilidade do ? torna-o útil em várias situações para expressar 
condições de correspondência específicas.
"""
