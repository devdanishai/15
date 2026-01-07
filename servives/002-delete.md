

---

## 1️⃣ Stop the service

```bash
sudo systemctl stop <service-name>
```

## 2️⃣ Disable it (prevent auto-start on boot)

```bash
sudo systemctl disable <service-name>
```

## 3️⃣ Delete the service file

```bash
sudo rm /etc/systemd/system/<service-name>.service
```

## 4️⃣ Reload systemd to apply changes

```bash
sudo systemctl daemon-reload
sudo systemctl reset-failed
```

---

### ✅ Why these steps matter

* **Stopping**: ensures it’s not running in memory
* **Disabling**: ensures it won’t start on boot
* **Removing the file**: deletes the definition
* **Reloading systemd**: updates systemd so it no longer knows about the removed service



---

