# Reminder

Default Page:  
`/usr/share/nginx/html`

Config File:  
`/etc/nginx/nginx.conf`

Server Block create alias sample:  
`sudo ln -s /etc/nginx/sites-available/config_file_name /etc/nginx/sites-enabled/`

Debug config files:  
`sudo nginx -t`

Restart Nginx:  
`/etc/init.d/nginx restart`

## Logs

Require Log:  
`/var/log/nginx/access.log`

Error Log:  
`/var/log/nginx/error.log`

