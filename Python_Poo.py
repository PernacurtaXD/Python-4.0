import os


os.system("cls || clear")

class Aluno:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome 
        self.idade = idade 

    def __str__(self) -> str:
           return (
                    f"\nNome: {self.nome}"                
                    f"\nIdade: {self.idade}"
           )


aluno = Aluno("Luis", 18)

#Primeira Forma
print(aluno)