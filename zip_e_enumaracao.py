# -*- coding: utf-8 -*-
# Zip
# zip retorna um iterador que combina múltiplos iteráveis em uma sequência de tuplas.
# Cada tupla contém os elementos nessa posição de todos os iteráveis. Por exemplo, exibindo
resultZip = list(zip(['a', 'b', 'c'], [1, 2, 3]))
print("Result list zip: {}".format(resultZip))

# Result : [('a', 1), ('b', 2), ('c', 3)]
# Como fizemos para range(), precisamos converter em uma lista ou iterar por meio dela com um loop para ver os elementos.

# Você pode desempacotar cada tupla em um loop for como este.

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("Tupla em um loop -> {}: {}".format(letter, num))

# Além de compactar duas listas juntas, você também pode descompactar uma lista usando um asterisco.
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
print("Descompactando duas listas -> {}: {}".format(letters, nums))

# Enumerate
# enumerate é uma função interna que devolve um iterador de tuplas contendo índices e valores para um lista. 
# Você vai usar isso muitas vezes quando quiser o índice junto a cada elemento de um iterável em um loop.
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
    print("letters {}".format(letters))    

# Quiz: Coordenadas zip
# Use zip para gravar um loop for que cria uma string especificando o rótulo e as coordenadas de cada ponto e acrescenta à lista points. 
# Cada string deve ser formatada como label: x, y, z. Por exemplo, a string para a primeira coordenada deve ser F: 23, 677, 4.
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
# points = list(zip(labels, x_coord, y_coord, z_coord))
for point in list(zip(labels, x_coord, y_coord, z_coord)):
    points.append("{}:{},{},{}".format(*point))

# O asterico *points significa que ele vai pegar todos os elementos e descompactar dentro do format ex: format(labels, x_coord, y_coord, z_coord)
for point in points:
    print(point)

# Quiz: Listas zip para dicionário
# Use zip para criar um dicionário cast que usa names como chave e heights como valores.
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
zipped = list(zip(cast_names, cast_heights))
cast = dict(zipped)
print(cast)

# Quiz: Tuplas descompactadas
# Descompacte a tupla cast em duas tuplas, names e heights.

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = zip(*cast)
print("Descompactando duas listas -> {}: {}".format(names, heights))

print(names)
print(heights)


# Quiz: Transposição com zip
# Use zip para transpor data de uma matriz 4 por 3 para uma matriz 3 por 4. 
# Na verdade, existe um truque legal para isso! Fique à vontade para olhar para as soluções, caso não consiga descobrir.
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

# Quiz: Enumerate
# Use enumerate para modificar a lista cast para que cada elemento contenha o nome seguido da altura correspondente do personagem. 
# Por exemplo, o primeiro elemento de cast deve mudar de "Barney Stinson" para "Barney Stinson 72".
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
teste = list(zip(cast, heights))
# write your for loop here

for i, singleElement in enumerate(teste):
    cast[i] = cast[i]+" "+ str(heights[i])
print(cast)