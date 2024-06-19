# Computer Forensics - eBPF

![GitHub License](https://img.shields.io/github/license/sstrinic/CF-eBPF)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/sstrinic/CF-eBPF)
![GitHub repo size](https://img.shields.io/github/repo-size/sstrinic/CF-eBPF)

Welcome to the Computer Forensics course repository!  
This repository contains exercises and semester project for Computer Forensics course.

## Contents

- **[Semester project](ebpf-project/)**
- **[Laboratory exercises](Labs/)**
  - [Lab01](Labs/Lab01/)
  - [Lab02](Labs/Lab02/)
  - [Lab03](Labs/Lab03/)
  - [Lab04](Labs/Lab04/)

## Setup

For laboratory exercises, **Jupyter** notebooks were utilized.
For the semester project, the **BCC** (BPF Compiler Collection) and **bpftrace** tools were employed.  

### Laboratory exercises

Use following commands to setup environment and install Jupyter notebook:

```bash
python -m venv labs
cd labs
source bin/activate
pip install jupyter
```

Jupyter notebook files have extension **.ipynb**.

### Semester project - eBPF

These commands will install the necessary dependencies and tools required for the eBPF project on **Fedora Linux**.  
If you want to test project on other Linux distros, you should find proper way to setup **BCC** and **bpftrace** on your Linux distro.  

Install BCC (BPF Compiler Collection) and bpftrace by running the following commands in your terminal:

```bash
sudo dnf install bcc bpftrace python-devel
sudo pip3 install -r requirements.txt
```

## Execution

To run scripts first change directory to ebpf-project with:  
`cd ebpf-project/`  

To run the code for bcc scripts use:  
`sudo python3 bcc.py`  

To run the code for bpftrace scripts use:  
`sudo python3 bpftrace.py`
