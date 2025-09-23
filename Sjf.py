processes = [
    {"pid": "P1", "at": 0, "bt": 6},
    {"pid": "P2", "at": 1, "bt": 8},
    {"pid": "P3", "at": 2, "bt": 7},
    {"pid": "P4", "at": 3, "bt": 3},
]

n = len(processes)
time = 0
completed = []
waiting_time = {}
turnaround_time = {}
completion_time = {}
gantt_chart = []

while len(completed) < n:
   
    available = [p for p in processes if p["at"] <= time and p["pid"] not in completed]
    
    if available:
      
        current = min(available, key=lambda x: x["bt"])
        start = time
        time += current["bt"]
        finish = time
        
        completed.append(current["pid"])
        gantt_chart.append((current["pid"], start, finish))
        
       
        completion_time[current["pid"]] = finish
        turnaround_time[current["pid"]] = finish - current["at"]
        waiting_time[current["pid"]] = turnaround_time[current["pid"]] - current["bt"]
    else:
        time += 1 


print("\n--- SJF CPU Scheduling ---")
print("PID\tAT\tBT\tCT\tTAT\tWT")
for p in processes:
    pid = p['pid']
    print(f"{pid}\t{p['at']}\t{p['bt']}\t{completion_time[pid]}\t{turnaround_time[pid]}\t{waiting_time[pid]}")

avg_wt = sum(waiting_time.values()) / n
avg_tat = sum(turnaround_time.values()) / n
print(f"\nAverage Waiting Time = {avg_wt:.2f}")
print(f"Average Turnaround Time = {avg_tat:.2f}")

print("\nGantt Chart:")
for g in gantt_chart:
    print(f"| {g[0]} ({g[1]} → {g[2]}) ", end="")
print("|")
