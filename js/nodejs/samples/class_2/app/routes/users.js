/**
 * rotas de usuarios ...
 * -------------------------------------------------------------------------
 */
module.exports = function(app){

    // listar ...
    app.get('/usuarios',function(req,res){ res.render("users/list"); });
}
