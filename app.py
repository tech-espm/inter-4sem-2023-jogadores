from sqlalchemy import create_engine
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dados import url_origem, string_conexao
from banco import criarOcorrencia, criarJogo, criarOcorrenciaJogo

driver = webdriver.Chrome()
driver.get(url_origem)

corpo_tabela = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, '#table-apps > tbody'))
)

linhas = corpo_tabela.find_elements(By.TAG_NAME, 'tr')

jogos = []

posicao = 0

for linha in linhas:
	appid = int(linha.get_attribute("data-appid"))

	posicao = posicao + 1

	colunas = linha.find_elements(By.TAG_NAME, 'td')

	imagem = colunas[1].find_elements(By.TAG_NAME, 'img')
	imagem = imagem[0].get_attribute('src')
	nome = colunas[2].text
	jogadores = int(colunas[4].get_attribute("data-sort"))

	jogos.append({
		'id': appid,
		'posicao': posicao,
		'nome': nome,
		'imagem': imagem,
		'jogadores': jogadores
	})

driver.close()

engine = create_engine(string_conexao)

idocorrencia = criarOcorrencia(engine)

jogos.sort(key=lambda jogo: jogo['jogadores'], reverse=True)

for jogo in jogos:
	criarJogo(engine, jogo)
	criarOcorrenciaJogo(engine, idocorrencia, jogo)

engine.dispose(True)
