1. Check which process is using port 3001
```bash
sudo netstat -tulpn | grep :3001
# or
sudo ss -tulnp | grep 3001
# or
sudo ss -tulpn | grep -E ':(8108)\s'


# output:
tcp6       0      0 :::3001                 :::*                    LISTEN      843503/next-server 
```

2. find working dir
```bash
pwdx 843503

output:
843503: /home/aiops/Documents/horizon-FullStack-version-2/test_frontend
```

3. find which command use to run file 
```bash
ps -fp 3207476

```