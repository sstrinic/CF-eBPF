# eBPF project

eBPF is a revolutionary technology with origins in the Linux kernel that can run sandboxed programs in a privileged context such as the operating system kernel. It is used to safely and efficiently extend the capabilities of the kernel without requiring to change kernel source code or load kernel modules.

Historically, the operating system has always been an ideal place to implement observability, security, and networking functionality due to the kernel’s privileged ability to oversee and control the entire system. At the same time, an operating system kernel is hard to evolve due to its central role and high requirement towards stability and security. The rate of innovation at the operating system level has thus traditionally been lower compared to functionality implemented outside of the operating system. [[1]](https://ebpf.io/what-is-ebpf/)

In this semester project bcc (BPF Compiler Collection) toolkit is being used.
BCC tracing tools can be on next image:

<a href="/data/bcc_tracing_tools_2019.png"><img src="/data/bcc_tracing_tools_2019.png" border="0" width="700"></a>

**Python scripts and bpftrace code:**

- users_command.py: Print what command is run by which user (uretprobe)
- filetop.py: Top for files, R/W by processes (kprobe)
- xdp_drop_count.py: Count dropped packets by XDP
- tracepoint.py: Testing personal tracepoint code
- opensnoop.bt: Trace open() syscalls (tracepoint)

<a href="/data/eBPF_example_3_scripts.png"><img src="/data/eBPF_example_3_scripts.png" border="0" width="700"></a>

SchedCLS programs are attached to the peer of the networking interface of the containers on the host according to the filtering configuration.

## Probes

- **Kernel probes**
    These give you dynamic access to internal components in the kernel.
  - kprobes
  - kretprobes
- **Tracepoints**
    These provide static access to internal components in the kernel.  
  - tracepoint
  - rawtracepoint  
- **User-space probes**
    These give you dynamic access to programs running in user-space.
  - uprobes
  - uretprobes
- **User statically defined tracepoints(USDT)**
    These allow static access to programs running in user-space.

## XDP - eXpress Data Path

It enables custom packet processing to be executed directly within the network driver, before the packets are passed to the kernel's networking stack.

## Bpftrace

The bpftrace (bt) language is inspired by the D language used by dtrace and uses the same program structure. Each script consists of a preamble and one or more action blocks. Preprocessor and type definitions take place in the preamble.[[2]](https://github.com/bpftrace/bpftrace/blob/master/man/adoc/bpftrace.adoc)  
Action block structure:

```D
probe[,probe]
/predicate/ {
  action
}
```

The predicate is an optional condition that must be met for the action to be executed.

## List probes & tracepoints

```bash
sudo perf list
cat /sys/kernel/debug/tracing/available_events
sudo bpftrace -l
sudo bpftrace -l "rawtracepoint:*" | wc -l
sudo bpftrace -l 'kprobe:*'
```
