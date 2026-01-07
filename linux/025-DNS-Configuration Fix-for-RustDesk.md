## Fix "Temporary failure in name resolution" Error Rustdesk connection to server
or
## DNS Configuration Fix for RustDesk

```bash
# Edit DNS configuration file
sudo nano /etc/systemd/resolved.conf

# Add these two lines under [Resolve] section:
DNS=8.8.8.8 1.1.1.1 192.168.110.1
FallbackDNS=8.8.4.4 1.0.0.1

# Restart DNS service to apply changes
sudo systemctl restart systemd-resolved

# Verify DNS is working
resolvectl status

# Test DNS resolution
nslookup google.com
```

---

### Bonus: Quick RustDesk Access Commands

```bash
# Stop Docker containers for RustDesk access
docker stop $(docker ps -q)

# Restart RustDesk service (if needed)
sudo systemctl restart rustdesk

# Resume Docker containers after using RustDesk
docker start mongo horizon-fullstack-version-4-backend-1 horizon-fullstack-version-4-frontend-1 horizon-fullstack-version-4-image-server-1
```

---
