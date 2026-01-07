# add user in linux
```bash
# create new user
sudo adduser student
```
passwd: dani@student


### check user
```bash
id student

groups student
```
output
```bash
student : student
```

### give privellige to user
run this command from old user terminal
```bash
sudo usermod -aG sudo student
```

### check user
```bash
groups student
```
output
```bash
student : student sudo
```

then run 
```bash
su - student
sudo whoami
```
__________________
###  list users
```bash
awk -F: '$3 >= 1000 && $3 < 65534 {print $1}' /etc/passwd
```
__________________

### rename user and group
```bash
#check group 
groups student 

# output:
student : student sudo

# rename user:
sudo usermod -l new-username old-username
sudo usermod -l devil sys_daemon


# rename group:
sudo groupmod -n new-groupname old-groupname
sudo groupmod -n devil sys_daemon
```



