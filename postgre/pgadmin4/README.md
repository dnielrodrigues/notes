## Samples


Script to start:
```
#!/bin/bash
cd /home/my_user/code/pgadmin4
source bin/activate
echo "PgAdmin4"
echo "link: http://127.0.0.1:5050"
echo "---------------------------"
python lib/python3.5/site-packages/pgadmin4/pgAdmin4.py </dev/null >pgadmin.log 2>&1 &
```
