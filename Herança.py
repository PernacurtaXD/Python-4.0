from abc import ABC, abstractclassmethod
import os 

class Funcionario(ABC):
    def __init__(self,nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @abstractclassmethod
    def calcular_salario(self) -> float:
        pass

    def __str__(self) -> str:
        return f"\nNome: {self.nome}\nIdade: {self.idade}\nSalário: {self.salario}"

os.system("cls || clear")
class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        BONIFICACAO = 1.2
        salario_final = self.salario * BONIFICACAO
        return salario_final
""" 
    def __str__(self) -> str:
        return f"\nGERENTE\n{super().__str__()}"
""" 

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh

    def calcular_salario(self) -> float:
        BONIFICACAO = 1.1
        salario_final = self.salario * BONIFICACAO
        return salario_final
"""
    def __str__(self) -> str:
        return f"\nMOTOBOY\n{super().__str__()}\nCNH:{self.cnh}"
"""
gerente = Gerente("Manoel", 25, 4526.65)
motoboy = Motoboy("João", 22, 2250.52, "159")


print(f"Nome: {gerente.nome}")
print(f"Salário final: R${gerente.calcular_salario()}")


print(f"Nome: {motoboy.nome}")
print(f"Salário final: R${motoboy.calcular_salario()}")