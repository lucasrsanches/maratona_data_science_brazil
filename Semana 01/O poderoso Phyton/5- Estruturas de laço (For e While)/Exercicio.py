pessoas = input('Informe a quantidade de convidados:')
pessoas = int(pessoas)
i = 0
lista_nomes = []

while i < pessoas:
    nomes = input('Informe os nomes:')
    lista_nomes.append(nomes)
    i += 1

print('Serão', pessoas, 'convidados')

for nome in lista_nomes:
    print(nome)
