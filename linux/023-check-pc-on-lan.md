
```bash
ip neigh | awk '$1 ~ /^192\.168\.110\./ {count++} END {print count+0}'
```
