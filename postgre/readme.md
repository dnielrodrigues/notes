# Postgre SQL

The more used open source database for web applications.

# Remember

Default Password: ```572600```

# Shell Console Commands

Log into postgre special unix account: ```sudo -i -u postgres```

Enter postgre console (always in the postgre unix user): ```psql```

Enter postgre console: ```psql -d db_name```

Create a new Role (in the postgre unix user): ```createuser --interactive```

Create a OS user for a Role: ```sudo adduser user_name```

Create a database (in the postgre unix user): ```createdb db_name```

# Postgre Console Commands

Get information about user logged and currently database: ```\conninfo```

# File config

In local enviroment use:

```
# TYPE  DATABASE        USER            ADDRESS                 METHOD
# "local" is for Unix domain socket connections only
local   all             all                                     trust
# IPv4 local connections:
host    all             all             127.0.0.1/32            trust
host    all             all             all                     trust
# IPv6 local connections:
host    all             all             ::1/128                 trust
```

### File Location

On CentOS : /var/lib/pgsql/data/pg_hba.conf