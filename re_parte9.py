# ranges numéricos

import re
# op -> 0.0.0.0 até 255.255.255.255
# 025.258.963-10 02525896310

# Teste essa expressão
# em https://regex101.com/r/lWVPOr/1
cpf = '025.258.963-10'

"""
relembrando:
^ -> começa com
$ -> termina com
"""
# Validando o CAMPO de cpf, não um cpf qualquer no texto ou o cpf em si, apenas o formato
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
print(cpf_reg_exp.search(cpf))
"""
<re.Match object; span=(0, 14), match='025.258.963-10'>
"""

# Validando o ip
ip_reg_exp = re.compile(
    r'^'  # Começa com
    r'(?:'
    r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.'
    r'){3}'  # Sequência de 3 digitos e um ponto repete 3x
    r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])'
    r'$',  # Termina com
    flags=0
)

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip,ip_reg_exp.findall(ip))
