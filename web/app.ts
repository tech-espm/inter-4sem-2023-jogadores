import app = require("teem");
import appsettings = require("./appsettings");

app.run({
	localIp: appsettings.localIp,
	root: appsettings.root,
	port: appsettings.port,
	sqlConfig: appsettings.sqlConfig
});
