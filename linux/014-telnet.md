# use of curl,nc,nmap,openssl,telnet
```bash

telnet 192.168.110.61 8002

# output: 
# Trying 192.168.110.61...
# Connected to 192.168.110.61.
# Escape character is '^]'.

crtl+]

# you will see telnet>
# then write 
quit
```

Note: telnet, curl(http), nc , nmap, openssl. you check them from client terminal like i am doing from my dell.

1. nc 
```bash
nc -zv 192.168.110.61 3000-3010   # scan range (zero I/O mode)
nc 192.168.110.61 3001            # open interactive connection
```
2. curl 
```bash
curl -v http://192.168.110.61:3001/health
```
3. nmap 
```bash
nmap -Pn -sV -p 3000-3010 192.168.110.61
```
4. openssl
```bash
openssl s_client -connect 192.168.110.61:443
```
5. telnet 
```bash
telnet 192.168.110.61 3001
```




