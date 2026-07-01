# CSE 406 — Operating System Lab 🖥️

Python implementations of classic **CPU scheduling**, **disk scheduling**, and **page replacement** algorithms, written as part of the CSE 406 Operating System Lab course.

## 📋 Algorithms Implemented

### CPU Scheduling
| File | Algorithm |
|---|---|
| `FCFS.py` | First Come First Serve |
| `SJF.py`, `Sjf.py` | Shortest Job First |
| `PriorityScheduling.py` | Priority Scheduling |
| `RoundRobin.py` | Round Robin |

### Disk Scheduling
| File | Algorithm |
|---|---|
| `FCFS_DiskScheduling.py` | First Come First Serve (Disk) |
| `SSTF_DiskScheduling.py` | Shortest Seek Time First |
| `CScanDiskScheduling.py` | C-SCAN |
| `scandiskscheduling.py` | SCAN |

### Page Replacement
| File | Algorithm |
|---|---|
| `FIFOPageReplacement.py` | FIFO Page Replacement |
| `FIFO(final_exam).py` | FIFO Page Replacement (exam variant) |

## 🧰 Tech Stack

- **Language:** Python 3

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed

### Running a script

```bash
git clone https://github.com/nhnadim06/cse-406.git
cd cse-406
python FCFS.py
```

Most CPU/disk scheduling scripts will prompt you for input (number of processes, arrival/burst times, disk requests, head position, etc.) directly in the terminal. A few scripts (e.g. `CScanDiskScheduling.py`, `Sjf.py`) use hardcoded sample data inside the file — edit the values at the top of the script to test different cases.

## 📁 Project Structure

```
cse-406/
├── FCFS.py                    # CPU: First Come First Serve
├── SJF.py / Sjf.py            # CPU: Shortest Job First
├── PriorityScheduling.py      # CPU: Priority Scheduling
├── RoundRobin.py               # CPU: Round Robin
├── FCFS_DiskScheduling.py     # Disk: FCFS
├── SSTF_DiskScheduling.py     # Disk: SSTF
├── CScanDiskScheduling.py     # Disk: C-SCAN
├── scandiskscheduling.py      # Disk: SCAN
├── FIFOPageReplacement.py     # Page Replacement: FIFO
└── FIFO(final_exam).py        # Page Replacement: FIFO (exam variant)
```

## 📄 License

This project currently has no license specified.

## 📬 Contact

Maintainer: [nhnadim06](https://github.com/nhnadim06)
