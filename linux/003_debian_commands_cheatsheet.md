# Debian/Ubuntu Linux Command Cheat Sheet

## 🔹 File & Directory Management
```bash
ls        # list files
cd        # change directory
pwd       # print working directory
mkdir     # make directory
rmdir     # remove empty directory
touch     # create empty file
find      # search for files/directories
tree      # display directory structure (apt install tree)
```

## 🔹 File Viewing & Editing
```bash
cat       # view file contents
less      # view file one screen at a time
head      # show first lines
tail      # show last lines
nano      # text editor
vim       # text editor (apt install vim)
```

## 🔹 File Operations
```bash
cp        # copy files
mv        # move/rename files
rm        # remove files
stat      # file info
file      # show file type
```

## 🔹 Permissions & Ownership
```bash
chmod     # change permissions
chown     # change ownership
chgrp     # change group ownership
umask     # default permission mask
```

## 🔹 System Information
```bash
uname -a  # kernel & system info
hostname  # show system name
uptime    # system running time
df -h     # disk usage
du -sh    # directory size
top       # running processes
htop      # interactive process viewer (apt install htop)
free -h   # memory usage
lsb_release -a   # distro info (apt install lsb-release)
```

## 🔹 Process Management
```bash
ps aux    # list processes
kill PID  # kill process by PID
killall   # kill by process name
jobs      # list background jobs
fg        # bring job to foreground
bg        # send job to background
sudo lsof -i :8100 #check port
```

## 🔹 Networking
```bash
ping      # test connectivity
curl      # transfer data from URLs (apt install curl)
wget      # download files
ip a      # show IP addresses
ifconfig  # show ip addresses
ss -tulnp # show listening ports & processes
scp       # secure copy over ssh
ssh       # connect to remote server
```

## 🔹 Package Management (Debian/Ubuntu)
```bash
sudo apt update             # refresh package index
sudo apt upgrade            # upgrade installed packages
sudo apt install <pkg>      # install package
sudo apt remove <pkg>       # remove package
sudo apt autoremove         # clean unused packages
sudo apt search <pkg>       # search package
dpkg -i file.deb            # install .deb package
dpkg -l                     # list installed packages
```

## 🔹 Archiving & Compression
```bash
tar -cvf archive.tar file/dir   # create tar
tar -xvf archive.tar            # extract tar
gzip file                       # compress
gunzip file.gz                  # decompress
zip file.zip file               # create zip (apt install zip)
unzip file.zip                  # extract zip (apt install unzip)
```

## 🔹 User Management
```bash
whoami    # current user
id        # user ID info
who       # logged in users
sudo adduser username   # add user
sudo passwd username    # change user password
su - username           # switch user
sudo <command>          # run as root


```

## 🔹 Disk & File System
```bash
lsblk     # list block devices
df -h     # show mounted disks
mount     # mount device
umount    # unmount device
fdisk -l  # partition info
mkfs.ext4 /dev/sdX      # create ext4 filesystem
fsck /dev/sdX           # check filesystem
```
