Exemplo Mais Simples Possível
-----------------------------

```
// dependecias ...
var http = require('http');

// criar servidor ...
var server = http.createServer(function(request,response){    
    if(request.url =="/produtos"){ response.end("<h1>pagina listagem</h1>"); }
    else { response.end("<h1>home do app</h1>"); }
});

// subir servidor ...
verser.listen(3000,"localhost");

// resultado ...
console.log("rodando...");
```

Início Básico
-------------

```
mkdir my_app
cd myapp
npm init
npm install express --save
npm install ejs --save
```

Ferramentas Úteis
-----------------

#### Express
- Framework principal do node
- https://www.npmjs.com/package/express

#### NodeMon
- Reiniciar o serviço host sempre que alterar os arquivos
- (apenas instalar globalmente e rodar "nodemon" ao invez de "nodejs")
- https://www.npmjs.com/package/nodemon

#### Driver pgSql
- PostgreSQL database
- https://www.npmjs.com/package/pg
