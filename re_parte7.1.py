# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A ou re.ASCII -. se utlizar esta flag o comportamento sera o mesmo que em javascript, por exemplo
# \W -> [^a-zA-Z0-9À-ú_]                      |
# \W -> [^a-zA-Z0-9_] -> re.A ou re.ASCII     | o W maiusculo representa a negação
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t] -> qualquer tipo de espaço
# \S -> [^ \r\n\f\n\t]
# \b -> borda -> Geralmente encontra string vazia no começo ou no fim de cada palavra
# \B -> não borda

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

# print(re.findall(r'[^ ]+', texto)) # Minha ideia inicial antes de ver a aula
"""
['\nJoão', 'trouxe', 'flores', 'para', 'sua', 'amada', 'namorada', 'em', '10', 'de', 'janeiro', 'de', '1970,\nMaria', 'era', 'o', 'nome', 'dela.\n\n\nFoi', 'um', 'ano', 
'excelente', 'na', 'vida', 'de', 'joão.', 'Teve', '5', 'filhos,', 'todos', 'adultos', 'atualmente.\nmaria,', 'hoje', 'sua', 'esposa,', 'ainda', 'faz', 'aquele', 'café', 
'com', 'pão', 'de', 'queijo', 'nas', 'tardes', 'de\ndomingo.', 'Também', 'né!', 'Sendo', 'a', 'boa', 'mineira', 'que', 'é,', 'nunca', 'esquece', 'seu', 'famoso\npão', 'de', 
'queijo.\nNão', 'canso', 'de', 'ouvir', 'a', 'Maria:\n"Joooooooooãooooooo,', 'o', 'café', 'tá', 'prontinho', 'aqui.', 'Veeemm', 'veeem', 'veem', 'vem"!\n8aria', 
'\njozoaosoasãoooooooooo\njsssssssssãoooooooooo\n']
"""

# print(re.findall(r'[a-z]+', texto, flags=re.I))
"""
['Jo', 'o', 'trouxe', 'flores', 'para', 'sua', 'amada', 'namorada', 'em', 'de', 'janeiro', 'de', 'Maria', 'era', 'o', 'nome', 'dela', 'Foi', 'um', 'ano', 'excelente', 
'na', 'vida', 'de', 'jo', 'o', 'Teve', 'filhos', 'todos', 'adultos', 'atualmente', 'maria', 'hoje', 'sua', 'esposa', 'ainda', 'faz', 'aquele', 'caf', 'com', 'p', 'o', 
'de', 'queijo', 'nas', 'tardes', 'de', 'domingo', 'Tamb', 'm', 'n', 'Sendo', 'a', 'boa', 'mineira', 'que', 'nunca', 'esquece', 'seu', 'famoso', 'p', 'o', 'de', 'queijo', 
'N', 'o', 'canso', 'de', 'ouvir', 'a', 'Maria', 'Jooooooooo', 'ooooooo', 'o', 'caf', 't', 'prontinho', 'aqui', 'Veeemm', 'veeem', 'veem', 'vem', 'aria', 'jozoaosoas', 
'oooooooooo', 'jsssssssss', 'oooooooooo']
"""

# print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
"""
['João', 'trouxe', 'flores', 'para', 'sua', 'amada', 'namorada', 'em', '10', 'de', 'janeiro', 'de', '1970', 'Maria', 'era', 'o', 'nome', 'dela', 'Foi', 'um', 'ano', 
'excelente', 'na', 'vida', 'de', 'joão', 'Teve', '5', 'filhos', 'todos', 'adultos', 'atualmente', 'maria', 'hoje', 'sua', 'esposa', 'ainda', 'faz', 'aquele', 'café', 
'com', 'pão', 'de', 'queijo', 'nas', 'tardes', 'de', 'domingo', 'Também', 'né', 'Sendo', 'a', 'boa', 'mineira', 'que', 'é', 'nunca', 'esquece', 'seu', 'famoso', 'pão', 
'de', 'queijo', 'Não', 'canso', 'de', 'ouvir', 'a', 'Maria', 'Joooooooooãooooooo', 'o', 'café', 'tá', 'prontinho', 'aqui', 'Veeemm', 'veeem', 'veem', 'vem', '8aria', 
'jozoaosoasãoooooooooo', 'jsssssssssãoooooooooo'
"""

# Short range para re.findall(r'[a-zA-Z0-9À-ú]+', texto)
# print(re.findall(r'\w+', texto)) # inclue caracteres da maioria dos idiomas, lembrando que sem o + ele irá pegar letra por letra
"""
['João', 'trouxe', 'flores', 'para', 'sua', 'amada', 'namorada', 'em', '10', 'de', 'janeiro', 'de', '1970', 'Maria', 'era', 'o', 'nome', 'dela', 'Foi', 'um', 'ano', 
'excelente', 'na', 'vida', 'de', 'joão', 'Teve', '5', 'filhos', 'todos', 'adultos', 'atualmente', 'maria', 'hoje', 'sua', 'esposa', 'ainda', 'faz', 'aquele', 'café', 
'com', 'pão', 'de', 'queijo', 'nas', 'tardes', 'de', 'domingo', 'Também', 'né', 'Sendo', 'a', 'boa', 'mineira', 'que', 'é', 'nunca', 'esquece', 'seu', 'famoso', 'pão', '
de', 'queijo', 'Não', 'canso', 'de', 'ouvir', 'a', 'Maria', 'Joooooooooãooooooo', 'o', 'café', 'tá', 'prontinho', 'aqui', 'Veeemm', 'veeem', 'veem', 'vem', '8aria', 
'jozoaosoasãoooooooooo', 'jsssssssssãoooooooooo']
"""

# print(re.findall(r'\w+', texto, flags=re.A)) # n pega o full unicode, apenas a tabela ASCII
"""
['Jo', 'o', 'trouxe', 'flores', 'para', 'sua', 'amada', 'namorada', 'em', '10', 'de', 'janeiro', 'de', '1970', 'Maria', 'era', 'o', 'nome', 'dela', 'Foi', 'um', 'ano', 
'excelente', 'na', 'vida', 'de', 'jo', 'o', 'Teve', '5', 'filhos', 'todos', 'adultos', 'atualmente', 'maria', 'hoje', 'sua', 'esposa', 'ainda', 'faz', 'aquele', 'caf',
 'com', 'p', 'o', 'de', 'queijo', 'nas', 'tardes', 'de', 'domingo', 'Tamb', 'm', 'n', 'Sendo', 'a', 'boa', 'mineira', 'que', 'nunca', 'esquece', 'seu', 'famoso', 'p', 'o', 
 'de', 'queijo', 'N', 'o', 'canso', 'de', 'ouvir', 'a', 'Maria', 'Jooooooooo', 'ooooooo', 'o', 'caf', 't', 'prontinho', 'aqui', 'Veeemm', 'veeem', 'veem', 'vem', '8aria', 
 'jozoaosoas', 'oooooooooo', 'jsssssssss', 'oooooooooo']
"""

# print(re.findall(r'\d+', texto, flags=re.I))
"""
['10', '1970', '5', '8']
"""

# print(re.findall(r'\s+', texto, flags=re.I))
"""
['\n', ' ', '    ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', '\n\n\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
'\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', '\n', ' ', ' ', 
' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' \n', '\n', '   \n']
"""

# print(re.findall(r'\S+', texto, flags=re.I))
"""
['João', 'trouxe', 'flores', 'para', 'sua', 'amada', 'namorada', 'em', '10', 'de', 'janeiro', 'de', '1970,', 'Maria', 'era', 'o', 'nome', 'dela.', 'Foi', 'um', 'ano', 
'excelente', 'na', 'vida', 'de', 'joão.', 'Teve', '5', 'filhos,', 'todos', 'adultos', 'atualmente.', 'maria,', 'hoje', 'sua', 'esposa,', 'ainda', 'faz', 'aquele', 'café', 
'com', 'pão', 'de', 'queijo', 'nas', 'tardes', 'de', 'domingo.', 'Também', 'né!', 'Sendo', 'a', 'boa', 'mineira', 'que', 'é,', 'nunca', 'esquece', 'seu', 'famoso', 'pão', 
'de', 'queijo.', 'Não', 'canso', 'de', 'ouvir', 'a', 'Maria:', '"Joooooooooãooooooo,', 'o', 'café', 'tá', 'prontinho', 'aqui.', 'Veeemm', 'veeem', 'veem', 'vem"!', '8aria', 
'jozoaosoasãoooooooooo', 'jsssssssssãoooooooooo']
"""

print(re.findall(r'\bflo\w+', texto, flags=re.I)) # Exemplo, quero encontrar todas as palavras que comecem com flo
"""
['flores']
"""

print(re.findall(r'\be\w+', texto, flags=re.I)) # Exemplo, quero encontrar todas as palavras que comecem com e
"""
['em', 'era', 'excelente', 'esposa', 'esquece']
"""

print(re.findall(r'\w+e\b', texto, flags=re.I)) # Exemplo, quero encontrar todas as palavras que terminem com e
"""
['trouxe', 'de', 'de', 'nome', 'excelente', 'de', 'Teve', 'atualmente', 'hoje', 'aquele', 'de', 'de', 'que', 'esquece', 'de', 'de']
"""

print(re.findall(r'\b\w{4}\b', texto, flags=re.I)) # Exemplo, quero encontrar todas as palavras que tenham 4 letras
"""
['João', 'para', '1970', 'nome', 'dela', 'vida', 'joão', 'Teve', 'hoje', 'café', 'café', 'aqui', 'veem']
"""

print(re.findall(r'flor\B', texto, flags=re.I))
"""
['flor']
"""
