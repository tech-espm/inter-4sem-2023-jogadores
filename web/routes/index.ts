import app = require('teem');
import Jogo = require("../models/jogo");
import DataUtil = require("../utils/dataUtil");

class IndexRoute {
	public async index(req: app.Request, res: app.Response) {
		res.render('index/index');
	}

	public async top10(req: app.Request, res: app.Response) {
		res.render('index/top10', {
			hoje: DataUtil.horarioDeBrasiliaISO()
		});
	}

	public async historico(req: app.Request, res: app.Response) {
		res.render('index/historico', {
			dataInicial: DataUtil.horarioDeBrasiliaISO(-30 * 24 * 60 * 60),
			dataFinal: DataUtil.horarioDeBrasiliaISO(),
			jogos: await Jogo.listar()
		});
	}

	public async sobre(req: app.Request, res: app.Response) {
		res.render('index/sobre');
	}
}

export = IndexRoute;
