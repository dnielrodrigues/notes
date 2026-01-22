# SHELL
sudo -u user_name psql db_name # log without a password

# PSQL TERMINAL
ALTER USER user_name WITH PASSWORD 'new_password'; # change password
CREATE USER username WITH SUPERUSER CREATEDB CREATEROLE LOGIN PASSWORD 'your_password'; # create super user
CREATE ROLE username WITH SUPERUSER LOGIN PASSWORD 'your_password'; # create super user
