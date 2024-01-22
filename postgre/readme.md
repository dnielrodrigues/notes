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

### Table management

Rename a column: 
`ALTER TABLE table_table RENAME COLUMN old_name TO new_name;`  
Add a column: 
`ALTER TABLE table_name ADD COLUMN IF NOT EXISTS column_name INT;`  
Delete a column: `...`  
Add a constraint: `...`  
Delete a constraint: `...`  
Alter a constraint: `...`  

### Links

* https://www.dataquest.io/blog/install-postgresql-14-7-for-macos/
* https://www.moncefbelyamani.com/how-to-install-postgresql-on-a-mac-with-homebrew-and-lunchy/
* https://stackoverflow.com/questions/15692508/a-faster-way-to-copy-a-postgresql-database-or-the-best-way
