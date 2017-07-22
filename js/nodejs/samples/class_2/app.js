/**
 * config ...
 * -----------------------------------------------------------------------------
 *
 * @OBS : modulos do node usando o formato "CommonJS" ...
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
app.listen(3000, function(){ console.log("rodando"); });
