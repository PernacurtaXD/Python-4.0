from ...projeto2.enum.sexo import Sexo 

class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        return (f"Nome: {self.nome}"
                f"Idade: {self.idade}"
                f"Sexo: {self.sexo.name}"
        )    
