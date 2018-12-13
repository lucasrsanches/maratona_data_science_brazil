N = int(input())

viewers = []
for i in range(N):
    A = int(input())
    viewers.append(A)

total = 0
resposta = -1
for i, v in enumerate(viewers):
    dia = i+1
    total = total + v
    if total >= 1000000 and resposta == -1:
        resposta = dia
print(resposta)