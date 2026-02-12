

### 1️⃣ Check your interface name

```bash
ip a
# check ip and 
networkctl status

```

*(Note the interface you want to assign static IP, e.g., `eno100`)*

---

### 2️⃣ Backup existing Netplan file

```bash
sudo cp /etc/netplan/01-network-manager-all.yaml /etc/netplan/01-network-manager-all.yaml.bak
```

---

### 3️⃣ Edit Netplan file

```bash
sudo nano /etc/netplan/01-network-manager-all.yaml
```

**Paste this (replace IPs & interface):**

```yaml
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    eno100:
      dhcp4: no
      addresses:
        - 192.168.18.102/24
      routes:
        - to: default
          via: 192.168.18.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```

---

### 4️⃣ Fix file permissions

```bash
sudo chmod 600 /etc/netplan/01-network-manager-all.yaml
```

---

### 5️⃣ Apply the configuration

```bash
sudo netplan apply
```

*(Optional safer test before applying fully:)*

```bash
sudo netplan try
```

---

### 6️⃣ Verify static IP

```bash
ip a
ip route
```

---

### 7️⃣ (Optional) Reboot to confirm persistence

```bash
sudo reboot
```

After reboot, verify again:

```bash
ip a
ip route
```

---
