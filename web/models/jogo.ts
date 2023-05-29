import app = require("teem");
import DataUtil = require("../utils/dataUtil");

class Jogo {
	public static async listar(): Promise<any[]> {
		return app.sql.connect(async (sql) => {
			return sql.query("select id, nome, imagem from jogo order by nome asc");
		});
	}

	public static async listarPosicaoPorData(idjogo: number, dataInicial: string, dataFinal: string): Promise<any[]> {
		return app.sql.connect(async (sql) => {
			return sql.query(`
				select date_format(o.data, '%d/%m/%y') data, oj.posicao
				from ocorrencia o
				inner join ocorrencia_jogo oj on oj.idocorrencia = o.id and oj.idjogo = ?
				where o.data between ? and ?
				order by o.data asc
			`, [idjogo, DataUtil.converterDataISO(dataInicial), DataUtil.converterDataISO(dataFinal)]);
		});
	}

	public static async listarTop10PorData(data: string): Promise<any[]> {
		return app.sql.connect(async (sql) => {
			return sql.query(`
				select oj.posicao, j.id, j.nome, j.imagem
				from ocorrencia o
				inner join ocorrencia_jogo oj on oj.idocorrencia = o.id and oj.posicao <= 10
				inner join jogo j on j.id = oj.idjogo
				where o.data = ?
				order by oj.posicao
			`, [DataUtil.converterDataISO(data)]);
		});
	}
}

export = Jogo;
