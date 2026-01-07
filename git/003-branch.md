### Branch:

```bash
# 1. Create a new branch for your experiment
git checkout -b experiment-1

# 2. Work normally in this branch
git status
git add .
git commit -m "Experiment: trying new camera logic"

# 3. Switch between branches locally
# go to master
git checkout master

# go to experiment
git checkout experiment-1

# 4. See all branches
git branch

# 5. Delete experiment branches when done (optional)
# if merged
git branch -d experiment-1

# if wanna delete without merge
git branch -D experiment-1
