Vars:
```
DBHOST=localhost
DBPORT=3306
DBUSER=homestead
DBNAME=sample
DBPASS=secret
FILE=dump.sql
```

### Terminal:  
`MYSQL_PASSWORD=$DBPASS mysql -h $DBHOST -u $DBUSER`  
`MYSQL_PASSWORD=$DBPASS mysql -h $DBHOST -u $DBUSER --password=$DBPASS --port=$DBPORT`  

### Dump:  
`MYSQL_PASSWORD=$DBPASS mysqldump -h $DBHOST -u $DBUSER > $FILE`  
```
MYSQL_PASSWORD=$DBPASS mysqldump -h $DBHOST -u $DBUSER --password=$DBPASS --port=$DBPORT --single-transaction --skip-lock-tables --column-statistics=0 --routines --add-drop-table --disable-keys --extended-insert $DBNAME > $FILE
```  

### Restore:  
`MYSQL_PASSWORD=$DBPASS mysql -h $DBHOST -u $DBUSER $DBNAME < $FILE`  
`MYSQL_PASSWORD=$DBPASS mysql -h $DBHOST -u $DBUSER --password=$DBPASS --port=$DBPORT $DBNAME < $FILE`  

### Rename DB: 
```
DB_OLD=old_database
DB_NEW=new_database

mysqldump -u $DBUSER -p -v $DB_OLD > old_dump.sql
mysqladmin -u $DBUSER -p create $DB_NEW
mysql -u $DBUSER -p $DB_NEW < old_dump.sql
```

### Gerais
List databases: `SHOW DATABASES;`  
Create DB: `CREATE DATABASE $DBNAME;`  
Delete DB: `DROP DATABASE [IF EXISTS] $DBNAME;`  
Select DB: `USE <DBNAME>;`  
Test service: `systemctl is-active mysql`  
Stop service: `sudo systemctl stop mysql`  
