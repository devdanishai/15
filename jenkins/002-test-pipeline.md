# Test pipeline steps

## 🔹 1️⃣ Create Your First Pipeline

1. Click **“New Item”**
2. Enter a name (e.g., `TestPipeline`)
3. Select **Pipeline** → Click **OK**
4. In **Pipeline → Definition**, choose **Pipeline script**
5. Paste a simple test pipeline:

```groovy
pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                sh 'echo "Jenkins is running locally on Ubuntu!"'
            }
        }
    }
}
```

6. Click **Save** → Then **Build Now**
7. Check **Console Output** → You should see your message printed.

---
---
# Extra Info 

## 🔹 2️⃣ Explore Jenkins Features

From the dashboard, you can:

* **Manage Jenkins → Manage Plugins** → Add Git, Docker, and other plugins
* **Build History / Console Output** → See logs of builds
* **Create Freestyle Jobs** → Simple build tasks without pipelines
* **Configure Global Tools** → Java, Git, Maven, Docker etc.

---

## 🔹 3️⃣ Optional Next Steps

* Connect **Git repositories** (GitHub, GitLab, or local repo)
* Add **unit tests** for automatic testing
* Build **Docker images locally**
* Deploy to a **local folder or server**

---



