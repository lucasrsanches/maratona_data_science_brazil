# Entrada de dados
A, B = input().split()

A = float(A)
B = float(B)

# Processamento
media = (A + B)/2
resposta = ''

if media >= 7:
    resposta = 'Aprovado'
elif media >= 4:
    resposta = 'Recuperacao'
else:
    resposta = 'Reprovado'

# Saída de dados
print(resposta)
