/**
 * rotas de usuarios ...
 * -------------------------------------------------------------------------
 */
module.exports = function(app){

    // driver pgSql ...
    var pg = require('pg');
    var conn = ..

    // listar ...
    app.get('/usuarios',function(req,res){ res.render("users/list"); });

    // criar ...
    app.post('/usuarios',function(req,res){ res.render("users/create"); });

    // editar ...
    app.putch('/usuarios/{{id}}',function(req,res){ res.render("users/edit"); });

    // deletar ...
    app.delete('/usuarios/{{id}}',function(req,res){ res.render("users/edit"); });

}
