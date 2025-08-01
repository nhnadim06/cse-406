def rr(pid, at, bt, quant):
    n = len(pid)

    processes = [(pid[i], at[i], bt[i], i) for i in range(n)]


    processes.sort(key=lambda x: x[1])

    pids = [p[0] for p in processes]
    at = [p[1] for p in processes]
    bt = [p[2] for p in processes]
    original_index = [p[3] for p in processes]

    rt = bt[:]
    ct = [0] * n
    done = 0
    time = 0
    queue = []

    while done < n:
        for i in range(n):
            if at[i] <= time and rt[i] > 0 and i not in queue:
                queue.append(i)
        if not queue:
            time += 1
            continue

        i = queue.pop(0)

        if rt[i] > quant:
            time += quant
            rt[i] -= quant
        else:
            time += rt[i]
            rt[i] = 0
            ct[i] = time
            done += 1

        for j in range(n):
            if at[j] > time - quant and at[j] <= time and rt[j] > 0 and j not in queue:
                queue.append(j)

        if rt[i] > 0 and i not in queue:
            queue.append(i)

    result = [None] * n
    for i in range(n):
        tat = ct[i] - at[i]
        wt = tat - bt[i]
        result[original_index[i]] = (pids[i], at[i], bt[i], ct[i], tat, wt)


    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    for res in result:
        print(f"{res[0]}\t{res[1]}\t{res[2]}\t{res[3]}\t{res[4]}\t{res[5]}")




n = int(input("Enter the number of processes: "))
pid = [f"P{i+1}" for i in range(n)]
arrival_times = []
burst_times = []

for i in range(n):
    arrival_time_input = int(input(f"Enter the arrival time for process P{i+1}: "))
    burst_time_input = int(input(f"Enter the burst time for process P{i+1}: "))
    arrival_times.append(arrival_time_input)
    burst_times.append(burst_time_input)

quant = int(input("Enter the time quantum: "))
rr(pid, arrival_times, burst_times, quant)
