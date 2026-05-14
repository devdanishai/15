# Local
```bash
# Install via npm (recommended for Linux)
npm install -g @anthropic-ai/claude-code

claude --version

ollama launch claude --model qwen3:32b 
ollama launch claude --model qwen3-coder:30b 
ollama launch claude --model qwen3-vl:235b-instruct-cloud 
```

# Server
```bash
npm install -g @anthropic-ai/claude-code@latest
```

_______________________________
# reduce context for qwen3-coder-next:


Create a modelfile:
```bash
nano ~/.ollama/qwen3-coder-next-fast.modelfile
```

Add this:
```
FROM qwen3-coder-next:q8_0
PARAMETER num_ctx 32768
```

Create the optimized version:
```bash
ollama create qwen3-coder-next-fast -f ~/.ollama/qwen3-coder-next-fast.modelfile
```

