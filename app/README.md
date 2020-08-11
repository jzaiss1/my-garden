# mygarden-api

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

Enable External Access for garden

Set up SSH keys <https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1804>

```bash
ssh-keygen
Enter file in which to save the key (/your_home/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
```

- [ ] TODO: Revisit SSH keys, first attempt failed

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

## Set up Flask Application

Install Wheel

```bash
pip install wheel
```

Install Flask and uWSGI

```bash
pip install uwsgi flask flask-mysqldb
```

## References

<https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04>

<https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04>

<https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04>
