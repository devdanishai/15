# Port Whitelist

Config-file-driven UFW firewall management for per-port IP whitelisting.
Only IPs listed in `port-whitelist.conf` can reach the managed ports.
All other traffic to those ports is silently dropped.

## Files

| File | Purpose |
|------|---------|
| `port-whitelist.conf` | List of `<port>:<ip>` pairs — the single source of truth |
| `sync-port-whitelist.sh` | Applies the config to UFW (wipes + rebuilds rules for listed ports) |
| `README.md` | This file |

## Quick start

```bash
# 1. Edit the whitelist
sudo nano ~/port-whitelist/port-whitelist.conf

# 2. Apply changes
sudo ~/port-whitelist/sync-port-whitelist.sh
```

## Config format

```
# Comments start with #
# Blank lines are ignored
# Format: <port>:<ip>

3001:192.168.18.150
3001:192.168.18.151
3000:192.168.18.152
```

- One IP per line
- Same IP can appear on multiple ports (just add another line)
- IPv4 addresses only (IPv6 not currently supported by this script)

## Common operations

### Add an IP
Append a line to the config and sync:
```
3001:192.168.18.200
```

### Remove an IP
Delete the line (or comment it out with `#`) and sync.

### Temporarily disable an IP
Prefix the line with `#`:
```
# 3001:192.168.18.151
```

### Add a new port to management
Add lines for it in the config. Example for port 8080:
```
8080:192.168.18.150
8080:192.168.18.200
```

Note: once a port is in the config, the sync script **owns** all UFW rules
for that port. Any manual `ufw allow 8080` rules will be wiped on next sync.

### Remove a port from management
Delete all lines for that port from the config. On next sync, the script
wipes its rules and adds none — resulting in full deny (UFW default).

### View current UFW rules for managed ports
```bash
sudo ufw status numbered | grep -E "3000|3001"
```

### View full UFW status
```bash
sudo ufw status numbered
```

## How the sync script works

The script is **idempotent** — running it repeatedly produces the same result.

1. Reads all unique ports from the config (ignoring comments / blank lines)
2. For each managed port: deletes ALL existing UFW rules for it (v4 and v6)
3. Reads the config again line by line and adds one allow rule per `port:ip`
4. Reloads UFW
5. Prints the final state for each managed port

**Safety:** the script only touches ports listed in the config. Rules for
SSH (22), RDP (3389), and other ports are left completely untouched.

## Troubleshooting

### Legitimate IP cannot connect
1. Check the IP is in the config: `grep <ip> ~/port-whitelist/port-whitelist.conf`
2. Check the rule is applied: `sudo ufw status numbered | grep <ip>`
3. Check the app is actually listening: `sudo ss -tlnp | grep :<port>`
4. From the client, test TCP reachability: `nc -zv 192.168.18.102 <port>`

### Sync script fails
- Must run as root: `sudo ~/port-whitelist/sync-port-whitelist.sh`
- Check config syntax — each line must be `port:ip` with no extra spaces
- Check UFW is installed and active: `sudo ufw status`

### I locked myself out of SSH
SSH (port 22) is not managed by this script, so this should not happen.
If it does, you need physical/console access to the server:
```bash
sudo ufw allow 22/tcp
```

### Roll back to "allow from anywhere" for a port
1. Remove the port from `port-whitelist.conf`
2. Run the sync script (this removes the specific-IP rules)
3. Manually add an allow-all rule:
   ```bash
   sudo ufw allow <port>/tcp
   ```

## Current whitelist

Check live config: `cat ~/port-whitelist/port-whitelist.conf`
