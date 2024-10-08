import pytest
from models.pessoa import Pessoa
from models.enum.sexo import Sexo

@pytest.fixture
def criar_pessoa():
    return Pessoa ("Luis", 18, Sexo.MASCULINO)


def test_nome(criar_pessoa):
    assert criar_pessoa.nome == "Luis"

def test_idade(criar_pessoa):
    assert criar_pessoa.idade == 18   
    
def test_pessoa_nome_valido(criar_pessoa):
    criar_pessoa == "Rafael"
    assert criar_pessoa.nome == "Rafael"

def test_pessoa_idade_negativa_retorna_mensagem_excessao():    
    with pytest.raises(ValueError, match = "Idade não pode ser negativa"):
        Pessoa("Luis", -12, Sexo.MASCULINO)


def test_pessoa_tipo_invalido_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match = "A idade deve conter números."):
        Pessoa("Luis", "18 anos", Sexo.MASCULINO)