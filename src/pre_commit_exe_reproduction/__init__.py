import subprocess
import sys

def main():
    name = "rye.exe" if sys.platform == "win32" else "rye"
    sys.exit(subprocess.call([name, *sys.argv[1:]]))
