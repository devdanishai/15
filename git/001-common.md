```bash

# initialize repo
git init

# create .gitignore
nano .gitignore

# add following in it
# Ignore virtual environment and cache
venv/
__pycache__/

## Ignore temporary / extra folders
final-civil/
final-military/
temp-images-folder/
weights/
yolo-dataset/
mongo-data-2025-09-07/
debug_vlm/
2nd-instance/weights/
2nd-instance/debug_crops/
2nd-instance/csv-data/
2nd-instance/detection_clips/
________________________
```

# add files in repo
```bash
# for all files 
git add .


# for selected files
git add filename

# cimmit files 
git commit -m "your comments"

#check status
git status

#check commits list
git log oneline

#check diff
git diff config.json

#wanna remove any file from stage
git restore --staged index.html

```

