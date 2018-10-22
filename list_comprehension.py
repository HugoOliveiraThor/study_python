# -*- coding: utf-8 -*-
# List Comprehension
# Em Python, você pode criar listas rapidamente e de forma concisa com compreensão de listas. 
# Este exemplo anterior: 

# capitalized_cities = []
# for city in cities:
#     capitalized_cities.append(city.title())

# pode ser reduzido para :

# capitalized_cities = [city.title() for city in cities]

# Compreensão de listas nos permite criar uma lista usando um loop for em uma única etapa.
# Você cria uma compreensão de listas com colchetes [], incluindo uma expressão a ser avaliada para cada elemento em um iterável. 
# Esta compreensão de lista acima puxa city.title() de cada elemento city em cities, 
# para criar cada elemento na lista nova, capitalized_cities. 

# Condicionais na compreensão de listas
# Você também pode adicionar condicionais para compreensão de listas (listcomps). 
# Após o iterável, você pode usar a palavra-chave if para verificar uma condição em cada iteração.

squares = [x**2 for x in range(9) if x % 2 == 0]
print("Squares {}".format(squares))

# O código acima define squares como a lista [0, 4, 16, 36, 64], já que x para a potência de 2 é avaliada somente se x for par. 
# Se você quiser adicionar um else, receberá um erro de sintaxe fazendo isso.

# squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3] --> invalida syntax

# Se quiser adicionar else, você deve mover condicionais para o início de listcomp, logo após a expressão, desta forma.
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print("Squares with elses {}".format(squares))

# Compreensão de listas não é encontrada em outras linguagens, mas é muito comum em Python.