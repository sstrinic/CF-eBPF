import subprocess
import os
import sys
import time


def run_script_in_terminal(script):
    subprocess.Popen(["terminator", "--command", f"sudo python3 {script}"])


if __name__ == "__main__":
    script_dir = "scripts/"
    script_paths = ["users-command.py"]
    script_paths = [script_dir + x for x in script_paths]

    for path in script_paths:
        if not os.path.exists(path):
            print(f"Script '{path}' does not exist. Exiting.")
            sys.exit(1)

    for script in script_paths:
        run_script_in_terminal(script)
        time.sleep(1)
