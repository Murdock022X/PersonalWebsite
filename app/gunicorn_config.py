# Config file for gunicorn

# Ip and port to bind gunicorn to.
bind = '0.0.0.0:8080'

# Number of workers to create.
workers = 2

# Where to send logs to.
accesslog = '/var/log/gunicorn/gunicorn.access.log'
errorlog = '/var/log/gunicorn/gunicorn.error.log'
