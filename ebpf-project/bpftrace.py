import subprocess
import os
import sys
import time


def run_script_in_tmux_pane(pane_id, script):
    subprocess.run(
        ["tmux", "send-keys", "-t", f"{pane_id}", f"bpftrace {script}", "C-m"]
    )


if __name__ == "__main__":
    script_dir = "bpftrace/"
    script_paths = ["opensnoop.bt", "tracepoints.bt"]
    script_paths = [script_dir + x for x in script_paths]

    for path in script_paths:
        if not os.path.exists(path.split(" ")[0]):
            print(f"Script '{path}' does not exist. Exiting.")
            sys.exit(1)

    subprocess.run(["tmux", "new-session", "-d", "-s", "bpftrace-session"])

    # Split the tmux window into 2 panes
    subprocess.run(["tmux", "split-window", "-h"])

    for i, script in enumerate(script_paths):
        run_script_in_tmux_pane(i, script)
        time.sleep(1)

    subprocess.run(["tmux", "attach", "-t", "bpftrace-session"])
