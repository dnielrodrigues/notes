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
```

Dump: 
```
MYSQL_PASSWORD=$DBPASS mysqldump -h $DBHOST -u $DBUSER > dump.sql
```

Restore: 
```
MYSQL_PASSWORD=$DBPASS mysql -h $DBHOST -u $DBUSER $DBNAME < dump.sql
```

### Gerais
Create DB: ```CREATE DATABASE $DBNAME;```  
Delete DB: ```DROP DATABASE [IF EXISTS] $DBNAME;```  
