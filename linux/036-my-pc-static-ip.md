# Linux Static IP Setup Guide

**System:** dell-Precision-3660 | **Interface:** enp0s31f6 | **OS:** Ubuntu (Netplan + NetworkManager)

---

## Step 1: Check your interface name and current IP

```bash
# Show all network interfaces and assigned IPs
ip a
```

```bash
# Show network status and gateway info
networkctl status
```

---

## Step 2: Backup existing Netplan file

```bash
# Create a backup before making any changes
sudo cp /etc/netplan/01-network-manager-all.yaml /etc/netplan/01-network-manager-all.yaml.bak
```

---

## Step 3: Edit Netplan configuration file

```bash
# Open the Netplan config file in nano editor
sudo nano /etc/netplan/01-network-manager-all.yaml
```

Paste the following configuration:

```yaml
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    enp0s31f6:
      dhcp4: no
      addresses:
        - 192.168.18.95/24
      routes:
        - to: default
          via: 192.168.18.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```

---

## Step 4: Fix file permissions

```bash
# Netplan requires strict 600 permissions on config files
sudo chmod 600 /etc/netplan/01-network-manager-all.yaml
```

---

## Step 5: Test and apply the configuration

```bash
# Safely test config — auto-reverts in 120 seconds if no confirmation
sudo netplan try
```

```bash
# Press ENTER to confirm, or apply directly
sudo netplan apply
```

---

## Step 6: Verify static IP is active

```bash
# Check that IP shows 'valid_lft forever' (no longer dynamic)
ip a show enp0s31f6
```

```bash
# Confirm default gateway is set via static route
ip route
```

```bash
# Test internet connectivity and DNS resolution
ping -c 3 google.com
```

---

## Step 7: Reboot to confirm persistence

```bash
# Reboot the system
sudo reboot
```

```bash
# After reboot — verify the static IP survived
ip a show enp0s31f6
```

```bash
# Confirm routing table is still correct
ip route
```

---

> **Expected result:** `192.168.18.95/24` with `valid_lft forever` | Gateway: `192.168.18.1` via static | 0% packet loss on ping
