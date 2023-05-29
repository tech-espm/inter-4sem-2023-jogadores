from sqlalchemy import text
from sqlalchemy.orm import Session
from dados import query_obter_jogo, query_criar_jogo, query_criar_ocorrencia, query_obter_idocorrencia, query_criar_ocorrencia_jogo

def criarOcorrencia(engine):
	ocorrencia = None

	with Session(engine) as sessao, sessao.begin():
		sessao.execute(text(query_criar_ocorrencia))
		ocorrencia = sessao.execute(text(query_obter_idocorrencia)).first()

	return ocorrencia.idocorrencia			

def criarJogo(engine, jogo):
	with Session(engine) as sessao, sessao.begin():
		parametros = {
			'id': jogo['id']
		}
		jogoExistente = sessao.execute(text(query_obter_jogo), parametros).first()
		if jogoExistente == None:
			sessao.execute(text(query_criar_jogo), jogo)

def criarOcorrenciaJogo(engine, idocorrencia, jogo):
	with Session(engine) as sessao, sessao.begin():
		parametros = {
			'idocorrencia': idocorrencia,
			'idjogo': jogo['id'],
			'posicao': jogo['posicao'],
			'jogadores': jogo['jogadores']
		}
		sessao.execute(text(query_criar_ocorrencia_jogo), parametros)
