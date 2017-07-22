/**
 * rotas de usuarios ...
 * -------------------------------------------------------------------------
 */
module.exports = function(app){

    app.get('/usuarios',function(req,res){
        res.render("usuarios/list");
    });
}
