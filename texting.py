import subprocess
from time import sleep
result = subprocess.run(['python', '--version'])
result = subprocess.run(['python', "testing2.py"])
while True:
    print("Running")
    sleep(1)
