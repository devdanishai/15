# use of cat with EOF
cat > dynamic.txt << EOF
Username : $USER
home directory: $HOME
EOF

# it will print:
Username : dell
home directory: /home/dell

note: if we wanna save literal text then we use "EOF"
cat > dynamic.txt << EOF
Username : $USER
home directory: $HOME
EOF

# it will print:
Username : $USER
home directory: $HOME

# echo with > = for text ingestion and erase older
echo "hello" > file1.txt

# echo with >> = for text ingestion without erasing older text
echo "hello" >> file1.txt

# add text without erasing older
cat >> file1.txt >> EOF
this way is used to ingest text 
in file without erasing older data
EOF

___________________________________________
# some different commands cat/EOF

cat > file1.txt << EOF # overwrite file.txt with dynamic variables
cat > file1.txt << "EOF" # overwrite file.txt with literal variables
cat >> file1.txt << EOF # append text

cat << EOF > file1.txt # overwrite text
cat << EOF >> file1.txt # appent text

___________________________________________

echo "hello, world" > file.txt # overwrite text
echo "hello, world appended" >> # append text

_____________________________________________

ip a show
sudo ufw enable
sudo ufw allow 8000/tcp
sudo ufw status

df -h
df -hT
du -sh folder-name

________________________________________________


__________________________________________________

tail -n 20 /home/aiops/mongodb_backup_cron.log
ls -l /mnt/storage/mongodb-backups-01/

___________________________________________________

sudo systemctl restart gdm

