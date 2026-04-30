
## 🛠️ Updated Official Installation Steps (Terminal)

### 1️⃣ Install prerequisites

```bash
sudo apt update
sudo apt install curl apt-transport-https -y
```

---

### 2️⃣ Download and save Brave’s GPG key

Run:

```bash
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
```

This is the **correct key file URL** — the one you tried earlier (`brave-core.asc`) is no longer used. ([Brave][1])

---

### 3️⃣ Add the Brave repository

```bash
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
```

---

### 4️⃣ Update and install Brave

```bash
sudo apt update
sudo apt install brave-browser -y
```

---

### 5️⃣ Launch Brave

You can start it from the apps menu or run:

```bash
brave-browser
```

---

## ✅ Alternative easy ways

If the above still has issues (sometimes CDN access or key problems happen), you can install Brave using:

### 📦 Snap (very easy)

```bash
sudo snap install brave
```

Ubuntu supports snap out of the box. 

Note: i use 1st way.