import unittest
import banco
import app
from sqlalchemy import create_engine
from dados import string_conexao

class TestBanco(unittest.TestCase):
    def test_banco_CriaOcorrenciaSemEngine(self): # Julia: Testa se a função criarOcorrencia retorna uma exceção quando não recebe um engine
        self.assertRaises(BaseException, banco.criarOcorrencia, None)

    def test_banco_CriaOcorrenciaOK(self):# João Vitor: Testa se a função criarOcorrencia retorna um inteiro quando recebe um engine
        engine = create_engine(string_conexao)
        banco.excluirOcorrencia(engine)
        r = banco.criarOcorrencia(engine)
        engine.dispose(True)
        self.assertIs(type(r), int)

    def test_banco_CriaOcorrenciaDuplicada(self):# Gabriel Zaude: Testa se a função criarOcorrencia retorna uma exceção quando já existe uma ocorrência no banco
        engine = create_engine(string_conexao)
        banco.excluirOcorrencia(engine)
        banco.criarOcorrencia(engine)
        self.assertRaises(BaseException, banco.criarOcorrencia, engine)
        engine.dispose(True)
    
    def test_banco_CriaJogoOK(self): #Gabriel Peixoto: Testa se a função criarJogo retorna True quando recebe um engine e um jogo
        engine = create_engine(string_conexao)
        jogo = {'id': 999,
			'posicao': 999,
			'nome': "Teste",
			'imagem': "Teste",
			'jogadores': 0}
        banco.criarJogo(engine,jogo)
        self.assertTrue(banco.criarJogo, engine)
        engine.dispose(True)

if __name__ == '__main__':
    unittest.main()
    #testador = TestBanco()
    #testador.test_banco_CriaOcorrenciaOK()
