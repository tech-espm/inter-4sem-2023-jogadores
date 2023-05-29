import app = require('teem');
import Jogo = require("../../models/jogo");

class JogoApiRoute {
	public async listar(req: app.Request, res: app.Response) {
		res.json(await Jogo.listar());
	}

	public async listarPosicaoPorData(req: app.Request, res: app.Response) {
		res.json(await Jogo.listarPosicaoPorData(parseInt(req.query["idjogo"] as string), req.query["dataInicial"] as string, req.query["dataFinal"] as string));
	}

	public async listarTop10PorData(req: app.Request, res: app.Response) {
		res.json(await Jogo.listarTop10PorData(req.query["data"] as string));
	}
}

export = JogoApiRoute;
