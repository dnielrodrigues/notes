# Arredondar Números

Para cima: `Math.ceil(x);`  
Para baixo: `Math.floor(x);`  
Pelo mais próximo: `Math.round(x);`  

# Manipular Array

Retirar e retornar o último item do array: `var last = arr.pop();` ou `arr.pop()`

Retirar e retornar o primeiro item do array: `var first = arr.shift();`

Inserir como último item do array: `arr.push(0);`

Inserir como primeiro item do array: `arr.push(10)`

HTTP Request without any lib:
```javascript
async function request(opt) {
  const url = opt.url || 'http://localhost:3000'
  const method = opt.method || 'GET'
  const headers = opt.headers || { 'Content-Type': 'application/json' }
  const body = opt.body ? JSON.stringify(opt.body) : JSON.stringify({})
  try {
    const response = await fetch(url, { method, headers, body })

    // verify success request
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    // convert to json
    const data = await response.json()
    console.log('Response:', data)
    return data
  } catch (error) {
    console.error('Request error: ', error)
    throw error
  }
}
```

Using HTTP request function:
```javascript
// Using:
const config = {
  url: 'https://apidinamica.tributario.aspec.com.br:8086/api/report_open',
  method: 'POST',
  headers: {
    'uf_municipio': 'ce_chorozinho',
    'Content-Type': 'application/json'
  },
  body: {
    action: 'gtm-rel-valor-nfse-servico-emitida-v1',
    params: {
      data_inicio: '01/01/2017',
      data_fim: '30/12/2017'
    }
  }
}
const res = await request(config)
console.log(res)
```
