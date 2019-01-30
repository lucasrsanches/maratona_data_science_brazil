nomes = ['Guilherme', 'Marcelo', 'Joao', 'Julia']

'''for i in nomes:
    print(i)'''

'''for item in range(4): #range= lista, porém pode ocorrer erro se o tamanho for maior que a variavel
    print(nomes[item])'''

for x in range(len(nomes)):  # len= usa o tamanho exato da lista e transforma em inteiro
    print(nomes[x])

palavra = 'Lucas'

for letra in palavra:
    print(letra)
