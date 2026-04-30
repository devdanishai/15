

```bash
ssh aiops@192.168.18.102
```

Then on the server:
```bash
# Create script
nano /home/aiops/speedtest_log.sh
```

Paste:
```bash
#!/bin/bash
DATE=$(date +%Y-%m-%d_%H-%M)
SAVE_DIR="$HOME/speedtest_logs"
mkdir -p "$SAVE_DIR"

speedtest | tee "$SAVE_DIR/speedtest_$DATE.txt"
```

Then:
```bash
chmod +x /home/aiops/speedtest_log.sh

# Add to cron
crontab -e
```

Add:
```bash
0 9 * * * /home/aiops/speedtest_log.sh >> /home/aiops/speedtest_logs/cron.log 2>&1
```

When you're back from vacation, check all logs:
```bash
ls ~/speedtest_logs/
cat ~/speedtest_logs/speedtest_2026-03-11_09-00.txt
```

# test 
```bash
bash /home/aiops/speedtest_log.sh
```

No screenshot needed since it's just saving text logs — you can review them all when you return.