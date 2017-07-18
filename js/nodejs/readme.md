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
