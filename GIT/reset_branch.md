```bash
BRANCH="your-branch-name" # Insira o nome da branch
git checkout $BRANCH # Mude para a branch que você quer esvaziar
git update-ref -d HEAD # Volte para antes do primeiro commit (isso remove todos os commits)
git rm --cached -r . # Remova todos os arquivos do staging area
git commit --allow-empty -m "Reset branch" # Faça um novo commit vazio (opcional)
git push -f origin $BRANCH #Force o push para o repositório remoto (se necessário)
```
