A = input()

A = float(A)

if A >= 7:
    print("Aprovado com nota:{:.2f}".format(A))

elif A >= 5:
    print("Recuperação")

else:
    print("Reprovado")
