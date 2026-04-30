# Ban local linux ip 

```bash
sudo ufw deny ssh
```

or if ufw is not enabled:

```bash
sudo ufw enable
sudo ufw deny ssh
```

Verify:
```bash
sudo ufw status
```

This blocks port 22 — no machine on your network can SSH into your Dell.