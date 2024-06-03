# eBPF project

eBPF is a revolutionary technology with origins in the Linux kernel that can run sandboxed programs in a privileged context such as the operating system kernel. It is used to safely and efficiently extend the capabilities of the kernel without requiring to change kernel source code or load kernel modules.

Historically, the operating system has always been an ideal place to implement observability, security, and networking functionality due to the kernel’s privileged ability to oversee and control the entire system. At the same time, an operating system kernel is hard to evolve due to its central role and high requirement towards stability and security. The rate of innovation at the operating system level has thus traditionally been lower compared to functionality implemented outside of the operating system. [[1]](https://ebpf.io/what-is-ebpf/)

In this semester project **bcc** (BPF Compiler Collection) toolkit and **bpftrace** are being used.
BCC tracing tools can be seen on next image:

<a href="/data/bcc_tracing_tools_2019.png"><img src="/data/bcc_tracing_tools_2019.png" border="0" width="700"></a>

## Python and bpftrace scripts

- Python:

  1. users_command.py: Print what command is run by which user (uretprobe)
  2. filetop.py: Top for files, R/W by processes (kprobe)
  3. xdp_drop_count.py: Count dropped packets by XDP
  4. tracepoint.py: Testing personal tracepoint code

- Bpftrace:

  1. opensnoop.bt: Trace open() syscalls (tracepoint)
  2. kprobes.bt: Examples of kprobes
  3. tracepoints.bt: Examples of tracepoints

### Python scripts  

<a href="/data/python_scripts_ex.png"><img src="/data/python_scripts_ex.png" border="0" width="700"></a>

### Bpftrace scripts  

<a href="/data/bpftrace_scripts_ex.png"><img src="/data/bpftrace_scripts_ex.png" border="0" width="700"></a>

## Probes

- **Kernel probes**
    Dynamic access to internal components in the kernel.
  - kprobes
  - kretprobes
- **Tracepoints**
    Static access to internal components in the kernel.  
  - tracepoint
  - rawtracepoint  
- **User-space probes**
    Dynamic access to programs running in user-space.
  - uprobes
  - uretprobes
- **User statically defined tracepoints(USDT)**
    Static access to programs running in user-space.

### List probes & tracepoints

```bash
sudo perf list
cat /sys/kernel/debug/tracing/available_events
sudo bpftrace -l
sudo bpftrace -l "rawtracepoint:*" | wc -l
sudo bpftrace -l 'kprobe:*'
```

### Tracepoints formats

<a href="/data/sys_enter_read.png"><img src="/data/sys_enter_read.png" border="0" width="500"></a>  
<a href="/data/sys_exit_read.png"><img src="/data/sys_exit_read.png" border="0" width="500"></a>  
<a href="/data/sys_mkdir.png"><img src="/data/sys_mkdir.png" border="0" width="500"></a>  

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

## Example of digging in kernel - bpftrace + kprobe

Inside kernel definition of **arp_create**, located in arp.h:

<a href="/data/arp_create.png"><img src="/data/arp_create.png" border="0" width="500"></a>

Implementation inside kprobes.bt for **arp_create** kprobe:

```D
kprobe:arp_create {
  $sip = arg4;
  $dip = arg2;
  $smac = sarg0; // arg6
  $dmac = sarg1; // arg5
  time("%H:%M:%S ");
  printf("SRC: %16s %s", ntop($sip), macaddr($smac));
  printf(" -> DST: %16s %s\n", ntop($dip), macaddr($dmac));
}
```

## Other

TBD  

### XDP - eXpress Data Path

Enables custom packet processing to be executed directly within the network driver, before the packets are passed to the kernel's networking stack.  

Inspect ELF files with: `readelf -Ws /bin/bash`  
SchedCLS programs are attached to the peer of the networking interface of the containers on the host according to the filtering configuration.
