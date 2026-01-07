curl -fsSL https://raw.githubusercontent.com/dontizi/rlama/main/install.sh | sh

rlama install-dependencies

# Use llama3.1:8b for good balance of speed and quality
# note:we have to give folder in path not file 
rlama rag llama3.1:8b myrag ~/Downloads/novel-folder

rlama list
rlama run myrag

_______________________________
# Delete the current RAG
rlama delete myrag1

# Recreate it with nomic-embed-text (you already have this model!)
rlama rag llama3.1:8b myrag ~/Downloads/novel-folder --reranker-model nomic-embed-text
rlama run myrag

rlama rag qwen3:32b myrag1 ~/Downloads/novel-folder --reranker-model nomic-embed-text
rlama run myrag1

rlama rag qwen3:32b myrag1 ~/Downloads/novel-folder --reranker-model nomic-embed-text --chunk-size 800 --chunk-overlap 150

rlama rag qwen3:32b myrag1 ~/Downloads/novel1 --reranker-model nomic-embed-text --chunk-size 1000 --chunk-overlap 200

# For literary/narrative content:
rlama rag qwen3:32b myrag2 ~/Downloads/novel1 --reranker-model nomic-embed-text --chunk-size 2500 --chunk-overlap 500 --chunking-strategy semantic


-----------------------
fmt -w 90 the-definition-raw.txt > the-definition.txt
-----------------------
How do residents choose their names, and what is the significance of those names?
How does the narrator perceive Maria and why?