from elftools.elf.elffile import ELFFile
from bcc import BPF
from time import strftime
import pwd


# get user name from user ID
def get_username(uid):
    try:
        return pwd.getpwuid(uid).pw_name
    except KeyError:
        return str(uid)


# .dynsym-> symbol tables dedicated to dynamically linked symbols
def get_sym(filename):
    with open(filename, "rb") as f:
        elf = ELFFile(f)
        symbol_table = elf.get_section_by_name(".dynsym")
        for symbol in symbol_table.iter_symbols():
            if symbol.name == "readline_internal_teardown":
                return "readline_internal_teardown"
    return "readline"


name = "/bin/bash"
sym = get_sym(name)

bpf_text = """
#include <uapi/linux/ptrace.h>
#include <linux/sched.h>

struct str_t {
    u32 pid;
    u32 uid;
    char str[80];
};

BPF_PERF_OUTPUT(events);

int printret(struct pt_regs *ctx) {
    struct str_t data  = {};
    char comm[TASK_COMM_LEN] = {};
    if (!PT_REGS_RC(ctx))
        return 0;
    data.pid = bpf_get_current_pid_tgid() >> 32;
    data.uid = bpf_get_current_uid_gid() >> 32;
    bpf_probe_read_user(&data.str, sizeof(data.str), (void *)PT_REGS_RC(ctx));

    bpf_get_current_comm(&comm, sizeof(comm));
    if (comm[0] == 'b' && comm[1] == 'a' && comm[2] == 's' && comm[3] == 'h' && comm[4] == 0 ) {
        events.perf_submit(ctx,&data,sizeof(data));
    }

    return 0;
};
"""

b = BPF(text=bpf_text)
b.attach_uretprobe(name=name, sym=sym, fn_name="printret")
print("%-9s %-7s %-10s %s" % ("TIME", "PID", "USER", "COMMAND"))


def print_event(cpu, data, size):
    event = b["events"].event(data)
    username = get_username(event.uid)
    print(
        "%-9s %-7d %-10s %s"
        % (
            strftime("%H:%M:%S"),
            event.pid,
            username,
            event.str.decode("utf-8", "replace"),
        )
    )


b["events"].open_perf_buffer(print_event)
while 1:
    try:
        b.perf_buffer_poll()
    except KeyboardInterrupt:
        exit()
