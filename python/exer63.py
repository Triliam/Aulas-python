numeros = [0,1,2,3,4,5,6]

#print(numeros)
for i in numeros:
    print(i)

num = int(input("Digite um número entre 0 e 6: "))

for i in numeros:
    if num == i:
        i = 7
    print(i)
    
