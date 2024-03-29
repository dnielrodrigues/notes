Vars:
```
DBHOST=localhost
DBPORT=3306
DBUSER=homestead
DBNAME=sample
DBPASS=secret
```

Terminal: 
```
MYSQL_PASSWORD=$DBPASS mysql -h $DBHOST -u $DBUSER
MYSQL_PASSWORD=$DBPASS mysql -h $DBHOST -u $DBUSER --port=33060
```

Dump: 
```
MYSQL_PASSWORD=$DBPASS mysqldump -h $DBHOST -u $DBUSER > dump.sql
```

Restore: 
```
MYSQL_PASSWORD=$DBPASS mysql -h $DBHOST -u $DBUSER $DBNAME < dump.sql
```

Rename DB: 
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
