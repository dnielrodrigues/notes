# Postgre SQL

### File config

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

### Location
On CentOS : /var/lib/pgsql/data/pg_hba.conf



# Remember

### Default Password
```572600```
