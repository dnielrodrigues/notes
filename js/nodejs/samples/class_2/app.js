/**
 * config ...
 * -----------------------------------------------------------------------------
 *
 * @OBS : modulos do node usam o formato "CommonJS" ...
 *
 * @IMPORTANT : auto restart node : https://nodemon.io/
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
