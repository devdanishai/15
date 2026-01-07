### pyarmor steps
```bash
pip install pyarmor
pyarmor obfuscate test.py
python3 dist/test.py
```
____________________
### for license
```bash
pyarmor licences --product-name=myapp --bind-cpu=1234567890 --expired=2025-12-31
```
- output: a licence file (licesc.lic) is generated in the licenses/ directory
____________________

- add following code in your .py file
```bash
from pyarmor.runtime import __pyarmor__

__pyarmor__.init('license.lic')

print("Protected by PyArmor licens!")
```


