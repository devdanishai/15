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

git pull origin main --allow-unrelated-histories # use this only if repo already has commits

git push -u origin main
```
--------------------------------
#### 2. work flow after 1st commit:

```bash
git add .
git commit -m "ur updated comment"
# if use "git push -u origin main" then only "git push" is ok
git push
git status
```