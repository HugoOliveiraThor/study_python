# -*- coding: utf-8 -*-
# Zip
# zip retorna um iterador que combina múltiplos iteráveis em uma sequência de tuplas.
# Cada tupla contém os elementos nessa posição de todos os iteráveis. Por exemplo, exibindo
teste = list(zip(['a', 'b', 'c'], [1, 2, 3]))
print(teste)
# Result : [('a', 1), ('b', 2), ('c', 3)]
# Como fizemos para range(), precisamos converter em uma lista ou iterar por meio dela com um loop para ver os elementos.

# Você pode desempacotar cada tupla em um loop for como este.

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))