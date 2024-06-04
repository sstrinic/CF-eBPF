# eBPF project

eBPF is a revolutionary technology with origins in the Linux kernel that can run sandboxed programs in a privileged context such as the operating system kernel. It is used to safely and efficiently extend the capabilities of the kernel without requiring to change kernel source code or load kernel modules.

Historically, the operating system has always been an ideal place to implement observability, security, and networking functionality due to the kernel’s privileged ability to oversee and control the entire system. At the same time, an operating system kernel is hard to evolve due to its central role and high requirement towards stability and security. The rate of innovation at the operating system level has thus traditionally been lower compared to functionality implemented outside of the operating system. [[1]](https://ebpf.io/what-is-ebpf/)

<a href="/images/ebpf_overview.png"><img src="/images/ebpf_overview.png" border="0" width="700" alt="eBPF overview"/></a>

In this semester project **bcc** (BPF Compiler Collection) toolkit and **bpftrace** are being used.
BCC tracing tools can be seen on next image:

<a href="/images/bcc_tracing_tools_2019.png"><img src="/images/bcc_tracing_tools_2019.png" border="0" width="700" alt="BCC tracing tools"/></a>

## Python and bpftrace scripts

### Python scripts example

 1. users_command.py: Print what command is run by which user (uretprobe)
 2. filetop.py: Top for files, R/W by processes (kprobe)
 3. xdp_drop_count.py: Count dropped packets by XDP
 4. tracepoint.py: Testing personal tracepoint code

<a href="/images/python_scripts_ex.png"><img src="/images/python_scripts_ex.png" border="0" width="700" alt="Python scripts example"/></a>

### Bpftrace scripts example

 1. opensnoop.bt: Trace open() syscalls (tracepoint)
 2. key_pressed.bt: Prints which key is pressed and top 10 pressed after exiting
 3. others.bt: Prints details of mkdir calls, IP and MAC addresses when ARP is sent

<a href="/images/bpftrace_scripts_ex.png"><img src="/images/bpftrace_scripts_ex.png" border="0" width="700" alt="Bpftrace scripts example"/></a>

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

<a href="/images/sys_enter_read.png"><img src="/images/sys_enter_read.png" border="0" width="500" alt="Sys enter read format"/></a>  
<a href="/images/sys_exit_read.png"><img src="/images/sys_exit_read.png" border="0" width="500" alt="Sys exit read format"/></a>  
<a href="/images/sys_mkdir.png"><img src="/images/sys_mkdir.png" border="0" width="500" alt="Sys mkdir format"/></a>

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

<a href="/images/arp_create.png"><img src="/images/arp_create.png" border="0" width="500" alt="Arp create kernel"/></a>

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

<a href="/images/xdp.png"><img src="/images/xdp.png" border="0" width="700" alt="XDP path"/></a>

Inspect ELF files with: `readelf -Ws /bin/bash`  
SchedCLS programs are attached to the peer of the networking interface of the containers on the host according to the filtering configuration.
