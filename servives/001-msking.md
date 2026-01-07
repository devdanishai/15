# Creating a new `systemd` service from scratch:

---

## **Step 1️⃣ – Create the service file**

```bash
sudo nano /etc/systemd/system/<service-name>.service
```

Replace `<service-name>` with your desired name, e.g., `my-app`.

---

## **Step 2️⃣ – Add service content**

Example for a Python app:

```ini
[Unit]
Description=My App Service
After=network.target

[Service]
User=aiops
WorkingDirectory=/home/aiops/path-to-app
ExecStart=/home/aiops/path-to-venv/bin/python3 /home/aiops/path-to-app/main.py
Restart=always
RestartSec=5
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

**Notes:**

* `User`: the Linux user that runs the service
* `WorkingDirectory`: folder where your app lives
* `ExecStart`: full path to executable (Python + script, or binary)
* `Restart` and `RestartSec`: auto-restart on crash
* `Environment`: optional variables, e.g., `PYTHONUNBUFFERED`

---

## **Step 3️⃣ – run following commands**

```bash
sudo systemctl daemon-reload
sudo systemctl enable <service-name>.service
sudo systemctl start <service-name>.service
sudo systemctl status <service-name>.service
```

## **Step 4️⃣ – Optional: Stop or restart service**

```bash
sudo systemctl stop <service-name>.service
sudo systemctl restart <service-name>.service
journalctl -u <service-name>.service -f

```

