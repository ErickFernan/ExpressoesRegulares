import re
from pprint import pprint


texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
"""
['192.168.0.1',
 '192.168.0.2',
 '192.168.0.3',
 '192.168.0.4',
 '192.168.0.5',
 '192.168.0.6']
 """

pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(\w+)', texto))
"""
[('192.168.0.1', 'active'),
 ('192.168.0.2', 'inactive'),
 ('192.168.0.3', 'active'),
 ('192.168.0.4', 'active'),
 ('192.168.0.5', 'inactive'),
 ('192.168.0.6', 'active')]
"""

# Positive lookeahead -> Imagine que eu queria apenas checar se a palavra na expressão é 'active'
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))
"""
['192.168.0.1', '192.168.0.3', '192.168.0.4', '192.168.0.6']
"""

# Negative lookeahead -> Imagine que eu queria apenas checar se a palavra na expressão NÃO é 'active'
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))
"""
['192.168.0.2', '192.168.0.5']
"""

# Positive lookeahead, nesse caso estou falando para que ele procure as linhas que tenham inactive
pprint(re.findall(r'(?=.*inactive).+', texto))
"""
['OFFLINE  192.168.0.2 GHIJK inactive', 'ONLINE  192.168.0.5 GHIJK inactive']
"""

# Positive lookeahead, nesse caso estou falando para que ele procure as linhas que tenham active mas existe um problema
pprint(re.findall(r'(?=.*active).+', texto))
"""
['ONLINE  192.168.0.1 GHIJK active',
 'OFFLINE  192.168.0.2 GHIJK inactive',
 'OFFLINE  192.168.0.3 GHIJK active',
 'ONLINE  192.168.0.4 GHIJK active',
 'ONLINE  192.168.0.5 GHIJK inactive',
 'OFFLINE  192.168.0.6 GHIJK active']
"""

# Positive lookeahead, nesse caso estou falando para que ele procure as linhas que tenham active, negando o in
pprint(re.findall(r'(?=.*[^in]active).+', texto))
"""
['ONLINE  192.168.0.1 GHIJK active',
 'OFFLINE  192.168.0.3 GHIJK active',
 'ONLINE  192.168.0.4 GHIJK active',
 'OFFLINE  192.168.0.6 GHIJK active']
"""

# Positive lookbehind ?<= -> Checando as linhas que possuem o ONLINE
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
"""
['192.168.0.1', '192.168.0.4', '192.168.0.5']
"""

# Negative lookbehind ?<! -> Checando as linhas que não possuem o ONLINE
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
"""
['192.168.0.2', '192.168.0.3', '192.168.0.6']
"""

# Lembrando apenas que o PLA, NLA, PLB e NLB só verificam se existe a palavra mas não retornam nada
