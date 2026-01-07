https://overthewire.org

### level 0:
ssh bandit0@bandit.labs.overthewire.org -p 2220
passwd: bandit0

level 1: 
ls
cat readme
copy passwd
ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

login new terminal 
ssh bandit1@bandit.labs.overthewire.org -p 2220
passwd: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

run new ssh terminal

___
level 2:
# go to your home directory
cd ~
# confirm the file is there
ls -la

# then show the file's contents (either)
cat ./-
# or (recommended — stops option parsing)
cat -- -
# or use an absolute path from anywhere:
cat -- /home/bandit1/-

# get passwrd 
263JGJPfgU6LtdEvgfWU1XP5yac29mFx

---
Level 3 Goal:

The password for the next level is stored in a file called --spaces in this filename-- located in the home directory

sol:
ls -la

cat -- "--spaces in this filename--"

MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

---
- level 4: 
cd inhere
cat ...Hiding-From-You
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

---
- level 5 
cd inhere

ls -la

# quick check: show file types, look for "text" or "ASCII"
# show which of the -file* files are text
file -- -file*

cat -- -file07

4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw


### level 6: 
# go into the inhere directory tree
cd inhere

# find regular files exactly 1033 bytes and not executable
find . -type f -size 1033c ! -perm /111 -print0 | xargs -0 file | grep -i 'text\|ascii\|utf-'

cat ./maybehere07/.file2

HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

### Bandit Level 7
ssh bandit6@bandit.labs.overthewire.org -p 2220
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null -print -quit

cat /var/lib/dpkg/info/bandit7.password

morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

### Bandit Level 7 → Level 8
Level Goal
The password for the next level is stored in the file data.txt next to the word millionth

solution steps:
ssh bandit7@bandit.labs.overthewire.org -p 2220
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
cd ~
awk '/millionth/ {for(i=1;i<=NF;i++) if($i=="millionth") print $(i+1)}' data.txt
dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

### Bandit Level 8 → Level 9
- Level Goal
- The password for the next level is stored in the file data.txt and is the only line of text that occurs only once
- Commands you may need to solve this level
- grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xx

- solution:
ssh bandit8@bandit.labs.overthewire.org -p 2220
dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

sort data.txt | uniq -u
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM


### Bandit Level 9 → Level 10
- Level Goal
- The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.
- Commands you may need to solve this level
- grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

- solution:
ssh bandit9@bandit.labs.overthewire.org -p 2220
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
andit9@bandit:~$ strings data.txt | grep -E '={3,}' | sed 's/^=*\(.*\)$/\1/'
 the
 password
f\Z'========== is
 FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey



### Bandit Level 10 → Level 11
- Level Goal
- The password for the next level is stored in the file data.txt, which contains base64 encoded data
- Commands you may need to solve this level
- grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

- solution:
- ssh bandit10@bandit.labs.overthewire.org -p 2220
- FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
- base64 --decode data.txt
- The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

### Bandit Level 11 → Level 12
- Level Goal
- The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions
- Commands you may need to solve this level
- grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

- solution:
- ssh bandit11@bandit.labs.overthewire.org -p 2220
- dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
- tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt
- The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

### Bandit Level 12 → Level 13
- Level Goal
- The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)
- Commands you may need to solve this level
- grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv, file

- solution:
- ssh bandit12@bandit.labs.overthewire.org -p 2220
- 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
- # creates a unique temp dir and cd into it
- WORKDIR=$(mktemp -d /tmp/bandit13.XXXXXX)
- cd "$WORKDIR"

- cp ~/data.txt .
- mv data.txt dump.hex
- # safest: strip any non-hex then convert
- tr -cd '0-9A-Fa-f' < dump.hex | xxd -r -p > data.bin
- xxd -r dump.hex > data.bin
- # rename to .gz so gunzip treats it normally, then decompress
- mv data.bin data.gz
- gunzip data.gz

- # list the resulting file(s) and inspect the new file
- ls -l
- file *

- # rename then decompress
- mv data data.bz2
- bunzip2 data.bz2

- # inspect what appeared
- ls -l
- file *

- mv data data.gz
- gunzip data.gz

- # check the resulting file
- ls -l
- file *

passwd: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

### Bandit Level 13 → Level 14
- Level Goal
- The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on
- Commands you may need to solve this level
- ssh, telnet, nc, openssl, s_client, nmap

### 

