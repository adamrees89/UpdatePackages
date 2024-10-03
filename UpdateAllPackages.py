import subprocess
import sys
import os
from pur import update_requirements

def check_pur_installed():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'show', 'pur'])
    except subprocess.CalledProcessError:
        print('WARNING: pur is not installed. Please run "pip install pur" to install it.')
        sys.exit(1)

def generate_requirements_file():
    try:
        with open('requirements.txt', 'w') as f:
            subprocess.run(['pip', 'freeze', '--local'], stdout=f, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error generating requirements file: {e}")
        sys.exit(1)

def update_requirements_file():
    try:
        update_requirements('requirements.txt', 'updates.txt')
    except Exception as e:
        print(f"Error updating requirements file: {e}")
        sys.exit(1)

def install_updates():
    try:
        subprocess.run(['pip', 'install', '-r', 'updates.txt', '--upgrade'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing updates: {e}")
        sys.exit(1)

def clean_up(files):
    for file in files:
        try:
            os.remove(file)
        except OSError as e:
            print(f"Error removing file {file}: {e}")

def main():
    check_pur_installed()
    generate_requirements_file()
    update_requirements_file()
    install_updates()
    clean_up(['requirements.txt', 'updates.txt'])

if __name__ == "__main__":
    main()