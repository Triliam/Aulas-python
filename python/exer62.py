
numeroMaior = 0
numeros = [1, 4, 3, 6, 2, 5]


for i in range(0,6):
    print(numeros[i])
    if numeros[i] > numeroMaior:
       numeroMaior = numeros[i]
       pos = i
print("O maior numeros eh: ", numeroMaior, " e esta na posicao", pos)


