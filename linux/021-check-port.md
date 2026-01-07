```bash
sudo ufw status

sudo ss -tulnp | grep 8002  #(sudo netstat -tulnp | grep 8002)

output:
tcp   LISTEN 0      2048              0.0.0.0:8002       0.0.0.0:*    users:(("python3",pid=3223274,fd=115))

output:
#No output → port 8002 is free.
```