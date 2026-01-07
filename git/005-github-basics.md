# basic workflow for guthub:

#### 1. 1st commit workflow:

```bash
git init
git add .
git commit -m "initial commit"
git status
git remote add origin https://github.com/devdanishai/Notes_app.git
git branch # mostly (* master)
git branch -M main #rename to main

git pull origin main --allow-unrelated-histories

git push -u origin main
```
--------------------------------
#### 2. work flow after 1st commit:

```bash
git add .
git commit -m "ur updated comment"
git push origin main

```