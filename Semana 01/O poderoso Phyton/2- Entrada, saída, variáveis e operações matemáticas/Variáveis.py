nome = 'Lucas'
idade = 21
altura = 1.75
tipo_nome = type(nome)
tipo_idade = type(idade)
tipo_altura = type(altura)

print('nome:', nome)
print(tipo_nome)
print('idade:', idade)
print(tipo_idade)
print('altura:', altura)
print(tipo_altura)

print(nome, 'tem', idade, 'anos e', altura, 'de altura')
# Quando usado "+"(mais) ao invés de ","(virgula), é preciso converter int e float para str.
print(nome + 'tem' + str(idade) + 'anos e' + str(altura) + 'de altura')
