import subprocess
try:
    judgement = subprocess.run(["/bin/bash", "List_block_devices.sh"], capture_output=True, check=True, text=True)
    print(judgement.stdout)
except subprocess.CalledProcessError as e:
    print(e.stderr)