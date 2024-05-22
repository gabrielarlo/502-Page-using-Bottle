# 502 Page

## Installations

1. `poetry install --no-root`
1. `poetry run python app.py`

## Run as service

1. Create file

```
sudo nano /etc/systemd/system/502page.service
```

1. Add content

```
[Unit]
Description=502-Page service
After=network.target

[Service]
User=username
Group=www-data
WorkingDirectory=/path/to/your/project
Environment="PATH=/path/to/poetry/bin:$PATH"
ExecStart=/path/to/poetry/bin/poetry poetry run python app.py

[Install]
WantedBy=multi-user.target
```

1. Enable service

```
sudo systemctl enable 502page
sudo systemctl start 502page
```

1. Check status

```
sudo systemctl status 502page
```

1. Check logs

```
sudo journalctl -u 502page
```
