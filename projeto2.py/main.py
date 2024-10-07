from models.enum.sexo import Sexo
from models.pessoa import Pessoa
import os 

pessoa1 = Pessoa("Luis", 18, Sexo.MASCULINO)

os.system("cls || clear ")
print(pessoa1)