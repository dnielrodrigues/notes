### Add data on $_SERVER variable:
`fastcgi_param MY_VARIABLE "myValue";`  

### Find php.ini file
`php --ini`  
PS: Look for "Loaded Configuration File"

### Install 7.4 version
```
sudo apt update
sudo apt -y install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo add-apt-repository ppa:ondrej/nginx
sudo apt update
sudo apt install php7.4 php7.4-cli php7.4-fpm php7.4-common php7.4-mysql php7.4-xml php7.4-curl php7.4-gd php7.4-mbstring php7.4-zip php7.4-intl -y
php7.4 -v
```
