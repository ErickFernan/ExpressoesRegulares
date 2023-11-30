# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $ -> passa a representar começo da linha e fim da linha
# re.S -> Dotall \n -> reconhece as quebras de linha
import re

texto = '''
131.768.460-53
055.123.060-50
955.123.060-90
'''

print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto, flags=re.M))
"""
['131.768.460-53', '055.123.060-50', '955.123.060-90']
"""

texto = '''
131.768.460-53
055.123.060-50 AS
955.123.060-90EE
'''

print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto, flags=re.M))
"""
['131.768.460-53']
"""


texto2 = '''O João gosta de folia 
E adora ser amado'''
print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))
"""
['O João gosta de folia \nE adora ser amado']
"""
