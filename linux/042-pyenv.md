Clear picture now! pyenv folder exists but **shell doesn't know about it**. We just need to connect it.

---

## Fix — add pyenv to your shell

```bash
nano ~/.bashrc
```

This opens the file. Use the **down arrow key** to scroll all the way to the bottom, then paste these 3 lines:

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Then save and exit:
- Press `Ctrl + X`
- Press `Y`
- Press `Enter`

Then reload:
```bash
source ~/.bashrc
```

---

Now test:
```bash
pyenv --version


#needed packages
sudo apt install -y libbz2-dev libreadline-dev libsqlite3-dev tk-dev liblzma-dev
# install new version
pyenv install 3.12.3

#set new version globally
pyenv global 3.12.3
```
_________
