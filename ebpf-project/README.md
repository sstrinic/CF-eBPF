# eBPF project

eBPF is a revolutionary technology with origins in the Linux kernel that can run sandboxed programs in a privileged context such as the operating system kernel. It is used to safely and efficiently extend the capabilities of the kernel without requiring to change kernel source code or load kernel modules.

Historically, the operating system has always been an ideal place to implement observability, security, and networking functionality due to the kernel’s privileged ability to oversee and control the entire system. At the same time, an operating system kernel is hard to evolve due to its central role and high requirement towards stability and security. The rate of innovation at the operating system level has thus traditionally been lower compared to functionality implemented outside of the operating system. [[1]](https://ebpf.io/what-is-ebpf/)

In this semester project bcc (BPF Compiler Collection) toolkit is being used.
BCC tracing tools can be on next image:

<center><a href="/data/bcc_tracing_tools_2019.png"><img src="/data/bcc_tracing_tools_2019.png" border=0 width=700></a></center>

**Scripts:**

- users-command.py: Print what command is run by which user
- vlan-learning.py: Learn VLANs on ethernet

SchedCLS programs are attached to the peer of the networking interface of the containers on the host according to the filtering configuration.
