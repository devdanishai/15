```bash
# 1. create project folder
mkdir 004-pyenv && cd 004-pyenv

# 2. pin Python version
pyenv local 3.12.3

# 3. create isolated virtualenv
pyenv virtualenv 3.12.3 my-pyenv

# 4. point project to virtualenv
pyenv local my-pyenv

# 5. verify
cat .python-version    # shows tip-calc-env
python --version       # shows 3.12.3
ls ~/.pyenv/versions/  # shows 3.12.3 and tip-calc-env

# 6. install packages
pip install requests
pip list

# 7. Project: run this
python3 main.py

# 8. uninstall/rm any env
pyenv uninstall tip-calc-env
```

