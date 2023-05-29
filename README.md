# Projeto Interdisciplinar IV - Sistemas de Informação ESPM

<p align="center">
    <a href="https://www.espm.br/cursos-de-graduacao/sistemas-de-informacao/"><img src="https://raw.githubusercontent.com/tech-espm/misc-template/main/logo.png" alt="Sistemas de Informação ESPM" style="width: 375px;"/></a>
</p>

# Análise de Jogos com Mais Jogadores por Data

### 2023-01

## Integrantes
- [Gabriel Pereira dos Guimarães Peixoto](https://github.com/GabrielP2324/)
- [João Vitor Malvestiti Miranda](https://github.com/JvmMiranda/)
- [Nome do integrante 3 e link do portifólio](https://github.com/tech-espm/)

## Descrição do Projeto

Este repositório contém uma análise de jogos com mais jogadores por data. O objetivo é identificar quais jogos têm atraído mais jogadores ao longo do tempo, fornecendo insights sobre tendências e popularidade de diferentes jogos.

Os dados utilizados para esta análise foram coletados de uma única fonte. Esses dados incluem informações sobre o número de jogadores ativos em diferentes jogos em datas específicas.

Os resultados da análise revelaram insights interessantes sobre jogos com mais jogadores por data. Alguns jogos mostraram-se consistentemente populares ao longo do tempo, enquanto outros tiveram picos de popularidade em datas específicas, possivelmente devido a eventos especiais, lançamentos de expansões ou atualizações.

# Detalhes de Configuração

Para funcionar corretamente, devem ser criados os seguintes arquivos/pastas nos caminhos especificados, com o conteúdo especificado:

- O arquivo `dados.py` deve ser criado em `/`, com o conteúdo abaixo:
```
url_origem = [URL do site]
string_conexao = [String de conexão com o banco de dados]
query_obter_jogo = [Query para obter os dados de um jogo no banco de dados]
query_criar_jogo = [Query para inserir um novo jogo no banco de dados]
query_criar_ocorrencia = [Query para inserir uma nova ocorrência no banco de dados]
query_obter_idocorrencia = [Query para obter o id da nova ocorrência inserida no banco de dados]
query_criar_ocorrencia_jogo = [Query para inserir os dados de um jogo específico na data da ocorrência]
```

- O arquivo `.env` deve ser criado em `/web`, com o conteúdo abaixo:

```
app_localIp=0.0.0.0
app_port=3000
app_root=
# Não pode terminar com barra /
app_urlSite=http://localhost:3000
app_staticFilesDir=public
app_disableStaticFiles=0
app_sqlConfig_connectionLimit=30
app_sqlConfig_waitForConnections=1
app_sqlConfig_charset=utf8mb4
app_sqlConfig_host=localhost
app_sqlConfig_port=3306
app_sqlConfig_user=[USUÁRIO DO BANCO]
app_sqlConfig_password=[SENHA DO USUÁRIO DO BANCO]
app_sqlConfig_database=[NOME DO BANCO]
```

# Licença

Este projeto é licenciado sob a [MIT License](https://github.com/tech-espm/inter-4sem-2023-jogadores/blob/main/LICENSE).

<p align="right">
    <a href="https://www.espm.br/cursos-de-graduacao/sistemas-de-informacao/"><img src="https://raw.githubusercontent.com/tech-espm/misc-template/main/logo-si-512.png" alt="Sistemas de Informação ESPM" style="width: 375px;"/></a>
</p>
