import subprocess
import os
import sys
import time


def run_script_in_tmux_pane(pane_id, script):
    subprocess.run(
        ["tmux", "send-keys", "-t", f"{pane_id}", f"python3 {script}", "C-m"]
    )


if __name__ == "__main__":
    script_dir = "scripts/"
    script_paths = ["users_command.py", "xdp_drop_count.py wlp0s20f3", "filetop.py 5"]
    script_paths = [script_dir + x for x in script_paths]

    for path in script_paths:
        if not os.path.exists(path.split(" ")[0]):
            print(f"Script '{path}' does not exist. Exiting.")
            sys.exit(1)

    subprocess.run(["tmux", "new-session", "-d", "-s", "ebpf-session"])

    # Split the tmux window into 4 panes
    subprocess.run(["tmux", "split-window", "-h"])
    subprocess.run(["tmux", "split-window", "-v"])
    subprocess.run(["tmux", "select-pane", "-t", "0"])
    subprocess.run(["tmux", "split-window", "-v"])

    for i, script in enumerate(script_paths):
        run_script_in_tmux_pane(i, script)
        time.sleep(1)

    subprocess.run(["tmux", "attach", "-t", "ebpf-session"])
