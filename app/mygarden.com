server {
        listen 80;
        listen [::]:80;

        root /var/www/mygarden.com/html;
        index index.html index.htm index.nginx-debian.html;

        server_name mygarden.com www.mygarden.com;

        location / {
                try_files $uri $uri/ =404;
        }
}