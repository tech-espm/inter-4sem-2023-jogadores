from sqlalchemy import text
from sqlalchemy.orm import Session
from dados import query_excluir_jogo, query_obter_jogo, query_criar_jogo, query_criar_ocorrencia, query_obter_idocorrencia, query_criar_ocorrencia_jogo, query_excluir_ocorrencia

def excluirOcorrencia(engine):
	with Session(engine) as sessao, sessao.begin():
		sessao.execute(text(query_excluir_ocorrencia))

def criarOcorrencia(engine):
	ocorrencia = None

	with Session(engine) as sessao, sessao.begin():
		sessao.execute(text(query_criar_ocorrencia))
		ocorrencia = sessao.execute(text(query_obter_idocorrencia)).first()

	return ocorrencia.idocorrencia			

def excluirJogo(engine, jogo):
	with Session(engine) as sessao, sessao.begin():
		sessao.execute(text(query_excluir_jogo),jogo)

def criarJogo(engine, jogo):
	with Session(engine) as sessao, sessao.begin():
		parametros = {
			'id': jogo['id']
		}
		jogoExistente = sessao.execute(text(query_obter_jogo), parametros).first()
		if jogoExistente == None:
			sessao.execute(text(query_criar_jogo), jogo)
			return True

def criarOcorrenciaJogo(engine, idocorrencia, jogo):
	with Session(engine) as sessao, sessao.begin():
		parametros = {
			'idocorrencia': idocorrencia,
			'idjogo': jogo['id'],
			'posicao': jogo['posicao'],
			'jogadores': jogo['jogadores']
		}
		sessao.execute(text(query_criar_ocorrencia_jogo), parametros)
