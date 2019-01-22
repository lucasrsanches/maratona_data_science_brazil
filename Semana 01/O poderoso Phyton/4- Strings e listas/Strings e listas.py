frase = 'Oi, tudo bem?'
lista_nomes = ['Joao', 'Maria', 'Guilherme', 'Diego']
lista_nomes.append('Geralda')
lista_nomes.remove('Joao')
lista_nomes.insert(1, 'Lucas')
lista_nomes[1] = ('Roberto')
contador = lista_nomes.count('Diego')

print(lista_nomes)
print(contador)
print(len(frase))  # conta as strings
print(frase.lower())  # deixa tudo minusculo
print(frase.split(','))
print(frase + 'Como vai voce?')
