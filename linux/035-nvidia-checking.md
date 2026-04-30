```bash
# 1.
nvcc --version
output:
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Mon_Apr__3_17:16:06_PDT_2023
Cuda compilation tools, release 12.1, V12.1.105
Build cuda_12.1.r12.1/compiler.32688072_0

# 2.
sudo find /usr -name "cudnn_version.h" 2>/dev/null
output:
/usr/include/x86_64-linux-gnu/cudnn_version.h

# 3. 
aiops@aiops-test:~$ grep -E "CUDNN_MAJOR|CUDNN_MINOR|CUDNN_PATCHLEVEL" /usr/include/x86_64-linux-gnu/cudnn_version.h
output:
#define CUDNN_MAJOR 9
#define CUDNN_MINOR 10
#define CUDNN_PATCHLEVEL 1
#define CUDNN_VERSION (CUDNN_MAJOR * 10000 + CUDNN_MINOR * 100 + CUDNN_PATCHLEVEL)
```
_______________

# gpu health
nvidia-smi

# disk
df -h

# RAM
free -h

# system load
uptime

# ollama checking
ollama --version
ollama ps

# running services 
ps aux | grep python
____________
sudo apt update
sudo apt install -y sysstat

mpstat -P ALL 1 3