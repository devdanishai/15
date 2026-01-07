On VM2 (client) 
- — generate SSH key
```bash
ssh-keygen -t ed25519

#Copy the public key to VM1 (server)
ssh-copy-id ubuntu@10.208.246.230
```

______________________________________________
on VM! (Server)
```bash
sudo nano /etc/ssh/sshd_config
```
#addthis into file 
```bash
PasswordAuthentication yes
ChallengeResponseAuthentication no
UsePAM yes
```
save it then run following
```bash
sudo systemctl restart ssh
```

________________________________________________

---

#### **Option 2 — Manually copy the key** (simplest workaround)

1. On VM2 (`ubuntu-server1`), show the public key:

```bash
cat ~/.ssh/id_ed25519.pub
```
- actual key
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGjUl/7abVVNpoLTnr1RTbpenNY6bAlcU0YOwWL+39XA ubuntu@ubuntu-server1

2. Copy the output.

3. On VM1 (`ubuntu-server`), open authorized_keys:

```bash
mkdir -p ~/.ssh
nano ~/.ssh/authorized_keys
```

* Paste the public key into the file
* Save and exit
* Set proper permissions:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

4. Test SSH login from VM2:

```bash
ssh ubuntu@10.208.246.230
```

* Should log in **without password** ✅

---
