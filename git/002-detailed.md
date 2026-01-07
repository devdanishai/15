### Add
```bash
# wanna add only modified files files
git add .

# wanna add only that file e.g
git add index.html

# wanna add all files 
git add --all # or "git add -A"
```

### Commit
```bash
# wanna commit changes
git commit -m "your comment"

# without staging commit
git commit -a -m "your comment"
```

### log
```bash
# See commit history
git log

# For a shorter view
git log --oneline

# To see which files changed in each commit
git log stats
```