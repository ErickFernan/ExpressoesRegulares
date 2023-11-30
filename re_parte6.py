# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação, se utilizado dentro do conjunto


import re

cpf = 'a 121.346.916-38'
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
# ['121.346.916-38']

cpf = 'a 121.346.916-38'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
# []

cpf = '121.346.916-38 outro'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
# ['121.346.916-38']

cpf = '121.346.916-38 outro'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf)) # a minha expressão começa e termina deste jeito, de qualquer outra forma não irá funcionar
# []

cpf = '121.346.916-38'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
# ['121.346.916-38']

print(re.findall(r'[^a-z]', cpf))
# ['1', '2', '1', '.', '3', '4', '6', '.', '9', '1', '6', '-', '3', '8']

print(re.findall(r'[^a-z]+', cpf))
# ['121.346.916-38']

print(re.findall(r'[^0-9]', cpf))
# ['.', '.', '-']

print(re.findall(r'[^0-9]+', cpf))
# ['.', '.', '-']
