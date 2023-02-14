import subprocess
import sys
import os
from pur import update_requirements

# Check if pur is installed, and warn user if it's not
try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'show', 'pur'])
except subprocess.CalledProcessError:
    print('WARNING: pur is not installed. Please run "pip install pur" to install it.')
    sys.exit(1)

# Generate requirements file from current environment
subprocess.call(['pip', 'freeze', '--local', '>', 'requirements.txt'])

# Use pur to update requirements file
subprocess.call(['pur', '-r', 'requirements.txt'])

# Use pip to update all packages
subprocess.call(['pip', 'install', '-r', 'requirements.txt', '--upgrade'])

# Clean up the requirements file
os.remove('requirements.txt')