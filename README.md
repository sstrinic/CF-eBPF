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

For laboratory exercises, we utilized **Jupyter** notebooks, while for the semester project,
**BCC** (BPF Compiler Collection) and **bpftrace** are used.  

### Laboratory exercises

TBD

### eBPF Project

To ensure compatibility and functionality, the project has been tested on Fedora Linux.
Install BCC (BPF Compiler Collection) and bpftrace by running the following command in your terminal:

```bash
sudo dnf install bcc bpftrace python-devel
sudo pip3 install -r requirements.txt
```

This command will install the necessary dependencies and tools required for the eBPF project on Fedora Linux.
If you want to test project on other Linux distors, you should find proper way to setup bcc and bpftrace on your Linux distro.

## Execution

For running scripts first change dir to ebpf-project with:  
`cd ebpf-project/`  
To run the code for bcc scripts use:  
`sudo python3 bcc.py`  
To run the code for bpftrace scripts use:  
`sudo python3 bpftrace.py`
