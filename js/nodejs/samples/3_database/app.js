/**
 * Banco de Dados ...
 * -----------------------------------------------------------------------------
 *
 * @OBS : ...
 *
 */
var app = require('./config/express')();

/**
 * rotas ...
 * -----------------------------------------------------------------------------
 */
var user_routes = require('./app/routes/users')(app);

/**
 * subir servidor ...
 * -----------------------------------------------------------------------------
 */
app.listen(3000, function(){ console.log('running'); });
