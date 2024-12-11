# Reminder

Default Page:  
`/usr/share/nginx/html`

Config File:  
`/etc/nginx/nginx.conf`

Server Block create alias sample:  
`sudo ln -s /etc/nginx/sites-available/config_file_name /etc/nginx/sites-enabled/`  
ou  
```
FROM="/path/to/file.txt"
TO="/path/to/alias.txt"
sudo ln -s $FROM $TO
```  

Debug config files:  
`sudo nginx -t`

Restart Nginx:  
`/etc/init.d/nginx restart`

For AWS Linux 2:  
`amazon-linux-extras list | grep nginx`  
`sudo amazon-linux-extras install <app_name>`

## Logs

Require Log:  
`/var/log/nginx/access.log`

Error Log:  
`/var/log/nginx/error.log`

# Links
Virtual hosts: https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-virtual-hosts-server-blocks-on-centos-6  
Change default error page: https://www.digitalocean.com/community/tutorials/how-to-configure-nginx-to-use-custom-error-pages-on-ubuntu-22-04
