BRANCH="your-branch-name"

# 1. Mude para a branch que você quer esvaziar
git checkout $BRANCH

# 2. Volte para antes do primeiro commit (isso remove todos os commits)
git update-ref -d HEAD

# 3. Remova todos os arquivos do staging area
git rm --cached -r .

# 4. Faça um novo commit vazio (opcional)
git commit --allow-empty -m "Reset branch"

# 5. Force o push para o repositório remoto (se necessário)
git push -f origin $BRANCH
