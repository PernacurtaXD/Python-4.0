import os 


os.system("cls || clear")
contador = 0
soma = 0
media = 0
#Solicitando dados 
nota = int(input("Digite um número:"))

#Usando laço de repetição
while nota >= 0:
 soma= soma + nota 
 contador+=1

 nota = int(input("Digite algum número:"))
 

media = soma / contador  

print(f"Média = {media}")
print(soma)


