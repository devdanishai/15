how to hide last login ip from ssh intro message

```bash
#run in terminal
sudo nano /etc/ssh/sshd_config

#find
# PrintLastLog yes

#change
PrintLastLog no

#save and exit
Ctrl + X, Y, Enter

# restart sshd service
sudo systemctl restart ssh

```

__________________________________________________
- note: you can check any last login by `last`