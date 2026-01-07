#### How to install tmux:
```bash
sudo apt update
sudo apt install tmux

tmux -V # check version
```

#### workflow 
* `tmux` → starts a session **without a name**

* `tmux ls` -> shows all sessions(you can run inside and outside session)

* `tmux new -s app` → starts a session **named “monitor”**

________________________
### run new app
* `tmux new -s app` # start new session

* run your app 

* `tmux ls` #verify

* `tmux attach -t app`  # reconnect later

* `echo $TMUX` # inside session 



### commands inside session
```bash
Ctrl + b  then  n   → next window
Ctrl + b  then  p   → previous window
Ctrl + b  then  0   → go to window #0
Ctrl + b  then  1   → go to window #1
Ctrl + b  then  w   → choose from menu list
Ctrl + b  then  d   → close tmux while running app
Ctrl + b  then  %   → vertical split
Ctrl + b  then  "   → horizental split 

```