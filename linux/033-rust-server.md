
# RustDesk Local Server Setup

---

## Step 1: Download the Server Package

```bash
# Run this on the server machine from the home directory
wget https://github.com/rustdesk/rustdesk-server/releases/download/1.1.12/rustdesk-server-linux-amd64.zip
```

---

## Step 2: Unzip the Package

```bash
# Extract the downloaded archive
unzip rustdesk-server-linux-amd64.zip
```

---

## Step 3: Start the ID/Rendezvous Server (hbbs)

```bash
# Navigate into the extracted folder and start hbbs
# Run this in a dedicated tmux window — keep it running
cd amd64
./hbbs -r 192.168.18.102
```

> A key pair will be generated on first run. Copy the public key shown in the output.

---

## Step 4: Save Your Public Key

```
48+9DvpaWD4dyPi+s16aMDfjvBKZz5TGT5sd35w4Oz4=
```

> You'll need this key when configuring RustDesk on both machines.

---

## Step 5: Start the Relay Server (hbbr)

```bash
# Open a NEW tmux window, then run:
cd amd64
./hbbr
```

> Keep both `hbbs` (Step 3) and `hbbr` (Step 5) running simultaneously in separate tmux windows.

---

## Step 6: Configure RustDesk on Both Machines

Go to: **RustDesk → Settings → Network → ID/Relay Server**

> Apply the **exact same settings** on both the local and server machines.

| Field        | Value                                            |
|--------------|--------------------------------------------------|
| ID Server    | `192.168.18.102`                                 |
| Relay Server | `192.168.18.102`                                 |
| API Server   | *(leave blank)*                                  |
| Key          | `48+9DvpaWD4dyPi+s16aMDfjvBKZz5TGT5sd35w4Oz4=` |

Click **Apply** after filling in the fields.

---

## Step 7: Open Firewall Ports on the Server

```bash
# Allow all required RustDesk ports through UFW
sudo ufw allow 21115/tcp   # NAT type test
sudo ufw allow 21116/tcp   # ID registration & heartbeat (TCP)
sudo ufw allow 21116/udp   # ID registration & heartbeat (UDP)
sudo ufw allow 21117/tcp   # Relay server
sudo ufw allow 21118/tcp   # Web client (optional)
sudo ufw allow 21119/tcp   # Web client (optional)
```


