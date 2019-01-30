# List (lista). Usa de forma ordenada e flexível (é possível alterar)
minha_lista = ['Gui', 'Joao']
# Tuple (tupla). Usa de forma ordenada porém não-flexível (não é alteravel)
minha_tupla = ('Gui', 'Joao')
meu_dicionario = {'nome': 'Guilherme', 'idade': 27}  # Dict (dicionario)
meu_conjunto = {'Gui', 'Joao'}  # Set (conjunto)

# len= usa o tamanho exato da lista e transforma em inteiro
# print(type(len(minha_tupla)))

for x in meu_dicionario.keys():
    print(x)

meu_dicionario['peso'] = 70
print(meu_dicionario)

meu_conjunto.add('Lucas')
print(meu_conjunto)
