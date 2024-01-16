# Postgre SQL: Read on WIKI

The more used open source database for web applications.

First access: `sudo -u postgres psql`  
On Mac: `psql -U postgres`

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

### Links

* https://www.dataquest.io/blog/install-postgresql-14-7-for-macos/  
* https://www.moncefbelyamani.com/how-to-install-postgresql-on-a-mac-with-homebrew-and-lunchy/  
