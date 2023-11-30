# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto
import re

# Funções
# findall -> Todas ocorrências
# search -> Primeira ocorrência (retorna um objeto match)
# sub -> Substituir algo no texto
# compile -> Compilar expressoes regulares, muito útil quando precisar reutilizar a expressão regular

string = 'Este é um teste de expressões teste regulares.'

                                   # o r permite que utilizemos \(simples) para escapar algum caracter ou para executar algum meta caracter
                                   # expressão regular em pytho segue o modelo: r'expressaoregular'
print(re.search(r'teste', string)) # busca teste dentro de string
"""<re.Match object; span=(10, 15), match='teste'>"""

print(re.search(r'teste2', string)) 
"None"""

print(re.findall(r'teste', string))
"""['teste', 'teste']"""

print(re.findall(r'teste2', string))
"""[]"""

print(re.sub(r'teste', 'ABCD', string))
"""Este é um ABCD de expressões ABCD regulares."""

print(re.sub(r'teste', 'ABCD', string, count=1)) # count = 0 troca todas, é o padrão
"""Este é um ABCD de expressões teste regulares."""

# Teste e teste são diferentes para as expressões regulares

regexp = re.compile(r'teste') # Compila a expressão que será utilizada mais de uma vez
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('ABCD',string))

"""
<re.Match object; span=(10, 15), match='teste'>
['teste', 'teste']
Este é um ABCD de expressões ABCD regulares.
"""
