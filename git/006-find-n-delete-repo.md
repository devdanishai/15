### find and delete loxcal repo:

```bash

find ~ -type d -name ".git" 2>/dev/null | wc -l

find ~ -type d -name ".git" 2>/dev/null
 
ls -ld /home/dell/Desktop/linux-commands/15/python-workout/.git        /home/dell/Desktop/linux-commands/15/linux/003-pm2/.git
 
rm -rf /home/dell/Desktop/linux-commands/15/python-workout/.git        /home/dell/Desktop/linux-commands/15/linux/003-pm2/.git
 
find ~ -type d -name ".git" 2>/dev/null
```