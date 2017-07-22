/**
 * rotas de usuarios ...
 * -------------------------------------------------------------------------
 */
 app.get('/produtos',function(req,res){

     // arquivo [lista.ejs] na pasta [views/produtos] ...
     res.render("produtos/lista");
 });
