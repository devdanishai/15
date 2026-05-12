ollama ps

ollama show nemotron3:33b



-----------------------------
# model creation for qwen2.5vl:

**1. qwen2.5vl with reduced context:**
```bash
nano ~/.ollama/qwen2.5vl-fast.modelfile
```
```
FROM qwen2.5vl:7b
PARAMETER num_ctx 4096
```
```bash
ollama create qwen2.5vl-fast -f ~/.ollama/qwen2.5vl-fast.modelfile
```

