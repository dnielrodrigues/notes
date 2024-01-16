# Postgre SQL: Read on WIKI

The more used open source database for web applications.

First access: `sudo -u postgres psql`

### On MacOS (testando):
``` bash
brew update
brew doctor
brew install postgresql@14
brew services start postgresql@14
brew services list
brew services stop postgresql@14
```
To uninstall:
```
brew services stop postgresql@14
brew uninstall --force postgresql@14
rm -rf $(brew --prefix)/var/postgresql@14
```

