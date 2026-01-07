# use of chmod:
```bash
# make code.py
echo "#!/usr/bin/env python3" > code.py
echo "print('hi')" >> code.py

#check permisions
ls -l code.py
# output
-rw-rw-r-- 1 dell dell 12 نومبر 11 12:28 code.py

# now run following command(it will give error)
 ./code.py

# make executeable
chmod +x code.py # chmod 775 code.py or chmod 755 code.py

# check permissions
ls -l code.py
# output:
-rwxrwxr-x 1 dell dell 12 نومبر  11 12:28 code.py

# now run following command
 ./code.py
```
### Other Commands
```bash
# set 644
chmod 644 code.py

ls -l code.py
# output:
-rw-r--r-- 1 dell dell   35 نومبر  13 14:20 code.py

# set 755
chmod 755 code.py

ls -l code.py
# outout:
-rwxr-xr-x 1 dell dell 35 نومبر  13 14:20 code.py

# use of -R and -v (for apply changes to all files of that folder)
chmod -R 755 001-chmod

# use of -v (for  verbose)
chmod -v 755 code.py
```

note: new file usually permission status is 644