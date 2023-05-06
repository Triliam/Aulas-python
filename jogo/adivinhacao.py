import random

print("---------------------------------")
print("      JOGO DE ADIVINHAÇÃO        ")
print("---------------------------------")

segredo = random.randrange(1, 11)

#print(segredo)

count = 0
while count < 3:
    numero = int(input("Digite um numero entre 1 e 10, voce tem 3 tentativas: "))
    
    if numero < 1 or numero > 10:
        print("Numero invalido, tente novamente")

    elif numero == segredo:
        print("Voce acertou!")
        break
    else:
        print("vc errou, tente novamente")
    count+=1
print("fim, o numero foi: ", segredo)    