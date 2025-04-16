Gerar chave pública para autenticação SSH:  
`ssh-keygen -t rsa -b 4096 -C "seu-email@exemplo.com"`  

Configurar chave pública:  
```
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

Testar conexão SSH com github:  
`ssh -T git@github.com`  

Desfazer último commit:  
`git reset HEAD~`  
