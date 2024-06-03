import os 


os.system("cls || clear")

soma = 0
contador = 0
notas = []

while True: 
    nota = float(input("Digite uma nota:"))
    notas.append(nota)
    soma+=nota
    contador+=1

    resposta = input("Deseja adicionar mais uma nota (s/n)?").upper()

    if resposta == 'N':
        break


media = soma / contador

os.system("cls || clear")

for i, nota in enumerate(notas):
    print(f"{i+1}ª Notas = {nota}")
print(f"Média = {media:.2}")