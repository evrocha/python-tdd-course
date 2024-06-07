import pytest
from scripts.bytebank import Funcionario
from pytest import mark

# Metodologia usada:
# Given... When... Then...
## Given: Contexto, cenário
## When: Ação chamada
## Then: Resposta, ação já executada

class TestClass:
    def test_idade_(self):
        entrada = '13/03/2000' 
        esperado = 24
        func_test = Funcionario("Teste", entrada, 12)
        res = func_test.idade()
        assert res == esperado
    
    def test_sobrenome(self):
        entrada = " Emanuel Rocha "
        esperado = "Rocha"
        func_test = Funcionario(entrada, '12/12/2022', 12)
        res = func_test.sobrenome()
        assert res == esperado
    
    @mark.decrescimo_salario
    def test_decrescimo_salario(self):
        entrada = 100000
        esperado = 90000
        func_test = Funcionario("Emanuel Rocha", '12/12/2022', entrada)
        func_test.decrescimo_salario()
        res = func_test.salario
        assert res == esperado
    
    @mark.bonus
    def test_calcular_bonus(self):
        entrada = 1000
        esperado = 100
        func_test = Funcionario("Emanuel Rocha", '12/12/2022', entrada)
        res = func_test.calcular_bonus()
        assert res == esperado
    
    @mark.bonus
    def test_calcular_bonus_com_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000
            func_test = Funcionario("Emanuel Rocha", '12/12/2022', entrada)
            res = func_test.calcular_bonus()
            assert res