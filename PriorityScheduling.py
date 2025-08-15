
n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    pid = f"P{i+1}" 
    at = int(input(f"Enter Arrival Time for {pid}: "))
    bt = int(input(f"Enter Burst Time for {pid}: "))
    pr = int(input(f"Enter Priority for {pid}: "))
    processes.append({"PID": pid, "AT": at, "BT": bt, "Priority": pr})

time = 0
completed = []
ready_queue = []
processes_left = processes.copy()

while processes_left or ready_queue:
    for p in processes_left[:]:
        if p["AT"] <= time:
            ready_queue.append(p)
            processes_left.remove(p)

    if ready_queue:
        ready_queue.sort(key=lambda x: (x["Priority"], x["AT"]))
        current = ready_queue.pop(0)

        start_time = max(time, current["AT"])
        completion_time = start_time + current["BT"]

        current["CT"] = completion_time
        current["TAT"] = current["CT"] - current["AT"]
        current["WT"] = current["TAT"] - current["BT"]

        completed.append(current)
        time = completion_time
    else:
        time += 1

print("\nPID\tAT\tBT\tPr\tCT\tTAT\tWT")
total_TAT = 0
total_WT = 0

for p in completed:
    print(f"{p['PID']}\t{p['AT']}\t{p['BT']}\t{p['Priority']}\t{p['CT']}\t{p['TAT']}\t{p['WT']}")
    total_TAT += p['TAT']
    total_WT += p['WT']

avg_TAT = total_TAT / n
avg_WT = total_WT / n
print(f"\nAverage Turnaround Time: {avg_TAT:.2f}")
print(f"Average Waiting Time: {avg_WT:.2f}")