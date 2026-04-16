1. Create different ssh keys for different companies:  
```bash
# Company A
ssh-keygen -t ed25519 -C "you-email@company-a.com" -f ~/.ssh/id_ed25519_company_a

# Company B  
ssh-keygen -t ed25519 -C "your-email@company-b.com" -f ~/.ssh/id_ed25519_company_b

# For personal
ssh-keygen -t ed25519 -C "your-email@gmail.com" -f ~/.ssh/id_ed25519_perconal
```

2. Add keys to SSH agent:  
```bash
# Start the SSH agent
eval "$(ssh-agent -s)"

# Add keys
ssh-add ~/.ssh/id_ed25519_company_a
ssh-add ~/.ssh/id_ed25519_company_b
ssh-add ~/.ssh/id_ed25519_personal
```

3. Create file `~/.ssh/config`:  
```bash
# Company A
Host github-company-a
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_company_a
    IdentitiesOnly yes

# Company B
Host github-company-b
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_company_b
    IdentitiesOnly yes

# Personal
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes

# Fallback
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
```

4. Insert public keys to Github account:  
```bash
# See Company A key
cat ~/.ssh/id_ed25519_company_a.pub

# See Company B key
cat ~/.ssh/id_ed25519_company_b.pub

# See Personal key
cat ~/.ssh/id_ed25519_personal.pub
```

5. Using aliases to clone:  
```bash
# To company A repository
git clone git@github-company-a:company-a/project-a.git

# To company B repository
git clone git@github-company-b:company-b/project-b.git

# To personal repository
git clone git@github-personal:your-user/personal-project.git
```

6. Config user by repository:  
```bash
# Inside each repository
cd ~/projects/company-a/site
git config user.name "Your professional name"
git config user.email "hour-email@company-a.com"

cd ~/projects/company-b/project
git config user.name "Your name"
git config user.email "your-email@company-b.com"
```

7. Test connections:  
```bash
# Test company A connection
ssh -T git@github-company-a

# Test company B connection
ssh -T git@github-company-b

# Test personal connection
ssh -T git@github-personal
```
