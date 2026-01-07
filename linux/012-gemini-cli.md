### ⚙️ Step 1: Install Gemini CLI
```bash
mkdir ~/gemini-cli
cd ~/gemini-cli
npm init -y
npm install @google/gemini-cli
npx gemini --version #verify

```


### Set your API Key as an Environment Variable

- In your terminal, run:
```bash
export GEMINI_API_KEY=AIzaSyCRnSDoDnw__OK1bJYHkr5GGn_lxULVH48
```
- test your api key by running:

```bash
echo $GEMINI_API_KEY

unset GOOGLE_API_KEY

npx gemini ask "What is the capital of FRANCE?" 

npx gemini chat

```

___


---

### ⚡ Fix: Make the API key permanent

1. Open your shell config file (`~/.bashrc` or `~/.zshrc`) in an editor:

```bash
nano ~/.bashrc
```

2. Add these lines at the end:

```bash
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
```
- remove GOOGLE_API_KEY


3. Save and exit (`Ctrl+O` → `Enter` → `Ctrl+X` in nano).

4. Reload the shell:

```bash
source ~/.bashrc
```

---

✅ Now, every new terminal session will have the API key set, and you can run:

```bash
npx gemini chat
```

without re-exporting the key.

---

Optional: After this, you can also set an **alias** so you just type `gemini chat` instead of `npx gemini chat`.

Do you want me to show that one-liner alias?
