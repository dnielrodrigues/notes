/**
 * exemplo de modulo em CommonJS ...
 * -----------------------------------------------------------------------------
 * OBS:
 *      - com o codigo fora do "exports" o modulo sempre sera o mesmo, pois esta
 *        carregado antes de seu retorno ...
 *      - usando todo o codigo dentro do "exports" o modulo podera ter suas
 *        diferencas para cada vez que for chamado ...
 *
 */
var app = require('express')();
app.set('view engine', 'ejs');
app.set('views','./app/views')

// retorno ...
module.exports = function() {
    return app;
}
