import random

print("---------------------------------")
print("      JOGO DE ADIVINHAÇÃO        ")
print("---------------------------------")

segredo = random.randrange(1, 11)

print(segredo)

acertou = False
tentativas = 3

for i in range(1,4):
    print("Voce esta na tentativa", i, " de 3\n")
    numero = int(input("Digite um numero entre 1 e 10: "))
    
    if numero < 1 or numero > 10:
        print("numero invalido, digite novamente")
    #tentativas -=1
    
    if numero == segredo:
        acertou = True
        
    if acertou:
        print("---------------------------------")
        print("   VOCE ACERTOU!!! PARABÉNS!!!"   )
        print("---------------------------------")
        break
    else:
        print("Voce errou, tente novamente\n")
            #tentativas -= 1
print(f"Fim  de jogo. O numero sorteado foi: {segredo}")