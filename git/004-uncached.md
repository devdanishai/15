# wanna untrack any file

1. add that file in gitignore
```bash
count_line_coords.json
2nd-instance/count_line_coords.json
```

2. run following:
```bash
git rm --cached count_line_coords.json
git rm --cached 2nd-instance/count_line_coords.json
```

3. run follwong
```bash
git add .gitignore
git commit -m "Ignore count_line_coords.json files"
```
