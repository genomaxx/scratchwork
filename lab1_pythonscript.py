import requests
s = requests.__version__
r = requests.get('https://google.com')
p = requests.get('https://raw.githubusercontent.com/md6113/scratchwork/master/lab1_pythonscript.py')
print(s)
print(r)
print(p)
