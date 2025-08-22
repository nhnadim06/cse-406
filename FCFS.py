procs = int(input("Number of processes: "))

at = []
bt = []

for i in range(procs):
    atime = int(input(f"Arrival Time for Process P{i+1}: "))
    btime = int(input(f"Burst Time for Process P{i+1}: "))
    at.append(atime)
    bt.append(btime)
for i in range(procs):
    for j in range(i + 1, procs):
        if at[i] > at[j]:
            at[i], at[j] = at[j], at[i]
            bt[i], bt[j] = bt[j], bt[i]




ct = [0] * procs
tat = [0] * procs
wt = [0] * procs

current_time = 0

for i in range(procs):
    if current_time < at[i]:
        current_time = at[i]
    current_time += bt[i]
    ct[i] = current_time
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]
print("\nId\tAT\tBT\tCT\tWT\tTAT")
for i in range(procs):
    print(f"P{i+1}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{wt[i]}\t{tat[i]}")
avg_wt = int(sum(wt) / procs) 
avg_tat = int(sum(tat) / procs)
print(f"\navg waiting Time: {avg_wt}")
print(f"avg turnaround Time: {avg_tat}")
