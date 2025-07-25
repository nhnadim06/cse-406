procs = int(input("Enter number of processes: "))

procs_list = []
for i in range(procs):
    process_id = f"P{i+1}"
    arrival_time = int(input(f"Enter Arrival Time for {process_id}: "))
    burst_time = int(input(f"Enter Burst Time for {process_id}: "))
    procs_list.append([process_id, arrival_time, burst_time])

for i in range(procs):
    for j in range(i + 1, procs):
        if procs_list[i][1] > procs_list[j][1]:
            procs_list[i], procs_list[j] = procs_list[j], procs_list[i]

completed_processes = []
current_time = 0

while procs_list:
    ready_queue = []
    for process in procs_list:
        if process[1] <= current_time:
            ready_queue.append(process)
    if not ready_queue:
        current_time += 1
        continue
    shortest_index = 0
    for i in range(1, len(ready_queue)):
        if ready_queue[i][2] < ready_queue[shortest_index][2]:
            shortest_index = i
    shortest_process = ready_queue[shortest_index]

    procs_list.remove(shortest_process)

    pid = shortest_process[0]
    at = shortest_process[1]
    bt = shortest_process[2]
    ct = current_time + bt
    tat = ct - at
    wt = tat - bt

    completed_processes.append([pid, at, bt, ct, tat, wt])
    current_time = ct

for i in range(len(completed_processes)):
    for j in range(i + 1, len(completed_processes)):
        if completed_processes[i][0] > completed_processes[j][0]:
            completed_processes[i], completed_processes[j] = completed_processes[j], completed_processes[i]
print(f"\n{'Process':<8}{'Arrival':<10}{'Burst':<10}{'CT':<10}{'TAT':<10}{'WT':<10}")
for proc in completed_processes:
    print(f"{proc[0]:<8}{proc[1]:<10}{proc[2]:<10}{proc[3]:<10}{proc[4]:<10}{proc[5]:<10}")



total_wt = 0
for proc in completed_processes:
    total_wt += proc[5]
avg_wt = total_wt / process
print(f"\nAverage waiting time: {avg_wt:.2f}")