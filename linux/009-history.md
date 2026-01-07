### turn on / off history 
```bash
#turn off history
set +o history

#turn on history
set -o history
```


___________________________________________________
## 2nd way:
- go to `~/.bash_history`
- delete entires manually 
- then run `history -r`


______
### 3rd way:
```bash
sudo su -
unset HISTFILE; export HISTSIZE=0 HISTFILESIZE=0; history -c
```