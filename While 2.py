import os 

os.system("cls || clear")
contador = 0
soma = 0

while True:
    nota = float(input("Digite sua nota:"))
    #Parada do laço, não deve ficar depois do cálculo.
    if nota <= 0:
        break

    soma+=nota
    contador+=1

media = soma / contador

print(media)    