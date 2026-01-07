👍 Here’s a simple plan you can follow on your Linux server:

---

# 🟢 Step 1 — Create a simple Node.js project

```bash
mkdir pm2-test
cd pm2-test
npm init -y
```

Create a simple server, `index.js`:

```js
const http = require('http');

const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello from PM2 test!\n');
});

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

---

# 🟢 Step 2 — Test it manually

```bash
node index.js
```

* Open browser or curl:

```bash
curl http://localhost:3000
```

* You should see: `Hello from PM2 test!`

---

# 🟢 Step 3 — Run it with PM2

```bash
pm2 start index.js --name "PM2Test"
```

* PM2 will now manage the process.
* Check status:

```bash
pm2 list
pm2 show PM2Test
```

* View logs:

```bash
pm2 logs PM2Test
```

---

# 🟢 Step 4 — Test auto-restart

* find process and Kill the process manually:

```bash
pm2 pid PM2Test

kill <PID>
```

* PM2 will **restart it automatically** (check `pm2 logs`).

---

# 🟢 Step 5 — Save for reboot

```bash
pm2 save
pm2 startup
```

* Ensures PM2 restarts your app on server reboot.

---

# 🔹 Optional: Use `ecosystem.config.js`

Create `ecosystem.config.js`:

```js
module.exports = {
  apps: [
    {
      name: "PM2Test",
      script: "index.js",
      env: {
        PORT: 3001,
        NODE_ENV: "development"
      },
      watch: true,
      autorestart: true
    }
  ]
};
```

Run it:

```bash
pm2 start ecosystem.config.js
pm2 list
# also check
curl http://localhost:3001 # output: Hello from PM2 test!

```

---
# 🟢 Step 6 — PM2 Daily Use Commands (Cheat Sheet)

| Action                     | Command                             |
| -------------------------- | ----------------------------------- |
| Start app                  | `pm2 start index.js --name PM2Test` |
| Start from ecosystem       | `pm2 start ecosystem.config.js`     |
| Restart app                | `pm2 restart PM2Test`               |
| Reload app (zero-downtime) | `pm2 reload PM2Test`                |
| Stop app                   | `pm2 stop PM2Test`                  |
| Delete app                 | `pm2 delete PM2Test`                |
| Restart all apps           | `pm2 restart all`                   |
| Stop all apps              | `pm2 stop all`                      |
| Delete all apps            | `pm2 delete all`                    |
