# Computer Forensics - eBPF

Welcome to the Computer Forensics course repository!\
This repository contains exercises and semester project for Computer Forensics course.

## Contents

- **[eBPF Project](ebpf-project/)**
- **[Labs](Labs/)**
  - [Lab01](Labs/Lab01/)
  - [Lab02](Labs/Lab02/)
  - [Lab03](Labs/Lab03/)
  - [Lab04](Labs/Lab04/)

## Setup

For laboratory exercises, we utilize Jupyter notebooks, while for the semester project,
we leverage BCC (BPF Compiler Collection) and bpftrace.

### eBPF Project

To ensure compatibility and functionality, the project has been tested on Fedora Linux.
Install BCC (BPF Compiler Collection) and bpftrace by running the following command in your terminal:

```bash
sudo dnf install bcc bpftrace python-devel
```

This command will install the necessary dependencies and tools required for the eBPF project on Fedora Linux.
If you want to test project on other Linux distors, you should find proper way to setup bcc on your Linux distro.
