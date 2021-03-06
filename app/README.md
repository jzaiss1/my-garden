# My Garden API Server

## Initial Ubuntu Server Setup

Update apt repository

```bash
sudo add-apt-repository universe
```

Create a user for the application

```bash
sudo adduser garden
```

Granting Administrative Privileges

```bash
sudo usermod -aG sudo garden
```

Set Up a Basic Firewall

```bash
ufw app list
ufw allow OpenSSH
ufw enable
ufw status
```

## Install Nginx

```bash
sudo apt update
sudo apt install nginx
```

### Adjust the Firewall

```bash
sudo ufw app list
```

Enable HTTP

```bash
sudo ufw allow 'Nginx HTTP'
```

### Set Up Server Blocks

To avoid a possible hash bucket memory problem that can arise from adding additional server names, it is necessary to adjust a single value in the `/etc/nginx/nginx.conf` file.

```bash
sudo vi /etc/nginx/nginx.conf
```

Find the `server_names_hash_bucket_size` directive and remove the # symbol to uncomment the line:

```bash
...
http {
    ...
    server_names_hash_bucket_size 64;
    ...
}
...
```

See the `vserver-cfg.sh` for the site setup  <-- Just for testing if necessary

## Install components for Flask

```bash
sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
```

## Create a Python Virtual Environment

Install the `python3-venv` package, which will install the `venv` module:

```bash
sudo apt install python3-venv
```

Make a parent directory for our Flask project

```bash
mkdir ~/mygarden
cd ~/mygarden
```

Create a virtual environment to store your Flask project’s Python requirements by typing

```bash
python3.6 -m venv mygardenenv
```

Before installing applications within the virtual environment, you need to activate it. Do so by typing:

```bash
source mygardenenv/bin/activate
```

## Set up Flask to host the application

Install Wheel

```bash
pip install wheel
```

Install Flask and uWSGI

```bash
pip install uwsgi flask flask-mysql
```

Once the installations are complete deactivate the virtual environment

```bash
deactivate
```

## My Garden Application files

See `mygarden.py` for the application code

See `wsgi.py` for the uWSGI Entry Point

See `mygarden.ini` for the uWSGI Configuration

## Create the systemd Unit File

See `mygarden.service` for the configuration

```bash
sudo cp setup/mygarden.service /etc/systemd/system/
```

Configure the mygarden uWSGI service and enable to start at boot

```bash
sudo systemctl start mygarden
sudo systemctl enable mygarden
```

## Copy the application code

Clone the repo and copy the app folder to the mygarden directory

```bash
cp -r ~/mygarden/app .
```

## Configure Nginx to Proxy Requests

See `mygarden` for the block configuration

```bash
sudo cp setup/mygarden /etc/nginx/sites-available/
```

Link the file to the `sites-enabled` directory

```bash
sudo ln -s /etc/nginx/sites-available/mygarden /etc/nginx/sites-enabled
```

Test the configuration

```bash
sudo nginx -t
```

Restart the Nginx process

```bash
sudo systemctl restart nginx
```

Configure the Firewall

```bash
sudo ufw allow 'Nginx Full'
```
